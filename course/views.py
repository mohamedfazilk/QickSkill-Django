from django.http import JsonResponse
from django.shortcuts import render


from course.models import Skill


def autocomplete(request):
    if 'term' in request.GET:
        qs = Skill.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for skill in qs:
            titles.append(skill.title)

        return JsonResponse(titles, safe=False)
    return render(request, 'course/home.html')
