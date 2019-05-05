"""
Author: Fangyu Zhou
Time:2019.4.30
"""
# 多线程实现Retinex算法调用
import sys
import json
import cv2
import retinex
import os
from multiprocessing import Pool

def getImagePath(input_path):
    filelist = []
    for root, dirs, files in list(os.walk(input_path)):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                filelist.append(root  + file)
    return filelist

# def saveImg(imglist,savepath):
#     for i in range(len(imgnamelist)):
#         savefilepath = savepath + imgnamelist[i]
#         cv2.imwrite(imglist[i],savefilepath)

def process_save(filepath):
    # filename = os.listdir(input_path_save_path[0])
    with open('config.json', 'r') as f:
        config = json.load(f)
    img = cv2.imread(filepath)
    # img = cv2.imread(imgpath, cv2.IMREAD_ANYDEPTH) # 读取任何深度的图片
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)   # 颜色空间有
    img_amsrcr = retinex.automatedMSRCR(
        img,
        config['sigma_list']
    )
    # img_amsrcr = cv2.cvtColor(img_amsrcr, cv2.COLOR_RGB2GRAY)
    img_amsrcr = (img_amsrcr / 65535) * 255
    fname = filepath.split('/')[-1]
    savepath = './testdata/'
    imgsavepath = savepath + fname
    # return img_amsrcr
    cv2.imwrite(imgsavepath,img_amsrcr)
    # cv2.imshow('test',img_amsrcr)
    # cv2.waitKey(0)

if __name__ == '__main__':
    input_path = './data/'
    save_path = './testdata/'
    print('load images...')
    filepath = getImagePath(input_path)
    print('load Success!')
    print('process images...')
    pool = Pool(6)
    pool.map(process_save,filepath)
    pool.close()
    pool.join()
    print('Success!')