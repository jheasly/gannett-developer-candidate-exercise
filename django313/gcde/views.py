
import requests

from django.http import HttpResponse
from django.template import loader
# from django.shortcuts import render

# Create your views here.

def home(request):
    # check Django anonymous user session to see if a pid is already stored
    existing_pid = request.session.get('pid')

    # in either existing_pid case, we need to do this
    session = requests.Session()

    if existing_pid:
        # template needs a get_pid
        get_pid = existing_pid

        # add existing_pid to the requests package request cookies
        jar = requests.cookies.RequestsCookieJar()
        jar.set('pid', existing_pid)
        session.cookies = jar

        # make the heroku request
        response = session.get('https://peaceful-springs-7920.herokuapp.com/profile/')

        # uncomment for testing, to clear existing session data
        # request.session.clear()
    else:
        # a "first-time" request
        response = session.get('https://peaceful-springs-7920.herokuapp.com/profile/')

        # get the pid from the first-time request
        get_pid = response.cookies.get('pid')

        # add pid to Django anonymous user session
        request.session['pid'] = get_pid

        # set expire of Django anonymous user session for 365 days from now
        one_year_from_now_in_seconds = 60 * 60 * 24 * 365 # = 31,536,000
        request.session.set_expiry(one_year_from_now_in_seconds)

    # get profile-specific content
    r = requests.get('https://peaceful-springs-7920.herokuapp.com/content/{}/'.format(get_pid))
    articles = r.json()

    # display results
    template = loader.get_template('gcde/index.html')
    context = {
        'headline': 'My Delicious Articles',
        'get_pid': get_pid,
        'articles': articles['articles'],
        'theme': articles['theme'],
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("My Delicious Articles")
