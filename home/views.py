from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def home(request):
    # return HttpResponse('''
    #     <h1>I'm a Django Server</h1>
    #     <hr />
    #     <h3 style="color:red;">Loving it</h3>
    # ''')

    peoples = [
        {"name": "Sai nithin", "age": 19},
        {"name": "Prane", "age": 20},
        {"name": "Abhi", "age": 15},
        {"name": "Srikar", "age": 16},
    ]
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

    vegetables = ["Tomato", "Potato", "Pumpkin"]

    context = {
        "peoples": peoples,
        "text": text,
        "vegetables": vegetables,
        "title": "Home",
    }
    return render(request, "home/index.html", context)


@login_required(login_url="/login")
def about(request):
    context = {"title": "About"}
    return render(request, "home/about.html", context)


@login_required(login_url="/login")
def contact(request):
    context = {"title": "Contact"}
    return render(request, "home/contact.html", context)


@login_required(login_url="/login")
def start_page(request):
    print("*" * 10)
    return HttpResponse("This is Landing Page")
