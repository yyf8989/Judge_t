# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#python 从url上获取图片
import urllib
import pandas as pd
from tqdm import tqdm


def get_images_1(file_dir):
    df = pd.read_excel(file_dir)
    vio_images = df[df['vio_code'] == 1625]
    name_list = vio_images['name'].values.tolist()
    print('start get images from urls.')
    for name in tqdm(name_list):
        url1 = vio_images[vio_images['name'] == name]['url1']
        urllib.request.urlretrieve(str(url1), 'D:/贵阳出差_202001/智诚/traffic_judge/images/{}_1.jpg'.format(name))
        url2 = vio_images[vio_images['name'] == name]['url2']
        urllib.request.urlretrieve(str(url2), 'D:/贵阳出差_202001/智诚/traffic_judge/images/{}_2.jpg'.format(name))
        url3 = vio_images[vio_images['name'] == name]['url3']
        urllib.request.urlretrieve(str(url3), 'D:/贵阳出差_202001/智诚/traffic_judge/images/{}_3.jpg'.format(name))
    print('Images Download Done!')
    return 0


import requests
from PIL import Image
from io import BytesIO

def get_images_2(file_dir):
    df = pd.read_excel(file_dir)
    vio_images = df[df['vio_code'] == 1625]
    name_list = vio_images['name'].values.tolist()
    print('start get images from urls.')
    for name in tqdm(name_list):
        url1 = vio_images[vio_images['name'] == name]['url1']
        response = requests.get(url1)
        image = Image.open(BytesIO(response.content))
        image.save('D:/贵阳出差_202001/智诚/traffic_judge/images/{}_1.jpg'.format(name))

        url2 = vio_images[vio_images['name'] == name]['url2']
        response = requests.get(url2)
        image = Image.open(BytesIO(response.content))
        image.save('D:/贵阳出差_202001/智诚/traffic_judge/images/{}_2.jpg'.format(name))
        
        url3 = vio_images[vio_images['name'] == name]['url3']
        response = requests.get(url3)
        image = Image.open(BytesIO(response.content))
        image.save('D:/贵阳出差_202001/智诚/traffic_judge/images/{}_3.jpg'.format(name))
    print('Images Download Done!')
    return 0



if __name__ == '__main__':
    
    file_dir = 'D:/贵阳出差_202001/智诚/图片示例文档.xlsx'
    try:
        status = get_images_1(file_dir)
    except:
        status = get_images_2(file_dir)
        
#url = ''
#urllib.request.urlretrieve(url, 'D:/贵阳出差_202001/智诚/traffic_judge/images/{}_1.jpg'.format('a'))
#
#response = requests.get(url)
#print(response)
#image = Image.open(BytesIO(response.content))
#image.save('D:/贵阳出差_202001/智诚/traffic_judge/images/{}_2.jpg'.format('b'))
