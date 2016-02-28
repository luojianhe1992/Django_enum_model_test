from django.shortcuts import render

# allow us to redirect
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.template import RequestContext, loader

# import the User class in models.py
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# import the auth.models User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from WebApp.models import *


@login_required
def index(request):
    print("in the index function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/index.html', context)



# registration is normal route, and login is login is "django.contrib.views.login"
def registration(request):
    errors = []
    context = {}
    if request.method == "GET":
        return render(request, 'WebApp/register.html', context)

    # add 'errors' attribute to the context
    context['errors'] = errors

    password1 = request.POST['password']
    password2 = request.POST['password_confirmation']

    if password1 != password2:

        print("Passwords did not match.")

        # error1 happens
        errors.append("Passwords did not match.")

    if len(User.objects.all().filter(username = request.POST['user_name'])) > 0:
        print("Username is already taken.")

        # error2 happens
        errors.append("Username is already taken.")

    if errors:
        return render(request, 'WebApp/register.html', context)

    # create a new user from the valid form data, using create_user function with 2 arguments, 'username' and 'password'
    new_user = User.objects.create_user(username=request.POST['user_name'], password=request.POST['password'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    new_user.save()

    # using 'authenticate' function
    new_user = authenticate(username = request.POST['user_name'], password = request.POST['password'])

    # using 'login' function
    login(request, new_user)

    # using 'redirect' function
    return redirect(reverse('message'))

@login_required
def message(request):
    print("in the message function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/message.html', context)

@login_required
def upload(request):
    print("in the upload function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/upload.html', context)

@login_required
def preprocess(request):
    print("in the preprocess function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/preprocessing.html', context)

@login_required
def visualization(request):
    print("in the visualization function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/knnresult.html', context)

# def logout view
def my_logout(request):
    logout(request)
    return redirect(reverse('index'))

@login_required
def honeycell(request):
    print("in the honeycell function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/honeycell.html', context)

@login_required
def honeycomb(request):
    print("in the honeycomb function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/honeycomb.html', context)

@login_required
def analytics(request):
    print("in the analytics function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/analytics.html', context)


from WebApp.forms import *

@login_required
def add_car(request):
    print("in the add_car function.")

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    if request.method == "GET":
        print("in the GET method of add_car function.")

        form = CarModelForm()
        context['form'] =  form

        return render(request, 'WebApp/add_car.html', context)

    else:
        print("in the POST method of add_car function.")

        form = CarModelForm(request.POST, request.FILES)
        context['form'] = form

        print("%" * 30)
        # print(form)
        print("%" * 30)

        if not form.is_valid():
            print("The form is not valid.")
            errors.append("The form is not valid.")

            return render(request, 'WebApp/add_car.html', context)
        print("The form is valid.")

        car_owner = form.cleaned_data.get('car_owner')
        car_name = form.cleaned_data.get('car_name')
        car_color = form.cleaned_data.get('car_color')
        car_size = form.cleaned_data.get('car_size')

        print("%" * 30)
        print(car_owner)
        print(car_name)
        print(car_color)
        print(car_size)
        print("%" * 30)

        if len(Car.objects.filter(car_name=car_name)):
            print("The car_name already exist.")
            errors.append("The car_name already exist.")

            return render(request, 'WebApp/add_car.html', context)

        form.save()
        print("Already save the form.")

        return render(request, 'WebApp/add_car.html', {'user': request.user, 'form': CarModelForm()})


@login_required
def show_cars(request):
    print("in the show_cars function.")

    context = {}
    context['user'] = request.user

    cars = Car.objects.all()
    context['cars'] = cars

    for car in cars:
        print("%" * 60)
        print(car.car_owner)
        print(car.car_name)
        print(car.car_color)
        print(car.car_size)
        print(car.car_time_created)
        print(car.car_time_changed)
        print("%" * 60)

        print('\n')


    return render(request, 'WebApp/show_cars.html', context)
