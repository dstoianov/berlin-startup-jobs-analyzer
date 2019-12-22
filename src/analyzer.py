import operator


def read(file_name: str):
    with open(file_name, 'r') as file:
        return file.read()


def analyzer_urls():
    urls = read('urls.txt')

    print("===== analyze urls =====" * 3)

    urls = urls.replace('https://berlinstartupjobs.com/engineering/', '')
    urls = urls.replace('/', '')

    urls = urls.replace('full-stack', 'fullstack')
    urls = urls.replace('back-end', 'backend')
    urls = urls.replace('front-end', 'frontend')
    urls = urls.replace('dev-ops', 'devops')
    urls = urls.replace('team-lead', 'teamlead')
    urls = urls.replace('tech-lead', 'techlead')
    urls = urls.replace('science', 'scientist')
    urls = urls.replace('data-scientist', 'datascientist')
    urls = urls.replace('quality-assurance', 'qa')
    urls = urls.replace('-js-', '-javascript-')
    urls = urls.replace('sr-', 'senior-')

    urls = urls.replace('\n', '-')

    skip_word = ['m', 'w', 'f', 'div', 'x', 'd', 'gmbh', 'finleap']
    frequency = {}
    for word in urls.split('-'):
        if word in skip_word:
            continue
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    items = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
    for x in items:
        print(x)


def analyzer_tags():
    tags = read('tags.txt')

    print("===== analyze tags =====" * 3)

    tags = tags.replace('go\n', 'golang\n')
    tags = tags.replace('postgres\n', 'postgresql\n')
    tags = tags.replace('quality assurance', 'qa')
    tags = tags.replace('full stack', 'fullstack')
    tags = tags.replace('full-stack', 'fullstack')
    tags = tags.replace('dev ops', 'devops')
    tags = tags.replace('qa engineer', 'qa')
    tags = tags.replace('react.js', 'react')
    tags = tags.replace('front-end', 'frontend')
    tags = tags.replace('data scientist', 'data science')
    tags = tags.replace('nodejs\n', 'node.js\n')
    tags = tags.replace('node\n', 'node.js\n')
    tags = tags.replace('fullstack development\n', 'fullstack developer\n')

    frequency = {}
    for word in tags.split('\n'):
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    items = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
    for x in items:
        print(x)


if __name__ == '__main__':
    analyzer_urls()
    analyzer_tags()
