from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request,"survey_app/index.html")
def result(request):
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	print request.session
	return render(request, "survey_app/survey.html")


