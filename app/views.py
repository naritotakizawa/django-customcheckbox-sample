from django.shortcuts import render
from .forms import SampleForm


def top(request):
    form = SampleForm(request.GET or None)
    context = {'form': form}
    if form.is_valid():
        tags = form.cleaned_data.get('tags')
        if tags:
            print(tags)
    return render(request, 'app/top.html', context)
