# import base64
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import numpy as np  # 矩阵运算
# import cv2  # opencv包

# # 生成人脸检测器

# face_detector = cv2.CascadeClassifier('zxkj/f08_service/haarcascade_frontalface_default.xml') 

# @csrf_exempt  # 用于规避跨站点请求攻击
# def face_detect(request):
#     # 规定用户用POST的请求上传检测的图片
#     if request.method == "POST":
#         # 请求中包含图像则以流方式读取图像
#         if request.FILES.get("image", None) is not None:
#             image = read_image(stream=request.FILES["image"])
#         else:
#             return JsonResponse({'#face_num': -1, })
#         # 将彩色图片转为灰度,cv2检测的时候是以灰度图片检测的
#         if image.shape[2] == 3:
#             imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色图像转灰度图像
#         else:
#             imgGray = image
#         # 进行人脸检测
#         values = face_detector.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
#         # 将检测得到的人脸检测关键点封装成坐标
#         values = [(int(a), int(b), int(a + c), int(b + d)) for (a, b, c, d) in values]
#         # result={
#         #     '#face_mum': len(values),
#         #     "faces": values,
#         # }
#         # 将检测框显示在原图上
#         for (w, x, y, z) in values:
#             cv2.rectangle(image, (w, x), (y, z), (0, 255, 0), 2)

#         retval, buffer_img = cv2.imencode('.jpg', image)  # 在内存中编码为jpg格式
#         img64 = base64.b64encode(buffer_img)  # base64编码用于网络传输
#         img64 = str(img64, encoding='utf-8')  # bytes转换为str类型
#         result = {"img64":img64}  # json封装
#         return JsonResponse(result)

# def read_image(stream=None):
#     """以流的形似读取图片"""
#     if stream is not None:
#         data_temp = stream.read()
#     image = np.asanyarray(bytearray(data_temp), dtype="uint8")
#     image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#     return image