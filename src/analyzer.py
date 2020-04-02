import operator

from src import read


def tuning_stats(text: str) -> str:
    data_to_replace = [
        ('full-stack', 'fullstack'),
        ('full-stack', 'fullstack'),
        ('full-time', 'fulltime'),
        ('back-end', 'backend'),
        ('front-end', 'frontend'),
        ('dev-ops', 'devops'),
        ('team-lead', 'teamlead'),
        ('tech-lead', 'techlead'),
        ('science', 'scientist'),
        ('data-scientist', 'datascientist'),
        ('qa-engineer', 'qa'),
        ('quality-assurance', 'qa'),
        ('-js-', '-javascript-'),
        ('sr-', 'senior-'),
        ('mid-', 'middle-'),
        ('ruby-on-rails', 'rubyonrails'),
        ('site-reliability-engineer', 'sre'),
        ('reactjs', 'react'),
        ('golang', 'go'),
        ('big-data', 'bigdata'),
        # for Tags
        ('postgres\n', 'postgresql\n'),
        ('quality assurance', 'qa'),
        ('full stack', 'fullstack'),
        ('full-stack', 'fullstack'),
        ('dev ops', 'devops'),
        ('qa engineer', 'qa'),
        ('react.js', 'react'),
        ('front-end', 'frontend'),
        ('data scientist', 'data science'),
        ('nodejs\n', 'node\n'),
        ('node.js\n', 'node\n'),
        ('fullstack development\n', 'fullstack developer\n'),

    ]

    for value in data_to_replace:
        text = text.replace(value[0], value[1])

    return text


def analyze_urls(file_name: str):
    urls = read(file_name)

    print("===== analyze urls =====")
    total = len(urls.split('\n'))
    print(f"Total URLs '{total}' in analyze")
    print("===== analyze urls =====")

    if 'berlinstartupjobs' in urls:
        urls = urls.replace('https://berlinstartupjobs.com/engineering/', '')
        urls = urls.replace('/', '')

    if 'stackoverflow' in urls:
        urls = urls.replace('https://stackoverflow.com/jobs/', '')
        tmp_list = []
        for url in urls.split("\n"):
            url = url.split('?')[0]  # remove request parameters
            url = url.split('/')[1]  # remove job id
            tmp_list.append(url)
        urls = ('\n'.join(tmp_list))

    urls = tuning_stats(urls)

    urls = urls.replace('\n', '-')

    skip_word = ['d', 'm', 'w', 'f', 'in', 'div', 'x', 'se', 'gmbh', 'berlin']
    frequency = {}
    for word in urls.split('-'):
        if word in skip_word:
            continue
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    items = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
    for x in items:
        if x[1] > 1:
            print(x)


def analyze_tags(file_name: str):
    tags = read(file_name)

    print("===== analyze tags =====")
    total = len(tags.split('\n'))
    print(f"Total tags '{total}' in analyze")
    print("===== analyze tags =====")

    tags = tuning_stats(tags)

    frequency = {}
    for word in tags.split('\n'):
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    items = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
    for x in items:
        if x[1] > 1:
            print(x)


if __name__ == '__main__':
    folder = "data/03/03_"
    analyze_urls(f'{folder}urls_bsj.txt')
    analyze_tags(f'{folder}tags_bsj.txt')

    analyze_urls(f'{folder}urls_so.txt')
    analyze_tags(f'{folder}tags_so.txt')
