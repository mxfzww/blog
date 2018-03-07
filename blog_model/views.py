# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.

#首页
def Index(request):
    return render(request,"index.html")

#关于
def About(request):
    return render(request,"about.html")

#碎言碎语
def Mood(request):
    return render(request,"mood.html")

#学无止境
def Article(request):
    return render(request,"article.html")

#留言板
def Board(request):
    return render(request,"board.html")

#详情页
def Article_detail(request):
    return render(request,"article_detail.html")
