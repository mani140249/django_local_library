from django.shortcuts import render, redirect

from .models import Notice

# def noticeList(request):
# 	qs = Notice.objects.all().order_by('-date_created')[:5]
# 	return render(request, 'index.html', {'qs':qs})

def noticeDetail(request,id):
	print("========>",id)
	print("------------------->", request.GET.get('id'))
	# updateObject = Notice.objects.get(pk=pk)
	# print(updateObject)
	return render(request, 'index.html')
