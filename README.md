
# Frequency word analyzer based on a job title and tags in position 
 - for [https://berlinstartupjobs.com](https://berlinstartupjobs.com/engineering/)
 - for [https://stackoverflow.com](https://stackoverflow.com/)

## `berlin-startup-jobs` simple words analyzer


#### Based on https://github.com/GamjaPower/berlinstartupjobs.git 


## Requirements

- Python 3.7

## Quick start

1. clone repository, install libs check outdated
    ```sh
    git clone https://github.com/dstoianov/berlin-startup-jobs-analyzer.git
    cd berlin-startup-jobs-analyzer/
    python3 -m venv .venv or via virtualenv .venv --python=python3
    source .venv/bin/activate
    pip install -r requirements.txt
    pip list --outdated  # show outdated libs
    ```
1. collect and analyze data
    ```sh
    python src/crawler.py
    python src/analyzer.py
    ```


## Results Analysis

Description:

- the first parameter is the `technology name` 
- the second parameter is the `frequent occurrence`

Output Results:
 - see files in `adoc` format in repo


###  Posted Statistics: 

| Date   | BerlinStartupJobs Tags |  BerlinStartupJobs Urls | StackOverFlow Tags  |  StackOverFlow Urls |
|----------|:-------------:|:------:|:----:|:----:|
| 2020-01| 907| 223| 2020| 485 |
| 2020-02| 1020| 248| 2122| 506 |
| 2020-03| 908| 209| 1960| 473 |
| 2020-04| 830| 196| 1605| 390 |
| 2020-05| 682| 162| 1294| 318 |
| 2020-06| 430| 113| 1138| 278 |

