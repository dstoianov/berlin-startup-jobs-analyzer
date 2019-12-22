import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def write_text(file_name: str, values: list):
    print(f"Collect entries '{str(len(values))}' for '{file_name}'")
    with open(file_name, 'w') as file:
        file.write('\n'.join(values))


def crawl():
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
    except:
        print("Exception happens, close WebDriver..")
        driver.quit()
    finally:
        print("Close WebDriver...")
        driver.quit()
        write_text('urls.txt', target_urls)
        write_text('tags.txt', target_tags)


if __name__ == '__main__':
    crawl()
