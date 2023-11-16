from django.shortcuts import render

# Create your views here.
def datarender(request):
  data='this data is our assumption'
  d={'assumption':data}
  return render(request,'datarender.html',context=d)

def login(request):
  d={'username':'harika','age':21}
  return render(request,'login.html',context=d)
  