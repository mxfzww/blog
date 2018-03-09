# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from blog_model.models import Article as Articles,Comment
from django.views.decorators import csrf
#首页
def Index(request):
    article_list = Articles.objects.filter(category_id=1).all()[0:5]
    article_list_tj = aritcle_list_tj()
    aritcle_list_view = article_list_view()
    return render(request,"index.html",{"article_list":article_list,"article_list_tj":article_list_tj,"aritcle_list_view":aritcle_list_view})

#关于
def About(request):
    return render(request,"about.html")

#碎言碎语
def Mood(request):
    article_sort2 = Articles.objects.filter(category_id=2).all()
    return render_to_response("mood.html",locals())

#学无止境
def Article(request):

    article_list_tj = aritcle_list_tj()

    article_sort2 = Articles.objects.filter(category_id=3).all()[0:5]

    return render(request,"article.html", {"article_sort2":article_sort2,"article_list_tj":article_list_tj})

#留言板
def Board(request):

    if request.method == "POST":
        Comment.objects.create(comment=request.POST.get("comment"),user_name="root",source_id=0)

    Commentdata = Comment.objects.all().filter(source_id=0).order_by("-create_time")[0:5]
    return render(request, "board.html",{"Commentdata":Commentdata})
    #return render_to_response("board.html",locals())

#详情页
def Article_detail(request,pk):

    if request.method == "POST":
        Comment.objects.create(comment=request.POST.get("comment"),user_name="root",source_id=request.POST.get("id"))

    #文章信息
    article_one = Articles.objects.get(id=pk)
    #评论信息

    article_one.viewed()

    commonts = Comment.objects.all().filter(source_id=pk).order_by("-create_time")[0:5]

    article_list_tj = aritcle_list_tj()

    #return render("article_detail.htm", {"article_one": article_one})
    return render(request,"article_detail.html", {"article_one": article_one,"commonts":commonts,"article_list_tj":article_list_tj})

#推荐
def aritcle_list_tj():
    article_list_tjs = Articles.objects.filter(tj=1).all()[0:5]
    return article_list_tjs

#点击量
def article_list_view():
    article_list_view = Articles.objects.order_by("-date_time").all()[0:5]
    return article_list_view