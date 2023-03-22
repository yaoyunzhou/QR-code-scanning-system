from pyzbar.pyzbar import decode
from PIL import Image
import csv
# import pandas as pd
import os

# 加载图像
image = Image.open("test.png")
# 解码二维码
data = decode(image)
# 打印二维码中包含的数据
# link = []
dataofurl = data[0].data.decode()
# dataofurl = dataofurl.split("//")
# dataofur1 = dataofurl[0] 
# dataofur2 = dataofurl[1].split('/')[0]
# dataofur3 = dataofurl[1].split('/')[1]
# linkt = dataofur1 + str("//") + dataofur2 + str("/") + dataofur3
#! debug
# print(linkt)
# URL = pd.read_csv('ML/url_t.csv',encoding="utf-8")
# print(URL)
# URL['url'] = dataofurl


# 打开CSV文件以写入模式
with open('ML/url_t.csv', mode='w') as csv_file:
    # 创建CSV写入器
    writer = csv.writer(csv_file)

    # 写入表头
    writer.writerow(['url'])

    # 写入链接
    writer.writerow([dataofurl])