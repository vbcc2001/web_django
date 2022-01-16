# import base64
# import os

# from django.core.paginator import Paginator
# from django.http import StreamingHttpResponse, JsonResponse
# from django.shortcuts import render, get_object_or_404
# # Create your views here.
# from django.utils.encoding import escape_uri_path

from django.views.decorators.csrf import csrf_exempt

import numpy as np  # 矩阵运算
import cv2  # opencv包

# 生成人脸检测器
face_detector = cv2.CascadeClassifier('.\\haarcascade_frontalface_default.xml') 

@csrf_exempt  # 用于规避跨站点请求攻击
def face_detect(request):
    result = {}
    # 规定用户用POST的请求上传检测的图片
    if request.method == "POST":
        # 请求中包含图像则以流方式读取图像
        if request.FILES.get("image", None) is not None:
            image = read_image(stream=request.FILES["image"])
        else:
            result.updata({'#face_num': -1, })
            return JsonResponse(result)
        # cv2检测的时候是以灰度图片检测的
        # 将彩色图片转为灰度
        if image.shape[2] == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 进行人脸检测
        values = face_detector.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
        # 将检测得到的人脸检测关键点封装成坐标
        values = [(int(a), int(b), int(a + c), int(b + d)) for (a, b, c, d) in values]
        result.update({
            '#face_mum': len(values),
            "faces": values,
        })
        return JsonResponse(result)

def read_image(stream=None):
    """以流的形似读取图片"""
    if stream is not None:
        data_temp = stream.read()
    image = np.asanyarray(bytearray(data_temp), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


@csrf_exempt
def facedetectDemo(request):
    result = {}

    if request.method == "POST":
        if request.FILES.get('image') is not None:
            img = read_image(stream=request.FILES["image"])
        else:
            result.update({
                "#faceNum": -1,
            })
            return JsonResponse(result)

        if img.shape[2] == 3:
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色图像转灰度图像
        else:
            imgGray = img


        # 进行人脸检测
        values = face_detector.detectMultiScale(imgGray,
                                           scaleFactor=1.1,
                                           minNeighbors=5,
                                           minSize=(30, 30),
                                           flags=cv2.CASCADE_SCALE_IMAGE)
        # 将检测得到的人脸检测关键点坐标封装
        values = [(int(a), int(b), int(a + c), int(b + d))
                  for (a, b, c, d) in values]

        # 将检测框显示在原图上
        for (w, x, y, z) in values:
            cv2.rectangle(img, (w, x), (y, z), (0, 255, 0), 2)

        retval, buffer_img = cv2.imencode('.jpg', img)  # 在内存中编码为jpg格式
        img64 = base64.b64encode(buffer_img)  # base64编码用于网络传输
        img64 = str(img64, encoding='utf-8')  # bytes转换为str类型
        result["img64"] = img64  # json封装
    return JsonResponse(result)


def read_file(file_name, size):
    """分批读取文件"""
    with open(file_name, mode='rb') as fp:
        while True:
            c = fp.read(size)
            if c:
                yield c  # 生成器，相当于一个特殊的迭代器，当运行到这个语句的时候会保存当前的对象；下次再运行到这里的时候会接着上次的对象继续运行。
            else:
                break

