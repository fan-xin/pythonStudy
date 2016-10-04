from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
class Person(object):
    def __init__(self, name, age, sex):
        self.name=name
        self.age=age
        self.sex=sex

    def say(self):
        return "I am "+ self.name

def index(req,id):
    user = {'name':'tom', 'age':23, 'sex':'male'}
    book_list = ['python','java','php','web']
    #return HttpResponse('<h1>Hello fanxin! welcome</h1>')
    return render_to_response('index.html',{'title':'my page','book_list':book_list,'user':user,'id':id})
