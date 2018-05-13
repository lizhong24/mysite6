#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms


class UserForm(forms.Form):
    username = forms.CharField()

# 用户登录
def login(req):
    if req.method == "POST":
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            # 把获取表单的用户名传递给session对象
            req.session['username'] = username
            return HttpResponseRedirect('/index/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})

# 登录之后跳转页
def index(req):
    username = req.session.get('username','anybody')
    return render_to_response('index.html',{'username':username})

# 注销动作
def logout(req):
    del req.session['username']  # 删除session
    return HttpResponse('logout ok!')
