import sys






# from pathos.multiprocessing import ProcessingPool as Pool
from multiprocessing import Pool

# import win32api,win32con

import json
import cv2
import png
import retinex
import os
from PIL import Image



# data_path = 'F:/test'
# img_list = os.listdir(data_path)
#
# with open('config.json', 'r') as f:
#     config = json.load(f)
#
# for img_name in img_list:
#     if img_name == '.gitkeep':
#         continue
#
#     img = cv2.imread(os.path.join(data_path, img_name),cv2.IMREAD_ANYDEPTH)
#     img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#
#     img_amsrcr = retinex.automatedMSRCR(
#         img,
#         config['sigma_list']
#     )
#
#     img_amsrcr = cv2.cvtColor(img_amsrcr, cv2.COLOR_RGB2GRAY)
#
#
#     with open('F:/test_enhance.png','wb') as f:
#         writer = png.Writer(width= img_amsrcr.shape[0], height= img_amsrcr.shape[1],bitdepth=16,greyscale=True)
#         img_amsrcr = img_amsrcr.tolist()
#         writer.write(f,img_amsrcr)

def process_save(filename):
    # path = 'F:/Data/data_rib_1024_ori/test1024/target/'
    # savepath = 'F:/enhance_test'
    path = './data/'
    savepath = './testdata/'
    with open('config.json', 'r') as f:
        config = json.load(f)
        # config = simplejson.load(f)
    # for file in filename:
    imgname = os.path.join(path,filename[0])
    # img = cv2.imread(imgname, cv2.IMREAD_ANYDEPTH) # 将图片灰度化
    img = cv2.imread(imgname)
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    img_amsrcr = retinex.automatedMSRCR(
        img,
        config['sigma_list']
    )
    # img_amsrcr = cv2.cvtColor(img_amsrcr, cv2.COLOR_RGB2GRAY)

    imgsavepath = os.path.join(savepath,filename[0])
    # with open(imgsavepath,'wb') as f:
        # writer = png.Writer(width= img_amsrcr.shape[1], height= img_amsrcr.shape[0],bitdepth=16,greyscale=True)
        # img_amsrcr = img_amsrcr.tolist()
        # writer.write(f,img_amsrcr)
    img_amsrcr = (img_amsrcr / 65535) * 255
    # img_amsrcr = img_amsrcr / 65535
    cv2.imwrite(imgsavepath,img_amsrcr)
    # cv2.imshow('test',img_amsrcr)
    # cv2.waitKey(0)

if __name__ == '__main__':
    path = './data/'
    # savepath = 'F:/enhancesave-307'
    #
    #filenames = os.listdir(path)
    # imgname = 'F:/X15219772.png'
    # imgsavepath = 'F:/test_enhance_withoutbone.png'
    # #
    # with open('config.json', 'r') as f:
    #     config = json.load(f)
    # img = cv2.imread(imgname, cv2.IMREAD_ANYDEPTH)
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # # img_amsrcr = retinex.MSRCR(
    # #     img,
    # #     config['sigma_list'],
    # #     config['G'],
    # #     config['b'],
    # #     config['alpha'],
    # #     config['beta'],
    # #     config['low_clip'],
    # #     config['high_clip']
    # # )
    # img_amsrcr = retinex.automatedMSRCR(
    #     img,
    #     config['sigma_list']
    #     #config['low_clip'],
    #     #config['high_clip']
    # )
    # img_amsrcr = cv2.cvtColor(img_amsrcr, cv2.COLOR_RGB2GRAY)
    # with open(imgsavepath, 'wb') as f:
    #     writer = png.Writer(width=img_amsrcr.shape[0], height=img_amsrcr.shape[1], bitdepth=16, greyscale=True)
    #     img_amsrcr = img_amsrcr.tolist()
    #     writer.write(f, img_amsrcr)
    # print('finished')
    # win32api.MessageBox(0,'finished','提示',win32con.MB_OK)


    filenames = os.listdir(path)
    # pool = Pool(6)

    process_save(filenames)
    # pool.map(process_save, filenames)
    # pool.close()
    # pool.join()
