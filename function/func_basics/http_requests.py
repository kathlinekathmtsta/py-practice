# 将下载安装好的第三方模块导入到当前文件
import requests


# 定义一个函数，让这个函数可以访问到网站并获取网站的页面数据

def get_info(url):
    # 获取网页内容
    response = requests.get(url)

    # 打印请求网站成功后返回的页面信息
    print(response.content.decode())


#   定义多个URL变量
url_1 = 'https://www.baidu.com/'
get_info(url_1)

url_2 = 'https://www.bing.com'
get_info(url_2)
