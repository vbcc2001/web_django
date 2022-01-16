## 依赖
python 3.10.1
pip 21.3.1
virtualenv

## 安装部署

```
virtualenv D:\F07_Python\env\web_django
cd D:\F07_Python\env\web_django\Scripts\
.\activate
cd  D:\F02_SRC\web_django
```
```
python -m pip install Django
# python -m install psycopg[binary,pool]  
python -m pip install psycopg2
python -m pip install whitenoise

python -m pip install Pillow
python -m pip install django-ckeditor
python -m pip install pyquery
python -m pip install docx2pdf
python -m pip install docxtpl

python -m pip install django-widget-tweaks


pip freeze > requirements.txt

python manage.py makemigrations 
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic

python manage.py runserver
```

