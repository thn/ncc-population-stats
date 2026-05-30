# NCC Saturn Population stats 2018-2022

Historical server stats for the unofficial neocron.org Saturn server. Not to be confused with the official Saturn server in Neocron 1 run by ReaKKtor, or with any of the current official Neocron Evolution Servers run by the Neocron Support Team at https://neocron-game.com

The THN had planned to import this into the Stats DB at https://stats.techhaven.org/ but never got around to it. A simple cron job collected the output of the neocron.org server API every 10 minutes, storing the results as timestamped files. All source files can be found in the tar.gz in the `source` directory.

The `stats` directory contains the combined JSON files from the source, in the following format for each month.

```json
[
  {
    "datetime": "2021-08-01T00:00:01",
    "data": {
      "name": "Saturn",
      "status": 0,
      "online": 0
    }
  },
  {
    "datetime": "2021-08-01T00:10:01",
    "data": {
      "name": "Saturn",
      "status": 0,
      "online": 0
    }
  },
  {
    "datetime": "2021-08-01T00:20:01",
    "data": {
      "name": "Saturn",
      "status": 0,
      "online": 0
    }
  }
]
```

There are gaps in the data due to server issues and connection issues. The gaps are listed below. 

## Data gaps > 1 day

Periods where no valid JSON was collected (blank = failed download, counts as a gap).

| From | To | Duration |
|------|----|----------|
| 2018-02-25 22:30 | 2018-03-01 23:40 | 4d 1h 10m |
| 2020-03-24 01:20 | 2020-04-16 21:15 | 23d 19h 55m |
| 2020-04-20 16:45 | 2020-04-22 20:00 | 2d 3h 15m |
| 2020-04-30 06:35 | 2020-05-12 21:40 | 12d 15h 5m |
| 2020-05-12 21:50 | 2020-06-02 20:35 | 20d 22h 45m |
| 2020-06-15 02:45 | 2020-07-27 00:05 | 41d 21h 20m |
| 2022-04-05 03:20 | 2022-08-26 00:40 | 142d 21h 20m |

## Down periods > 1 day

Consecutive `status=0` samples with no data gap between them.

| From | To | Duration |
|------|----|----------|
| 2018-04-09 14:15 | 2018-04-12 15:50 | 3d 1h 35m |
| 2018-08-25 19:05 | 2018-10-02 00:15 | 37d 5h 10m |
| 2018-10-02 02:35 | 2018-10-05 05:30 | 3d 2h 55m |
| 2021-07-20 16:20 | 2022-04-05 03:20 | 258d 11h 0m |
| 2022-08-26 00:40 | 2024-01-10 19:20 | 502d 18h 40m |

## Monthly peak & average population

Only server-up (`status=1`) samples are counted.

| Month | Peak | Avg | Samples |
|-------|-----:|----:|--------:|
| 2018-01 | 16 | 0.99 | 4365 |
| 2018-02 | 26 | 6.95 | 7172 |
| 2018-03 | 31 | 9.23 | 8629 |
| 2018-04 | 24 | 4.93 | 7756 |
| 2018-05 | 12 | 2.41 | 8899 |
| 2018-06 | 10 | 1.36 | 8639 |
| 2018-07 | 10 | 1.03 | 8923 |
| 2018-08 | 11 | 2.29 | 7135 |
| 2018-09 | — | — | 0 |
| 2018-10 | 13 | 2.15 | 7697 |
| 2018-11 | 10 | 1.83 | 8640 |
| 2018-12 | 11 | 1.20 | 8925 |
| 2019-01 | 10 | 1.15 | 8917 |
| 2019-02 | 5 | 0.41 | 8064 |
| 2019-03 | 10 | 0.41 | 8898 |
| 2019-04 | 5 | 0.33 | 8608 |
| 2019-05 | 4 | 0.33 | 8921 |
| 2019-06 | 4 | 0.29 | 8632 |
| 2019-07 | 10 | 1.42 | 8860 |
| 2019-08 | 9 | 1.56 | 8911 |
| 2019-09 | 5 | 0.84 | 8639 |
| 2019-10 | 5 | 0.74 | 8928 |
| 2019-11 | 8 | 1.04 | 8370 |
| 2019-12 | 8 | 0.86 | 8927 |
| 2020-01 | 3 | 0.31 | 8921 |
| 2020-02 | 6 | 0.23 | 8221 |
| 2020-03 | 6 | 0.34 | 6634 |
| 2020-04 | 5 | 0.09 | 3242 |
| 2020-05 | 0 | 0.00 | 3 |
| 2020-06 | 0 | 0.00 | 3528 |
| 2020-07 | 4 | 0.31 | 1438 |
| 2020-08 | 5 | 0.50 | 6556 |
| 2020-09 | 3 | 0.19 | 4319 |
| 2020-10 | 7 | 1.06 | 4459 |
| 2020-11 | 8 | 0.90 | 4287 |
| 2020-12 | 3 | 0.12 | 4464 |
| 2021-01 | 4 | 0.48 | 4463 |
| 2021-02 | 2 | 0.29 | 4032 |
| 2021-03 | 2 | 0.12 | 4464 |
| 2021-04 | 3 | 0.09 | 4320 |
| 2021-05 | 2 | 0.06 | 4464 |
| 2021-06 | 3 | 0.04 | 4320 |
| 2021-07 | 2 | 0.06 | 2831 |
| 2021-08 | — | — | 0 |
| 2021-09 | — | — | 0 |
| 2021-10 | — | — | 0 |
| 2021-11 | — | — | 0 |
| 2021-12 | — | — | 0 |
| 2022-01 | — | — | 0 |
| 2022-02 | — | — | 0 |
| 2022-03 | — | — | 0 |
| 2022-04 | — | — | 0 |
| 2022-08 | — | — | 0 |
| 2022-09 | — | — | 0 |

## Regenerating the stats directory

`combine.py` reads from `source/` and writes one JSON file per month to `stats/`. Extract the tar.gz archive in `source/` before running:

```sh
tar -xzf source/*.tar.gz -C source/
python3 combine.py
```
