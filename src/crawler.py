import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def crawl():
    target_urls = []
    try:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), )
        for page in range(1, 10):
            base_url = 'http://berlinstartupjobs.com/engineering/'
            if page != 1:
                base_url = base_url + 'page/' + str(page)
            print(f"open url '{base_url}'")
            driver.get(base_url)

            elements = driver.find_elements_by_css_selector('.jobs-list-items li')
            for elem in elements:
                href = elem.find_element_by_css_selector('h4 a').get_attribute('href')
                target_urls.append(href)
            print(f"wait for {str(1 + page)} sec..")
            time.sleep(1 + page)
    except:
        print("Exception happens, close WebDriver..")
        driver.quit()
    finally:
        print("Close WebDriver...")
        driver.quit()
        print(f"Collect entries '{str(len(target_urls))}'")
        with open('urls.txt', 'w') as file:
            file.write('\n'.join(target_urls))


if __name__ == '__main__':
    crawl()
