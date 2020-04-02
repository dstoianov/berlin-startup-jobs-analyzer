import time
import random
import datetime

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def save_to_file(file_name: str, data_list: list):
    dt = datetime.datetime.today()
    number = f"{dt.year}-{dt.month}"
    file_n = f"03_{file_name}.txt"
    write_text(file_n, data_list)


def write_text(file_name: str, values: list):
    if len(values) > 0:
        print(f"Collect entries '{str(len(values))}' for '{file_name}'")
        with open(file_name, 'w') as file:
            file.write('\n'.join(values))
    else:
        print("No data to write!")


def sleep_as_human():
    wait = random.randrange(5) + 1
    print(f"wait for {str(wait)} sec..")
    time.sleep(wait)  # simulate that you are human :)


def crawl_startup_jobs():
    target_urls = []
    target_tags = []
    try:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), )
        driver.maximize_window()

        for page in range(1, 11):
            base_url = 'http://berlinstartupjobs.com/engineering/'
            if page != 1:
                base_url = base_url + 'page/' + str(page)
            print(f"open url '{base_url}'")
            driver.get(base_url)

            elements = driver.find_elements_by_css_selector('.jobs-list-items li')
            for elem in elements:
                href = elem.find_element_by_css_selector('h4 a').get_attribute('href')
                target_urls.append(href)

                tags = elem.find_elements_by_css_selector('.links-box a')
                for tag in tags:
                    target_tags.append(tag.text.lower())

            sleep_as_human()
    except Exception as e:
        print(f"Exception happens, close WebDriver.. {str(e)}")
    finally:
        print("Close WebDriver...")
        driver.quit()
        save_to_file('urls_bsj', target_urls)
        save_to_file('tags_bsj', target_tags)


def crawl_stack_overflow():
    target_urls = []
    target_tags = []
    try:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), )
        driver.maximize_window()
        for page in range(1, 22):
            base_url = f"https://stackoverflow.com/jobs?l=Berlin%2c+Germany&d=50&u=Km&sort=i&pg={page}"
            print(f"open url '{base_url}'")
            driver.get(base_url)

            elements = driver.find_elements_by_css_selector('.listResults .-job')
            for elem in elements:
                href = elem.find_element_by_css_selector('h2 a').get_attribute('href')
                target_urls.append(href)

                tags = elem.find_elements_by_css_selector('div .post-tag')
                for tag in tags:
                    tag = tag.text.lower()
                    if len(tag) > 0:
                        # print(f"add tag '${tag}'")  # for debug only
                        target_tags.append(tag)

            sleep_as_human()
    except Exception as e:
        print(f"Exception happens, close WebDriver.. {str(e)}")
    finally:
        print("Close WebDriver...")
        driver.quit()
        save_to_file('urls_so', target_urls)
        save_to_file('tags_so', target_tags)


if __name__ == '__main__':
    # crawl_startup_jobs()
    crawl_stack_overflow()
