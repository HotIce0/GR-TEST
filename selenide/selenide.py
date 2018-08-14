"""

selenide Version 1.0
为贵阳紫光科技有限公司中国教育卡web应用测试用
注意：不适用于所有控件(当控件不可用键盘控制时)

"""

import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenide.dataconfig import WEB


def open_web_driver(browser, url_name, wait=0):
    return _Driver[browser](WEB[url_name], wait)


# 使用谷歌浏览器打开
def open_web_by_chrome(url, wait=0):
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get(url)
    chrome_driver.implicitly_wait(wait)
    return chrome_driver


# 其他浏览器
'''
等新电脑来了再写。。。。


'''

_Driver = {
    'chrome': open_web_by_chrome,
}


# 提示信息是否匹配
def error_tip_message_match(driver, message, xpath, timeout=0.1):
    try:
        wait = WebDriverWait(driver, timeout, poll_frequency=0.1)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        if driver.find_element_by_xpath(xpath).text == message:
            return True
        else:
            return False
    except TimeoutException:
        print("所匹配元素未找到")
        return False


# 跳页
def jump_page(driver, page, xpath, timeout=''):
    elem = driver.find_element_by_xpath(xpath)
    elem.send_keys(page)
    elem.send_keys(Keys.ENTER)
    return True


# 填写input类型
def write_input(driver, content, xpath, timeout=''):
    driver.find_element_by_xpath(xpath).clear()
    driver.find_element_by_xpath(xpath).send_keys(content)
    return True


# 填写选择时间
def write_time(driver, date, xpath, timeout=''):
    driver.find_element_by_xpath(xpath).clear()
    driver.find_element_by_xpath(xpath).send_keys(date)
    driver.find_element_by_xpath(xpath).send_keys(Keys.ENTER)
    return True
    # """
    # 日期格式: 2018-7-26
    # """
    # if date == '':
    #     return True
    # ele = driver.find_element_by_xpath(xpath)
    # ele.click()
    # try:
    #     date = datetime.datetime.strptime(date, '%Y-%m-%d')
    # except ValueError:
    #     print('日期格式错误')
    # date_today = datetime.datetime.strptime(str(datetime.date.today()), '%Y-%m-%d')
    # i_offset = int(str(date - date_today).replace('0:00:00', '0')[0:2])
    # if i_offset == 0:
    #     ele.send_keys(Keys.LEFT)
    #     ele.send_keys(Keys.RIGHT)
    # elif i_offset < 0:
    #     i_offset = -i_offset
    #     for i in range(0, i_offset):
    #         ele.send_keys(Keys.LEFT)
    # elif i_offset > 0:
    #     for j in range(0, i_offset):
    #         ele.send_keys(Keys.RIGHT)
    # ele.send_keys(Keys.ENTER)
    # return True


# 选择下拉列表
def choice_dropdown(driver, offset, xpath, timeout=''):
    sleep(1)
    elem = driver.find_element_by_xpath(xpath)
    elem.click()
    ac1 = ActionChains(driver)
    ac2 = ActionChains(driver)
    ac3 = ActionChains(driver)
    if offset == '':
        offset = '0'
    for i in range(0, int(offset)):
        ac1.send_keys(Keys.DOWN)
        # elem.send_keys(Keys.DOWN)
    ac1.send_keys(Keys.ENTER).perform()
    # elem.send_keys(Keys.ENTER)
    #  b sleep(3)
    ac3.send_keys(Keys.ESCAPE).perform()
    # elem.send_keys(Keys.ESCAPE)
    return True


# 单选框
def choice_radiogroup(driver, offset, xpath, timeout=''):
    radios = driver.find_element_by_xpath(xpath)
    radios_real = radios.find_elements_by_xpath('./label')
    radios_real[int(offset) - 1].click()
    return True


# 点击按钮
def click_button_long(driver, data, xpath, timeout=0.1):
    try:
        wait = WebDriverWait(driver, timeout, poll_frequency=0.1)
        print('开始等待')
        driver.find_element_by_xpath(xpath)
        driver.refresh()
        driver.find_element_by_xpath(xpath).click()
        return True
    except TimeoutException:
        return False


