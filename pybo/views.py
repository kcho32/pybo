from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. -> input validate, model call, context에 data저장, UI select
def index(request):
    return HttpResponse('안녕하세요, pybo에 오신걸 환영합니다.')

