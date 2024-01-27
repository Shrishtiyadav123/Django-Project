from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from.models import Member
from .forms import MemberForm

# Create your views here.
def email(request):
    mymember = Member.objects.all().values()
    context ={
        'mymember':mymember
    }
    template=loader.get_template('email.html')
    return HttpResponse(template.render(context,request))

def intro(request):
    mymember = Member.objects.all().values()
    context = {
        'mymember': mymember
    }
    template=loader.get_template('intro.html')
    return HttpResponse(template.render(context,request))

def contacts(request):
    member_list = Member.objects.all().all()
    context= {
        'member_list': member_list
    }
    template=loader.get_template('contacts.html')
    return HttpResponse(template.render(context,request))


def detail(request,id):
    mymember = Member.objects.get(id=id)
    template=loader.get_template('detail.html')
    context= {
        'mymember':mymember
    }
    
    return HttpResponse(template.render(context,request))
def all_member(request):
    member_list = Member.objects.all().values()
    context = {
        'member_list': member_list
    }
    template=loader.get_template('all_member.html')
    return HttpResponse(template.render(context,request))

def sample1(request):
    mymember = Member.objects.all().values()
    context ={

    }
    template=loader.get_template('sample1.html')
    return HttpResponse(template.render(context,request))

@csrf_exempt
def add_newmember(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname',)
        lastname = request.POST.get('lastname',)
        rollno = request.POST.get('rollno',)
        phoneno = request.POST.get('phoneno',)
        image = request.FILES['image']
        member= Member(firstname=firstname,lastname=lastname,rollno=rollno,phoneno=phoneno,image=image)
        member.save()
    template=loader.get_template('add_newmember.html')
    return HttpResponse(template.render())

def update(request,id):
    member=Member.objects.get(id=id)
    form = MemberForm(request.POST,instance=member)
    if form.is_valid():
        form.save()
        template = loader.get_template('add_newmember.html')
        return HttpResponse(template.render())
    return render(request,'update.html',{'form':form,'member':member})

@csrf_exempt
def delete(request,id):
    if request.method == 'POST':
        member =  Member.objects.get(id=id)
        member.delete()
        template = loader.get_template('all_member.html')
        return HttpResponse(template.render())
    return render(request,'delete.html')
 