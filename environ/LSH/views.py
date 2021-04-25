from django.http import HttpResponse 
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


from .forms import QuoteForm



def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"title": "The work I do",
		"this is true": True, 
		"my_number": 123,
		"my_list": [900, 4567, 1342, "Abc"],
		"my_html": "<h1>hello world</h1>"
	}
	return render(request, "about.html", my_context)

def projects_view(request, *args, **kwargs):
	return render(request, "projects.html", {})

def directory_view(request, *args, **kwargs):
	return render(request, "directory.html", {})

def prices_view(request, *args, **kwargs):
	return render(request, "prices.html", {})

def quoteView(request):
    if request.method == 'GET':
        form = QuoteForm()
    else:
        form = QuoteForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            website = form.cleaned_data['website']
            number = form.cleaned_data['number']
            about = form.cleaned_data['about']
            try:
                send_mail(name, email, website, number, about [cassandratalbot@yahoo.co.uk])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "quote/quote.html", {'form': form})
 

def successView(request):
    return HttpResponse("Success! Thank you for your message. We'll aim to get back to you within two working days!")

def updates_View(request, *args, **kwargs):
	return render(request, "updates.html", {})
