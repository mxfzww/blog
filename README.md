###赵巍博客
Django搭建博客
使用Django快速搭建博客

要求

Python: 2.X

Django: 1.10.x

Mysql

示例博客：http://python.fendous.cn/blog

特点

两种皮肤自由切换

阅读排行榜/最新评论

多目标源博文分享

博文归档

友情链接

留言板

安装

setting.py配置自己的数据库

python manage.py makemigrations blog

python manage.py migrate

python manage.py runserver

浏览器中打开http://127.0.0.1:8000/即可访问
