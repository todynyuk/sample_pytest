from selenium.webdriver.common.by import By
import time


def click_universal_category_link(driver, category):
    driver.find_element(By.XPATH, f"//a[@class='menu-categories__link' and contains(.,'{category}')]").click()
    time.sleep(3)


def set_search_input(driver, param):
    driver.find_element(By.XPATH, "//input[contains(@class, 'search-form__input')]").send_keys(param)


def click_search_button(driver):
    driver.find_element(By.XPATH, "//button[contains(@class, 'search-form__submit')]").click()


def get_goods_title_text(driver):
    buffer = driver.find_element(By.XPATH, "//span[@class='goods-tile__title']")
    goods_title_texts = []
    for elem in buffer:
        goods_title_texts.append(elem.text)
    return goods_title_texts


def verify_is_search_brand_present_in_goods_title(driver, brand):
    goods_title_texts = [x.lower() for x in get_goods_title_text(driver)]
    res = all([ele for ele in str(brand).lower() if (ele in goods_title_texts)])
    return res


def verify_wrong_search_request(driver):
    time.sleep(2)
    return driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").is_displayed()
