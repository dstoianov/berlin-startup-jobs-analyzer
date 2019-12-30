import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def write_text(file_name: str, values: list):
    if len(values) > 0:
        print(f"Collect entries '{str(len(values))}' for '{file_name}'")
        with open(file_name, 'w') as file:
            file.write('\n'.join(values))
    else:
        print("No data to write!")


def crawl_startup_jobs():
    target_urls = []
    target_tags = []
    try:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), )
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

            print(f"wait for {str(1 + page)} sec..")
            time.sleep(1 + page)
    except Exception as e:
        print(f"Exception happens, close WebDriver.. {str(e)}")
    finally:
        print("Close WebDriver...")
        driver.quit()
        write_text('urls.txt', target_urls)
        write_text('tags.txt', target_tags)


def crawl_stack_overflow():
    target_urls = []
    target_tags = []
    try:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), )
        for page in range(1, 22):
            base_url = f"https://stackoverflow.com/jobs?l=Berlin%2c+Germany&d=50&u=Km&sort=i&pg={page}"
            print(f"open url '{base_url}'")
            driver.get(base_url)

            elements = driver.find_elements_by_css_selector('.listResults .-job')
            for elem in elements:
                href = elem.find_element_by_css_selector('a').get_attribute('href')
                target_urls.append(href)

                tags = elem.find_elements_by_css_selector('div a')
                for tag in tags:
                    tag = tag.text.lower()
                    if len(tag) > 0:
                        target_tags.append(tag)

            print(f"wait for {str(1 + page)} sec..")
            time.sleep(1 + page)
    except Exception as e:
        print(f"Exception happens, close WebDriver.. {str(e)}")
    finally:
        print("Close WebDriver...")
        driver.quit()
        write_text('urls_so.txt', target_urls)
        write_text('tags_so.txt', target_tags)


if __name__ == '__main__':
    crawl_startup_jobs()
    crawl_stack_overflow()
