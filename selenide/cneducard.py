from selenium.webdriver import ActionChains

from selenide.dataconfig import *
from selenide.selenide import *
import selenide.csvop as CO
from selenium.common.exceptions import *

co = None
_WEB = WEB

_USER = USER

_WHERE = WHERE


# # 点到某个页面的过程
# def click_to(driver, where):
#     for xpath in where:
#         driver.find_element_by_xpath(xpath).click()
#     return driver


# #  登录过程  class_name 控制
# def _login(driver, username, password):
#     driver.find_element_by_class_name("header_btn").click()
#     driver.find_element_by_class_name('user').send_keys(username)
#     driver.find_element_by_class_name('pwd').send_keys(password)
#     driver.find_element_by_class_name('loginbtn').click()
#     return driver


# 配置并返回Driver
def config(browser, url_name, test_name, implicitly_wait=0.5):
    """
    只需要调用这个函数(前五个参数全为str，见dataconfig）
    :param url_name: url名称
    :param browser: 浏览器名称
    :param test_name: 测试项目名称
    :param implicitly_wait: 隐式等待时间
    :return: Driver类型
    """

    return exe_fig(exe_once_fig(open_web_driver(browser, url_name, implicitly_wait), test_name), co)


# 配置执行
def exe_fig(driver, co):
    # 获取头部信息
    elements_header = co.get_header()
    # 获取输入类型
    elements_type = co.get_elem_types()
    # 获取元素xpath
    elements_xpath = co.get_elem_xpath()
    # 获取延时
    elements_timeouts = co.get_elem_timeouts()
    # 获取测试用例
    test_case = co.get_data()
    # 输出以上数据
    print(elements_header)
    print(elements_type)
    print(elements_xpath)
    print(elements_timeouts)
    # 执行测试用例

    for csv_list_index in range(0, len(test_case)):
        if len(test_case[csv_list_index]) != 0:
            print('正在执行测试', test_case[csv_list_index])
            is_success = True

            for i in range(2, len(co.get_header())):
                try:
                    if not input_data(driver, elements_type[i], test_case[csv_list_index][i], elements_xpath[i],
                                      elements_timeouts[i]):
                        is_success = False
                        print('错误项', test_case[csv_list_index][i])
                except NoSuchElementException:
                    print("找不到元素", test_case[csv_list_index])
                # except WebDriverException:
                #     print("focus error", test_case[csv_list_index])
            # 写入测试结果
            if not is_success:
                test_case[csv_list_index][1] = 'NG'
            else:
                test_case[csv_list_index][1] = 'OK'
            # 刷新页面
            driver.refresh()
    # 保存结果
    co.save_csv_data(test_case)
    # driver.close()
    driver.quit()
    # 测试完成


def exe_once_fig(driver, name):
    # 读取测试用例用对象
    global co
    co = CO.CsvOp(name)
    # 获取头部信息
    elements_header = co.get_once_header()
    # 获取输入类型
    elements_type = co.get_once_elem_types()
    # 获取元素xpath
    elements_xpath = co.get_once_elem_xpath()
    # 获取延时
    elements_timeouts = co.get_once_elem_timeouts()
    # 获取测试用例
    test_case = co.get_once_data()
    # 输出以上数据
    print(elements_header)
    print(elements_type)
    print(elements_xpath)
    print(elements_timeouts)
    # 执行测试用例

    for csv_list_index in range(0, len(test_case)):
        print('正在执行一次性测试', test_case[csv_list_index])
        is_success = True
        for i in range(2, len(co.get_once_header())):
            if not input_data(driver, elements_type[i], test_case[csv_list_index][i], elements_xpath[i],
                              elements_timeouts[i]):
                is_success = False
                print('错误项', test_case[csv_list_index][i])
        # 写入测试结果
        if not is_success:
            test_case[csv_list_index][1] = 'NG'
        else:
            test_case[csv_list_index][1] = 'OK'
        # 刷新页面
        driver.refresh()
    # 保存结果
    co.save_csv_once_data(test_case)

    return driver
