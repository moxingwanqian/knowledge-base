# coding=utf-8
# 导入库
import os
import time
import requests
from lxml import etree

# 定义请求头
headers = {
    'User-Agent': 'Chrome 10.0'
}

# 建立传入数据函数
def input_data():
    Html_Num = input('Enter the Html_Num:')
    Page_Num = input('Enter the Page_Num:')

# 创建网页列表函数
def url_list():
    url_home = 'http://www.tujigu.net/a/'
    url_header = url_home + str(Html_Num) + '/'
    urls.append(url_header)
    for a in range(2, int(Page_Num))
        url_other = url_header + str(a) + '.html'
        urls.append(url_other)

# 建立创建目标文件夹函数
def get_path_name(url_header):
    res = requests.get(url=url_header, headers=headers)
    tree = etree.HTML(res.text)
    img_alt = tree.xpath('//div[@class="content"]/img/@alt')[0]
    path_name = './' + str(img_alt)
    if not os.path.exista(path_name):
        os.mkdir(path_name)
    else:
        pass

# 建立图片下载函数
def get_img():
    for src in img_src_list:
        img_data = requests.get(url=src, headers=headers).content
        name = src.split('/')[-1]
        with open(path + name, 'wb') as f:
            print('Downloading Picture:{name}')
            f.write(img_data)
            f.close()
        time.sleep(0.5)
        
# 主程序入口
if __name__ == '__main__':
    # 创建图片和urls列表
    img_src_list = []
    urls = []
    # 运行函数
    input_data()
    url_list()
    get_path_name(urls[0])
    get_img()
    print('Finish!')
    
