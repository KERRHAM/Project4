from django.shortcuts import render
from .models import About
from .forms import AddpostForm
from django.contrib import messages
# Create your views here.

def about_me(request):
    """
    Renders the About page
    """
    if request.method == "POST":
        addpost_form = AddpostForm(data=request.POST)
        if addpost_form.is_valid():
            addpost_form.save()
            messages.add_message(request, messages.SUCCESS, "Post request received! I endeavour to respond within 2 working days.")
    about = About.objects.all().order_by('-updated_on').first()
    addpost_form = AddpostForm()

    return render(
        request,
        "about/about.html",
       {
            "about": about,
            "addpost_form": addpost_form
        },
    )