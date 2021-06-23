from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from home.models import Person,Battery
from home.forms import NameForm

# Create your views here.
def index(request):
	if request.method == "POST" and request.is_ajax():
		code = request.POST['code']
		new_lower_limit = request.POST['lower_limit']
		new_upper_limit = request.POST['upper_limit']
		new_priority = request.POST['priority']
		battery = Battery.objects.get(code = code)
		battery.lower_limit = new_lower_limit
		battery.upper_limit = new_upper_limit
		battery.priority = new_priority
		battery.save()
		''' Check check'''
		print(battery)
		response_data = {}
		response_data['code'] = code
		print(response_data)
		return JsonResponse(response_data)
	elif request.method == "GET" and request.is_ajax():
		context = {}
		context['all'] = Battery.objects.all()
		return render(request,'table_view.html',context)
	else:
		print("Refreshing ...")
		context = {}
		context['all'] = Battery.objects.all()
		return render(request,'index.html',context)

# def form_view(request):
# 	form = NameForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = NameForm()
# 		return HttpResponseRedirect('/')	
# 	context = {'form': form}
# 	print("Hello",form)
# 	return render(request,'index.html',context)


# def form_view(request):
# 	form = NameForm()
# 	if request.method == 'POST' and request.is_ajax():
# 		form = NameForm(request.POST)
# 		print("Hi1",form['fname'])
# 		if form.is_valid():
# 			form.save()	
# 	context = {'form': form}
# 	print("Hello",form)
# 	return render(request,'index.html',context)