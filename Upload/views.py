from django.shortcuts import render
from django.http import  HttpResponse
import os
from django.shortcuts import render_to_response

# Create your views here.
def upload(request):
    if request.method == "POST":
        handle_upload_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse('Successful')  # 此处简单返回一个成功的消息，在实际应用中可以返回到指定的页面中

    return render_to_response('Upload/upload.html')


def handle_upload_file(file, filename):
    path = r'F:\github\TianWen3.6\TianWen2\TianWen\dataprocessing'  # 上传文件的保存路径，可以自己指定任意的路径
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename, 'wb+')as destination:
        for chunk in file.chunks():
            destination.write(chunk)