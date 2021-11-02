from django.shortcuts import render

from .crawler import my_form_post
from .forms import TestForm


def test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            complt_data = my_form_post(keyword)

            return render(request, 'scraper/test.html', {'complt_data': complt_data})
        else:
            return render(request, 'scraper/form.html', {'form': form})
    form = TestForm()
    return render(request, 'scraper/form.html', {'form': form})
