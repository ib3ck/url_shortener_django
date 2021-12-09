from django.shortcuts import render, redirect
from .models import short_url
from .forms import UrlForm
from .shortner import shortner


def Home(request, token):
    su: short_url = short_url.objects.filter(short_url=token)[0]
    su.count += 1
    su.save()

    return redirect(su.long_url)


def Make(request):
    form = UrlForm(request.POST)
    urls = short_url.objects.all()
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = shortner().issue_token()
            NewUrl.short_url = a
            NewUrl.save()
        else:
            form = UrlForm()
            a = "Invalid URL"
    return render(request, 'home.html', {'form': form, 'a': a, 'urls': urls})
