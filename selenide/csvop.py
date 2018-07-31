import csv


class CsvOp(object):
    """
    csv操作类

    """

    def __init__(self, test_name):
        """
        初始化CSV操作了 读取csv文件
        命名规则 ： 类型文件： 'test'+'_head.csv'
                   数据文件： 'test'+'_data.csv'

        :param test_name:
        """
        self._test_name = str(test_name)

        # 获取名称
        self._head_name = self._test_name + '_head.csv'
        self._data_name = self._test_name + '_data.csv'
        # try:
        #     f = open(self._head_name, 'r', encoding='utf-8')
        #     print('ok')
        #     f.close()
        # except:
        #     print('encode error')
        # 读取utf-16类型
        with open(self._head_name, 'r', encoding='utf-8') as f:
            self._head = list(csv.reader(f))
        # 读取测试数据
        with open(self._data_name, 'r', encoding='utf-8') as f:
            self._data = list(csv.reader(f))

    # 设置csv 文件类型
    def set_head(self, head):
        self._head = head

    def set_data(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def save_csv_head(self, head):
        """
        头部文件保存
        """
        self.set_data(head)
        # 保存头
        with open(self._data_name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(self._head)

    def save_csv_data(self, data):
        """
        数据保存
        """
        self.set_data(data)
        # 保存数据
        with open(self._data_name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(self._data)

    # 获取测试项名称
    def get_header(self):
        return self._head[0]

    # 获取测试项类型
    def get_elem_types(self):
        return self._head[1]

    # 获取测试项XPATH
    def get_elem_xpath(self):
        return self._head[2]

    # 获取测试项延迟
    def get_elem_timeouts(self):
        return self._head[3]
