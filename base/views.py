from django.shortcuts import render

# Create your views here.
#query to the database

rooms = [
    {"id": 1,  "name": "Lets lear python"},
    {"id": 2,  "name": "Lets lear Design with me"},
    {"id": 3,  "name": "Frontend Developer"},
    {"id": 4,  "name": "Lets lear python"},
]


# create pages here render the templates
def home(request):
    context = { "rooms": rooms }
    return render(request, "base/home.html", context)

# pk get the value from URL
def room(request, pk):
    room = None
    for i in rooms:
        if i["id"] == int(pk):
            room = 1
    
    context = {"room": room}
    return render(request, "base/room.html", context)