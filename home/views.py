from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from home.models import Battery

# Create your views here.
def index(request):
	if request.method == "POST" and request.is_ajax():
		code = request.POST['code']
		priority = request.POST['priority']
		new_lower_limit = request.POST['lower_limit']
		new_upper_limit = request.POST['upper_limit']
		changes = Battery.objects.filter(code = code,priority = priority).update(lower_limit = new_lower_limit,upper_limit = new_upper_limit)
		print(changes)
		return JsonResponse({'changes_made': changes})
	elif request.method == "GET" and request.is_ajax():
		context = {}
		context['all'] = Battery.objects.all()
		return render(request,'index.html',context)
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