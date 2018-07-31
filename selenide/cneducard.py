from selenide.dataconfig import *
from selenide.selenide import *
import selenide.csvop as CO

_WEB = WEB

_USER = USER

_WHERE = WHERE


# 点到某个页面的过程
def click_to(driver, where):
    for xpath in where:
        driver.find_element_by_xpath(xpath).click()
    return driver


#  登录过程  class_name 控制
def _login(driver, username, password):
    driver.find_element_by_class_name("header_btn").click()
    driver.find_element_by_class_name('user').send_keys(username)
    driver.find_element_by_class_name('pwd').send_keys(password)
    driver.find_element_by_class_name('loginbtn').click()
    return driver


# 配置并返回Driver
def config(browser, url, user, where, test_name, implicitly_wait=0.5):
    """
    只需要调用这个函数(前五个参数全为str，见dataconfig）
    :param browser: 浏览器名称
    :param url: 网站名称
    :param user: 身份
    :param where: 到哪里
    :param test_name: 测试项目名称
    :param implicitly_wait: 隐式等待时间
    :return: Driver类型
    """
    return exe_fig(click_to
                   (_login(open_web_driver
                           (browser, url=_WEB[url], wait=implicitly_wait), _USER[user][0], _USER[user][1]),
                    WHERE[where]),
                   test_name)


# 配置执行
def exe_fig(driver, name):
    # 读取测试用例用对象
    co = CO.CsvOp(name)
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
        print('正在执行测试', test_case[csv_list_index])
        is_success = True
        for i in range(2, len(co.get_header())):
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
    co.save_csv_data(test_case)
    # driver.close()
    driver.quit()
    # 测试完成
