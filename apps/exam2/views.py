from __future__ import unicode_literals
from .models import User, Quote
import bcrypt
from django.core.urlresolvers import reverse
from django.contrib.messages import get_messages
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse

def index(request):

    return render (request, 'exam2/index.html')

def register(request):
    errors = User.objects.register_validate(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    hashed_password = bcrypt.hashpw((request.POST['password'].encode()), bcrypt.gensalt(10))
    User.objects.create(name=request.POST['name'], username=request.POST['username'],birthday=request.POST['bday'], email=request.POST['email'],password= hashed_password)
    user = User.objects.get(email=request.POST['email'])
    request.session['uid'] = user.id
    # user_id = User.objects.get(username=request.POST['username'])
    return redirect('/home')

# ===================== Login
def login(request):
    errors = User.objects.login_validate(request.POST)
    # checks username in models for existence
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    # user = User.objects.get(username = request.POST['username'])
    user = User.objects.get(email = request.POST['email'])
    # if  not user:
    #     messages.add_message(request, messages.INFO, "Usernmae doesn't exist! Please register")
    #     return redirect('/')
    # else:
        # user = User.objects.filter(username = request.POST['username'])
    if not (bcrypt.checkpw(request.POST['password'].encode(), user.password.encode())):
        # errors['password']="Incorrect password! Please try again"
        messages.add_message(request, messages.INFO, "Invalid password")
        return redirect('/')
    else:
        request.session['uid'] = user.id
        # request.session['uname'] = user.name
    return redirect("/home")


def home(request):
    # Quote.objects.get(id=1).remove()
    context={
    'user': User.objects.get(id=request.session['uid']),
    'mine': Quote.objects.filter(wished_by=request.session['uid']),
    'others': Quote.objects.exclude(wished_by=request.session['uid']),
    'users': User.objects.all(),
    'quotes':Quote.objects.all(),
    }
    return render(request, 'exam2/home.html', context )

def logoff(request):
    request.session['uid'] = ""
    return redirect('/')

def addQuote(request):
    print "inside addQuote", request.POST
    if request.method == 'POST':
        if len(request.POST['quoted_by'])<3:
            messages.error(request, 'At least 3 characters for the Quoted By!!!')
            return redirect('/home')
        elif len(str(request.POST['message'])) <10:
            messages.error(request, 'Message needs to be at least 10 Characters!!!')
            return redirect('/home')

        quote=Quote.objects.create(message=request.POST['message'],quoted_by=User.objects.get(id=request.session['uid']))
        quote.wished_by.add(User.objects.get(id=request.session['uid']))
    # print 'created quoted_by', quote.name
    return redirect('/home')

def addtolist(request,id):
    Quote.objects.get(id=id).wished_by.add(User.objects.get(id=request.session['uid']))
    return redirect('/home')

def quotedBy(request,id):
    context={
            'user':User.objects.get(id=id),
            'quotes': Quote.objects.filter(quoted_by=id),
            'count': Quote.objects.filter(quoted_by=id).count(),
        }
    # print "user",context['quotes']
    return render (request, 'exam2/user.html',context)

def remove(request,id):
    Quote.objects.get(id=id).wished_by.remove(User.objects.get(id=request.session['uid']))
    # wished_item.remove()
    return redirect('/home')
