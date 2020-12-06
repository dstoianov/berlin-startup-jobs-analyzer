import operator
from src import logger as log

from src import read, data_to_replace


def tuning_stats(text: str) -> str:
    for value in data_to_replace:
        text = text.replace(value[0], value[1])

    return text


def analyze_urls(file_name: str):
    urls = read(file_name)

    log.info("===== analyze urls =====")
    total = len(urls.split('\n'))
    log.info(f"Total URLs '{total}' in analyze")
    log.info("===== analyze urls =====")

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

    skip_word = ['d', 'm', 'w', 'f', 'in', 'div', 'for', 'of', 'x', 'se', 'gmbh', 'berlin']
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

    log.info("===== analyze tags =====")
    total = len(tags.split('\n'))
    log.info(f"Total tags '{total}' in analyze")
    log.info("===== analyze tags =====")

    tags = tuning_stats(tags)

    frequency = {}
    for word in tags.split('\n'):
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    items = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)

    for x in items:
        if x[1] > 1:
            print(x)


def monthly_stats():
    log.info("Total count...")
    header = ["tags_bsj", "urls_bsj", "tags_so", "urls_so"]
    print(header)

    for month in ["01", "02", "03", "04", "05", "06", "08", "10", "11"]:
        res = "| 2020-" + month
        for file in header:
            records = read(f"data/{month}/2020_{month}_{file}.txt")
            res += "| " + str(len(records.split('\n')))

        print(res + " |")


if __name__ == '__main__':
    folder = "data/11/2020_11_"
    analyze_urls(f'{folder}urls_bsj.txt')
    analyze_tags(f'{folder}tags_bsj.txt')

    # analyze_urls(f'{folder}urls_so.txt')
    # analyze_tags(f'{folder}tags_so.txt')
    monthly_stats()
