from django.shortcuts import render, render_to_response
from django import  forms
from django.http import  HttpResponse
from .models import NormalUser

# Create your views here.
class NormalUserForm(forms.Form):
    #form的定义和model类的定义很像
    username=forms.CharField()
    headImg=forms.FileField()
#在View中使用已定义的Form方法
def registerNormalUser(request):
    #刚显示时调用GET方法
    if request.method=="POST":
        uf = NormalUserForm(request.POST,request.FILES)#刚显示时，实例化表单（是否有数据）
        if uf.is_valid():#验证数据是否合法，当合法时可以使用cleaned_data属性。
            #用来得到经过'clean'格式化的数据，会所提交过来的数据转化成合适的Python的类型。
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            #write in database
            normalUser=NormalUser()#实例化NormalUser对象
            normalUser.username = username
            normalUser.headImg = headImg
            normalUser.save()#保存到数据库表中
            return HttpResponse('Upload Succeed!')#重定向显示内容（跳转后内容）
    else:
        uf=NormalUserForm()#刚显示时，实例化空表单
    return render(request,'Upload/register.html',{'uf':uf})#只有刚显示时才起作用