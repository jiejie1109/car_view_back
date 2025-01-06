import jieba
from matplotlib import pylab as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from pymysql import *
import json


def get_img(field, targetImageSrc, resImageSrc):
    # 链接数据
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='cardata', charset='utf8')
    cusor = conn.cursor()
    sql = f"select {field} from carinfo"
    cusor.execute(sql)
    data = cusor.fetchall()

    # 传入数据
    text = ""
    for i in data:
        if i[0] != '':
            tagArr = i
            for j in tagArr:
                text += j

    cusor.close()
    conn.close()
    data_cut = jieba.cut(text, cut_all=False)
    string = " ".join(data_cut)

    # 根据词组描绘图片
    img = Image.open(targetImageSrc)
    img_arr = np.array(img)
    wd = WordCloud(
        font_path='STHUPO.TTF',
        mask=img_arr,
        background_color='#04122c'

    )
    wd.generate_from_text(string)
    # 绘制图片
    fig = plt.figure(1)
    plt.imshow(wd)
    plt.axis('off')

    plt.savefig(resImageSrc, dpi=800, bbox_inches='tight', pad_inches=0.1)


get_img('manufacturer', 'image/car.jpg', 'image/car_cloud.png')
