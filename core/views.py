from django.http import JsonResponse
from django.shortcuts import redirect
from .forms import *
from .models import *


def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                subs_exist = NewsLetterSubscription.objects.get(email=email)
                subs_exist.subscribed = True
                subs_exist.save()
            except:
                subs = NewsLetterSubscription(email=email, subscribed=True)
                subs.save()
        else:
            return JsonResponse(form.errors)

    return redirect("/./")
