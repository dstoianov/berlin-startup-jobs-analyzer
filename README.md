
# Frequency word analyzer based on a job title and tags in position [berlinstartupjobs.com](https://berlinstartupjobs.com/engineering/)

## `berlin-startup-jobs` simple words analyzer


#### Based on https://github.com/GamjaPower/berlinstartupjobs.git 


## Requirements

- Python 3.7

## Quick start
 
```sh
git clone https://github.com/dstoianov/berlin-startup-jobs-analyzer.git
cd berlin-startup-jobs-analyzer/
virtualenv .venv --python=python3
source .venv/bin/activate
pip install -r requirements.txt
python src/crawler.py
python src/analyzer.py
```


Description:

- the first parameter is the `technology name` 
- the second parameter is the `frequent occurrence`

Output Results:

```bash
===== analyze urls ========== analyze urls ========== analyze urls =====

('engineer', 112)
('senior', 84)
('developer', 69)
('software', 38)
('backend', 37)
('frontend', 30)
('fullstack', 22)
('devops', 21)
('javascript', 17)
('qa', 13)
('manager', 12)
('java', 11)
('datascientist', 11)
('android', 10)
('engineering', 10)
('berlin', 10)
('node', 9)
('data', 8)
('of', 8)
('python', 8)

.....

===== analyze tags ========== analyze tags ========== analyze tags =====

('javascript', 43)
('python', 37)
('java', 25)
('react', 24)
('node.js', 21)
('aws', 19)
('backend', 19)
('golang', 18)
('qa', 18)
('frontend', 18)
('developer', 17)
('devops', 16)
('android', 13)
('sql', 12)
('development', 12)
('postgresql', 12)
('typescript', 12)
('engineer', 12)
('docker', 11)
('kubernetes', 11)
('fullstack', 11)
('software', 10)
('data science', 10)
('frontend development', 9)
('css', 9)
('ios', 9)
('kotlin', 8)
('mysql', 8)
...
```

