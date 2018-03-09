###赵巍博客
Django搭建博客
使用Django快速搭建博客

要求

Python: 2.X

Django: 1.10.x

Mysql

示例博客：http://python.fendous.cn/blog
特点
博客文章 markdown 渲染，代码高亮
三方社会化评论系统支持(畅言)
三种皮肤自由切换
阅读排行榜/最新评论
多目标源博文分享
博文归档
友情链接

安装
pip install -r requirements.txt  #安装所有依赖
setting.py配置自己的数据库
python manage.py makemigrations blog
python manage.py migrate
python manage.py runserver
浏览器中打开http://127.0.0.1:8000/即可访问
