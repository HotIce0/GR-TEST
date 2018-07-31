"""
可配置为文件读取
"""
BROWSER = ['chrome', ]
# 网页
WEB = {
    "首页": 'https://www.gzeducard.com',

}
# 使用角色的账号密码
USER = {
    "贵州省教育局": ("gzsjyj", "123456"),
    "贵阳一中": ("gyyz", "123456"),
}
# 点到哪里去的XPATH元组(功能)
WHERE = {
    "教育局-数据上报": (
        "/html/body/div[4]/div/a[4]",
        "/html/body/div[6]/div[2]/a[ 2]"
    ),
    "教育局-营养餐": (
        "/html/body/div[4]/div/a[4]",
        "/html/body/div[6]/div[2]/a[ 3]"
    ),
    "教育局-控辍保学": (
        "/html/body/div[4]/div/a[4]",
        "/html/body/div[6]/div[2]/a[ 1]"),
    "教育局-数据上报-新建报表": (
        "/html/body/div[4]/div/a[4]",
        "/html/body/div[6]/div[2]/a[ 2]",
        '//*[@id="app"]/div/div[1]/div[2]/div[2]/a')
}