def click_button(driver, data, xpath, timeout=0.1):
    wait = WebDriverWait(driver, timeout, poll_frequency=0.1)
    wait.until(EC.visibility_of_any_elements_located((By.XPATH, xpath)))
    driver.find_element_by_xpath(xpath).click()
    return True


# 判断元素，是否从可见到可见
def elem_is_visible_true_true(driver, xpath, timeout=0.1):
    try:
        sleep(3)
        wait = WebDriverWait(driver, timeout=timeout, poll_frequency=0.1)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return True
    except TimeoutException:
        return False


# 判断元素，是否从可见到不可见
def elem_is_visible_true_false(driver, xpath, timeout=0.5):
    try:
        wait = WebDriverWait(driver, timeout, poll_frequency=0.1)
        sleep(1)
        wait.until(EC.invisibility_of_element_located((By.XPATH, xpath)))
        return True
    except TimeoutException:
        return False


# 判断元素，是否从不可见到不可见
def elem_is_visible_false_false(driver, xpath, timeout=0.5):
    try:
        sleep(1)
        wait = WebDriverWait(driver, timeout, poll_frequency=0.1)
        wait.until(EC.visibility_of_any_elements_located((By.XPATH, xpath)))
        return False
    except TimeoutException:
        return True


# 判断元素，是否从不可见到可见
def elem_is_visible_false_true(driver, xpath, timeout=0.5):
    try:
        sleep(1)
        wait = WebDriverWait(driver, timeout, poll_frequency=0.1)
        wait.until(EC.visibility_of_any_elements_located((By.XPATH, xpath)))
        return True
    except TimeoutException:
        return False


# still exist
def find_elem_true_true(driver, xpath, time_out=0.5):
    try:
        sleep(1)
        wait = WebDriverWait(driver, time_out, poll_frequency=0.1)
        wait.until_not(EC.presence_of_element_located((By.XPATH, xpath)))
        return False
    except TimeoutException:
        return True


# exist to miss
def find_elem_true_false(driver, xpath, time_out=0.1):
    try:
        sleep(1)
        wait = WebDriverWait(driver, time_out, poll_frequency=0.1)
        wait.until_not(EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    except TimeoutException:
        return False


# still miss
def find_elem_false_false(driver, xpath, time_out=0.1):
    try:
        sleep(1)
        wait = WebDriverWait(driver, time_out, poll_frequency=0.1)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return False
    except TimeoutException:
        return True


# miss to exist
def find_elem_false_true(driver, xpath, time_out=0.1):
    try:
        sleep(1)
        wait = WebDriverWait(driver, time_out, poll_frequency=0.1)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    except TimeoutException:
        return False


# 测试填写数据
def input_data(driver, ele_type, data, xpath, timeout=''):
    if not timeout == '':
        timeout = float(timeout)
    if data == '#None':
        return True
    return _OP[ele_type](driver, data, xpath, timeout)


"""字典，用于直接调用函数"""
# 存在测试
_EXIST = {
    'true_true': find_elem_true_true,
    'false_false': find_elem_false_false,
    'false_true': find_elem_false_true,
    'true_false': find_elem_true_false,
}
# 可见测试
_VISIBLE = {
    'true_true': elem_is_visible_true_true,
    'false_false': elem_is_visible_false_false,
    'false_true': elem_is_visible_false_true,
    'true_false': elem_is_visible_true_false,
}


# 基本操作
def _input_is_exist(driver, data, xpath, timeout):
    return _EXIST[data](driver, xpath, timeout)


def _input_is_visible(driver, data, xpath, timeout):
    return _VISIBLE[data](driver, xpath, timeout)


_OP = {'input': write_input,
       'time_selector': write_time,
       'dropdown': choice_dropdown,
       'radiogroup': choice_radiogroup,
       'button': click_button,
       'page': jump_page,
       'exist': _input_is_exist,
       'visible': _input_is_visible,
       'message': error_tip_message_match,
       'lbutton': click_button_long,
       }
