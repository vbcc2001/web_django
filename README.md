## 依赖
python 3.10.1
pip 21.3.1
virtualenv

## 安装部署
virtualenv D:\F07_Python\env\web_django
cd D:\F07_Python\env\web_django\Scripts\
.\activate
cd  D:\F02_SRC\web_django

python manage.py migrate

python manage.py collectstatic

py manage.py runserver


py -m pip install Django