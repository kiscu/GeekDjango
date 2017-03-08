from django.shortcuts import render
from django.http import HttpResponse, Http404

def hello(request):
	return HttpResponse("hello world")


def hello1(request, num):
	try:
		num = int(num)
	except ValueError:
		raise Http404()