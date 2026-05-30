#!/usr/bin/env python3
# Combines per-snapshot JSON files into monthly combined files.
# Extract any tar.gz archives into source/ before running.
# Usage: python combine.py [base_dir]
#   base_dir defaults to the script directory.
#   Reads from <base_dir>/source/YYYY-MM/saturn-*.json
#   Writes to  <base_dir>/stats/YYYY-MM.json
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DIR_PATTERN = re.compile(r'^\d{4}-\d{2}$')
FILE_PATTERN = re.compile(r'^saturn-\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{2}\.json$')


def combine(base_dir: Path) -> None:
    source_dir = base_dir / 'source'
    output_dir = base_dir / 'stats'
    if output_dir.exists():
        for f in output_dir.iterdir():
            f.unlink()
    output_dir.mkdir(exist_ok=True)

    months: dict[str, list] = defaultdict(list)
    count_ok = 0
    count_blank = 0
    count_invalid = 0

    for subdir in sorted(source_dir.iterdir()):
        if not subdir.is_dir() or not DIR_PATTERN.match(subdir.name):
            continue

        for filepath in sorted(subdir.iterdir()):
            if not FILE_PATTERN.match(filepath.name):
                continue

            content = filepath.read_text(encoding='utf-8').strip()

            if not content:
                count_blank += 1
                continue

            try:
                data = json.loads(content)
            except json.JSONDecodeError:
                print(f'WARNING: invalid JSON in {filepath}', file=sys.stderr)
                count_invalid += 1
                continue

            try:
                dt = datetime.strptime(filepath.stem, 'saturn-%Y-%m-%d_%H:%M:%S')
            except ValueError:
                print(f'WARNING: unparseable filename {filepath.name}', file=sys.stderr)
                count_invalid += 1
                continue

            month_key = dt.strftime('%Y-%m')
            months[month_key].append({'datetime': dt.isoformat(), 'data': data})
            count_ok += 1

    for month_key, entries in sorted(months.items()):
        entries.sort(key=lambda e: e['datetime'])
        out_path = output_dir / f'{month_key}.json'
        out_path.write_text(json.dumps(entries, indent=2), encoding='utf-8')

    print(f'Written {len(months)} JSON files to {output_dir}/')
    print(f'  valid: {count_ok}  blank: {count_blank}  invalid: {count_invalid}')


if __name__ == '__main__':
    base_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent
    combine(base_dir)
