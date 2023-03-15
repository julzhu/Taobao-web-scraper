from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from lxml import etree
import csv

driver = webdriver.Chrome()


def get_info(url, page, max_page):
    driver.get(url)
    driver.implicitly_wait(10)
    selector = etree.HTML(driver.page_source)
    infos = selector.xpath('//div[@class="item J_MouserOnverReq  "]')

    for info in infos:
        product_name = info.xpath('div/div/div/a/img/@alt')[0]
        price = info.xpath('div[2]/div/div/strong/text()')[0]
        sales = info.xpath('div[2]/div/div[@class="deal-cnt"]/text()')[0]
        shop = info.xpath('div[2]/div[3]/div/a/span[2]/text()')[0]
        file = [product_name, price, sales, shop, i]
        save(file)
        file = [product_name, price, sales, shop, i]
        save(file)

        print(product_name + '\n',
              price + '\n',
              sales + '\n',
              shop + '\n'
              )

        page = page + 1
        if page <= max_page:
            NextPage(url, page, max_page)
        else:
            pass


def save(item):
    with open(f'{file_name}.csv', 'a+', encoding='utf_8_sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(item)


def NextPage(url, page, max_page):
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//a[@trace="srp_bottom_pagedown"]').click()
    time.sleep(4)
    get_info(driver.current_url, page, max_page)


if __name__ == '__main__':
    file_name = 'lego_info'
    save(['Product Name', 'Price', 'Sales', 'Shop'])
    url = 'https://s.taobao.com/search?q=%E4%B9%90%E9%AB%9875978&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306'
    driver.get(url)
    driver.implicitly_wait(30)  # delay for manual login

    i = '乐高官方旗舰店'  # update search content

    driver.find_element(By.ID, "q").clear()
    driver.find_element(By.ID, "q").send_keys(i)
    driver.find_element(By.XPATH,
                        '//*[(@id = "J_SearchForm")]//*[contains(concat( " ", @class, " " ), concat( " ", "icon-btn-search", " " ))]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '//*[contains(concat( " ", @class, " " ), concat( " ", "sort", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "link", " " ))]').click()
    time.sleep(5)

    get_info(driver.current_url, 1, 20)  # update max page