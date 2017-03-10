from django.shortcuts import render,render_to_response
from django.http import HttpResponse, Http404

def hello(request):
	return HttpResponse("hello world")


def hello1(request, num):
	try:
		num = int(num)
	except ValueError:
		raise Http404()


def views(request):
	return render_to_response('3.html', {})