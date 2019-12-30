
# Frequency word analyzer based on a job title and tags in position 
 - for [https://berlinstartupjobs.com](https://berlinstartupjobs.com/engineering/)
 - for [https://stackoverflow.com](https://stackoverflow.com/)

## `berlin-startup-jobs` simple words analyzer


#### Based on https://github.com/GamjaPower/berlinstartupjobs.git 


## Requirements

- Python 3.7

## Quick start

1. clone repository
    ```bash
    git clone https://github.com/dstoianov/berlin-startup-jobs-analyzer.git
    cd berlin-startup-jobs-analyzer/
    virtualenv .venv --python=python3
    source .venv/bin/activate
    pip install -r requirements.txt
    python src/crawler.py
    python src/analyzer.py
    ```
1. collect and analyze data
    ```bash
    python src/crawler.py
    python src/analyzer.py
    ```


## Results Analysis

Description:

- the first parameter is the `technology name` 
- the second parameter is the `frequent occurrence`

Output Results:
- for Berlin Startup Jobs
```bash
===== analyze urls =====
Total URLs '248' in analyze
===== analyze urls =====
('engineer', 108)
('senior', 84)
('developer', 69)
('software', 38)
('backend', 37)
('frontend', 30)
('fullstack', 22)
('devops', 21)
('javascript', 17)
('finleap', 16)
('qa', 13)
('manager', 12)
('java', 11)
('datascientist', 11)
('android', 10)
('engineering', 10)
('node', 9)
('data', 8)
('of', 8)
('python', 8)
('hellofresh', 8)
('labs', 8)
('analytics', 7)
('react', 7)
('teamlead', 7)
('technology', 7)
('junior', 7)
('fit', 6)
('commercetools', 6)
('learning', 6)
...

===== analyze tags =====
Total tags '1020' in analyze
===== analyze tags =====
('javascript', 43)
('python', 37)
('java', 25)
('react', 25)
('node', 21)
('aws', 19)
('backend', 19)
('go', 18)
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
('php', 7)
('mobile', 7)
('machine learning', 7)
...
```


- for Stack Overflow

```bash
===== analyze urls =====
Total URLs '506' in analyze
===== analyze urls =====
('engineer', 201)
('senior', 188)
('developer', 136)
('backend', 77)
('software', 70)
('java', 60)
('frontend', 51)
('fullstack', 34)
('zalando', 32)
('devops', 31)
('engineering', 29)
('python', 24)
('react', 23)
('lead', 23)
('plus', 22)
('ag', 22)
('javascript', 22)
('data', 22)
('auto1', 20)
('ios', 18)
('manager', 18)
('entwickler', 18)
('delivery', 18)
('hero', 18)
('technologies', 16)
('for', 15)
('ebay', 15)
('junior', 14)
...

===== analyze tags =====
Total tags '2122' in analyze
===== analyze tags =====
('java', 149)
('javascript', 92)
('python', 91)
('amazon-web-services', 86)
('react', 84)
('docker', 48)
('kubernetes', 47)
('node', 44)
('sql', 42)
('microservices', 35)
('spring', 33)
('kotlin', 31)
('ios', 30)
('php', 30)
('linux', 29)
('rest', 27)
('sysadmin', 27)
('scala', 26)
('typescript', 26)
('postgresql', 25)
('c++', 24)
('android', 24)
('go', 23)
('swift', 23)
('css', 22)
('spring-boot', 21)
('cloud', 21)
('continuous-integration', 20)
('mysql', 19)
('jenkins', 18)
('agile', 16)
('html', 16)
('c#', 14)
('mobile', 14)
('user-experience', 13)
('mongodb', 13)
('terraform', 13)
('user-interface', 12)
('elasticsearch', 12)
('machine-learning', 11)
('rubyonrails', 11)
('git', 11)
('apache-spark', 10)
('api', 10)
('angularjs', 10)
...

```

