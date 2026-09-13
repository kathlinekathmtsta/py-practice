# 1. 定义三种不同的业务动作（注它们都接收一个data参数，方便统一调度）

def get_url(data):
    print(f"[1. 获取数据] 正在请求 URL: {data}")


def parse_html(data):
    print(f"[2. 解析数据] 正在解析 HTML: {data}")


def save_to_db(data):
    print(f"[3. 保存数据] 正在将 {data} 的结果写入数据库")


# 2. 准备数据源
url_1 = 'https://www.baidu.com/'
url_2 = 'https://www.google.com/'
url_3 = 'https://www.bing.com/'

url_list = [url_1, url_2, url_3]
# 数据池：url_list

# 3. 核心：将不同的函数引用保存在列表中，形成一个 流水线

pipeline = [get_url, parse_html, save_to_db]
# 动作池：pipeline

# 4. 业务调度：针对每一个 URL，依次执行流水线中的每一个动作
for url in url_list:
    print(f"\n====== 开始处理任务: {url} ======")
    for func in pipeline:
        func(url)   # 加括号，真正调用函数
