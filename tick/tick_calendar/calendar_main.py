from django.contrib import auth
from django.template import RequestContext
from tick.forms import *
from tick.models import *
from tick.communicate import *
from django.shortcuts import render_to_response




#view for the main
def calendar(request):

    if request.user.is_authenticated():

        #check for the remaining smsz
        credit    = Credit.objects.get(name=request.user.username)
        #get the phonenumbers
        mail      = MailForm()
        register  = RegForm()
        calendar  = calendarForm()
        login     = LoginForm()
        delete    = deleteEvent()
        organization = OrganisationForm()
        variables = RequestContext(request, { 'mail':mail,
                                              'credit':credit,
                                              'calendar':calendar,
                                              'deleteForm':delete,
                                              'register':register,
                                              'login':login,
                                              'organization':organization
                                 })
 
        return render_to_response('calendar.html', variables)


    else:

        mail     = MailForm()
        register = RegForm()
        login    = LoginForm()
        organization = OrganisationForm()
        variables = RequestContext(request, {
      
                                          'mail': mail,
                                          'register':register,
                                          'login':login,
                                          'organization':organization
                                 })
 
        return render_to_response('calendar.html', variables)
#end otf the main method

