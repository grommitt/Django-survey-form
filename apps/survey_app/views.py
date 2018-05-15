from django.shortcuts import render, HttpResponse, redirect

# the index function is called when root is visited
def index(request):
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request, 'survey_app/survey.html', context={'num_visits':num_visits})


def results(request):
    if request.method == "POST":   
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/results')
    else:
        return render(request, 'survey_app/results.html')




