from myLesson.models import *
from myLesson.forms import *

from django.shortcuts import render,render_to_response
from django.http import HttpResponse, Http404

def hello(request):
	if request.method == 'POST':
		form = Mybook(request.POST)
		if form.is_valid():
			data  = form.cleaned_data
			title = data["title"]
			return HttpResponse(title)

	form = Mybook()
	return render_to_response('4.html',{
		'form':form
		})


def hello1(request, num):
	try:
		num = int(num)
	except ValueError:
		raise Http404()


def views(request):
	return render_to_response('3.html', {})