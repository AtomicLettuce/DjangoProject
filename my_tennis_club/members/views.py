from django.http import HttpResponse
from django.template import loader
from .models import Member

def main(request):
  return HttpResponse(loader.get_template('main.html').render(request=request))

def members(request):
  mymembers= Member.objects.all().values()
  context = {'mymembers': mymembers,}
  template = loader.get_template('all_members.html')
  return HttpResponse(template.render(context, request))

def details (request, id):
  mymember  = Member.objects.get(id=id)
  template = loader.get_template('details.html')

  context={'mymember':mymember,}

  return HttpResponse(template.render(context, request))

def testing(request):
  mydata = Member.objects.values_list()
  template = loader.get_template('template.html')
  context = {
    'fruits': mydata,
  }
  return HttpResponse(template.render(context, request))