## 依赖
python 3.10.1
pip 21.3.1
virtualenv

## 开发配置

```
virtualenv D:\F07_Python\env\web_django
cd D:\F07_Python\env\web_django\Scripts\
.\activate
cd  D:\F02_SRC\web_django

# 导出 pip freeze > requirements.txt
pip install -r requirements.txt

python manage.py makemigrations  
python manage.py migrate  
python manage.py createsuperuser
python manage.py runserver

# 导出依赖
pip freeze > requirements.txt
```
## 安装依赖
```
python -m pip install Django
python -m pip install psycopg2
python -m pip install whitenoise

python -m pip install Pillow
python -m pip install django-ckeditor
python -m pip install django-widget-tweaks
python -m pip install pyquery
python -m pip install docx2pdf
python -m pip install docxtpl

# 图像处理（人脸识别用）
python -m pip install opencv-python
# 矩阵运算（人脸识别用）
python -m pip install numpy  
```

## 安装部署

### 通过 gunicorn 部署 

```
pip install gunicorn

pip install -r requirements.txt

python manage.py collectstatic
python manage.py makemigrations  
python manage.py migrate  
python manage.py createsuperuser

# 项目目录下运行  （-D 后台运行） 
gunicorn hengda.wsgi -D
# 安装Caddy2 进行代理，（安装Caddy2见官网）
# 配置/etc/caddy/Caddyfile文件：
www.3hhx.com {
    reverse_proxy 127.0.0.1:8000
}

```
### 通过 heroku 部署 
```
# 配置 runtime.txt
# 配置 Porcfile
```



