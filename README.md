
# Frequency word analyzer based on a job title [berlinstartupjobs.com](https://berlinstartupjobs.com/engineering/)

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


Output Result:

```bash
('engineer', 114)
('senior', 82)
('developer', 69)
('backend', 38)
('software', 38)
('frontend', 30)
('fullstack', 22)
('devops', 21)
('data', 19)
('javascript', 17)
('finleap', 16)
('div', 15)
('qa', 12)
('manager', 12)
('java', 11)
('android', 10)
('engineering', 10)
```

