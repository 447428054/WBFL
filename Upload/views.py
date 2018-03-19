from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse
from .models import NormalUser
import docx
from . import models


# Create your views here.
class NormalUserForm(forms.Form):
# form的定义和model类的定义很像
    username=forms.CharField()
    headImg=forms.FileField()


#在View中使用已定义的Form方法
def registerNormalUser(request):
    #刚显示时调用GET方法
    if request.method=="POST":
        uf = NormalUserForm(request.POST,request.FILES)  #刚显示时，实例化表单（是否有数据）
        if uf.is_valid():  #验证数据是否合法，当合法时可以使用cleaned_data属性。
            #用来得到经过'clean'格式化的数据，将所提交过来的数据转化成合适的Python的类型。
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            #write in database
            normalUser=NormalUser()  #实例化NormalUser对象
            normalUser.username = username
            normalUser.headImg = headImg
            normalUser.save()#保存到数据库表中
            #headImg.name仅仅是文件的名字，不包含路径
            suffix = headImg.name[headImg.name.find('.'):len(headImg.name) + 1]   #获取文件后缀名
            path = "G:/" + headImg.name  #文件的路径，使用时按文件保存的位置进行修改
            if suffix == '.docx':
                read_doc(request,path)
            elif suffix == '.pdf':
                read_doc(headImg,path)
            elif suffix == '.doc':
                read_doc(headImg,path)
            return HttpResponse('Upload Succeed!')  #重定向显示内容（跳转后内容）
    else:
        uf=NormalUserForm()  #刚显示时，实例化空表单
    return render(request,'Upload/register.html',{'uf':uf})  #只有刚显示时才起作用

'''
前置条件：path是文件的绝对路径，path下的文件要保证存在并且是docx格式
后置条件：将path下的docx文件读取出来，并保存在‘G:/’下的txt文档中；文档如果不存在，服务器会停止响应，后期对这个异常进行
处理；后面预计会加上对doc文件的支持，可能是将doc文件转换为docx文件处理
'''
def read_doc(request,path):  #阅读docx文档,path为文件的路径
        store_path = 'G:/'  #txt文件保存的路径
        doc = docx.Document(path)  #根据路径打开一个docx对象
        file_name = path[path.rfind('/') + 1:path.find('.')]  #提取路径中的文件名,不包含后缀
        outfile = open(store_path + file_name + '_temp.txt','w')   #创建一个临时的txt文件
        for i in range(len(doc.paragraphs)):  #将docx文档里的数据写入txt文档中
            outfile.write(doc.paragraphs[i].text + '\n')
        outfile.close()  #结束写入