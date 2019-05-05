
import json
import cv2
import retinex
import os


def process_save(filename):
    # path = 'F:/Data/data_rib_1024_ori/test1024/target/'
    # savepath = 'F:/enhance_test'
    path = './data/'
    savepath = './testdata/'
    with open('config.json', 'r') as f:
        config = json.load(f)
    imgname = os.path.join(path,filename)
    img = cv2.imread(imgname)
    # img = cv2.imread(imgname, cv2.IMREAD_ANYDEPTH) # 将图片灰度化
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    img_amsrcr = retinex.automatedMSRCR(
        img,
        config['sigma_list']
    )
    # img_amsrcr = cv2.cvtColor(img_amsrcr, cv2.COLOR_RGB2GRAY)

    imgsavepath = os.path.join(savepath,filename)
    # with open(imgsavepath,'wb') as f:
        # writer = png.Writer(width= img_amsrcr.shape[1], height= img_amsrcr.shape[0],bitdepth=16,greyscale=True)
        # img_amsrcr = img_amsrcr.tolist()
        # writer.write(f,img_amsrcr)
    img_amsrcr = (img_amsrcr / 65535) * 255
    cv2.imwrite(imgsavepath,img_amsrcr)
    # cv2.imshow('test',img_amsrcr)
    # cv2.waitKey(0)

if __name__ == '__main__':
    path = './data/'
    filenames = os.listdir(path)
    for filename in filenames:
        process_save(filename)

