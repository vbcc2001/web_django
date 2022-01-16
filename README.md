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

pip install virtualenv  
virtualenv ~/env/web_django 
source ~/env/web_django/bin/activate  

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
# 生产部署依赖
python -m pip install gunicorn
# 核心框架
python -m pip install Django
# 数据库依赖 ( psycopg[binary,pool] 不兼容Django4.0)
# python -m pip install psycopg2
python -m pip install psycopg2-binary
# 静态文件服务
python -m pip install whitenoise
# 图像处理
python -m pip install Pillow
# 富文本编辑器
python -m pip install django-ckeditor
# 表单定制化渲染
python -m pip install django-widget-tweaks
# 网页解析库
python -m pip install pyquery
# word转pdf (应聘用)
python -m pip install docx2pdf
# word文档处理 (应聘用)
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



