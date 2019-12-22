
import operator


def analyzer():
    with open('urls.txt', 'r') as file:
        urls = file.read()
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


if __name__ == '__main__':
    analyzer()
