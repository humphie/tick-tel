from django.template import RequestContext
from tick.forms import *
from tick.tick_text.credit_purchase import *
from tick.models import *
from tick.communicate import *
from django.shortcuts import HttpResponse, render_to_response



#view for the main
def text(request):

    if request.user.is_authenticated():

        #check for the remaining Creditz
        credit    = Credit.objects.get(name=request.user.username)
        #get the phonenumbers
        numbers   = Phone.objects.filter(username=request.user.username)
        mail      = MailForm()
        send      = SendForm()
        phoneBook = PhoneBookForm()
        save      = BookForm()
        delete    = DeleteForm()
        search    = TextSearchForm()
        register  = RegForm()
        login     = LoginForm()
        organization = OrganisationForm()
        variables = RequestContext(request, { 'mail':mail,
                                              'send':send,
                                              'credit':credit,
                                              'phoneBook':phoneBook,
                                              'delete':delete,
                                              'numbers':numbers,
                                              'save':save,
                                              'search':search,
                                              'register':register,
                                              'login':login,
                                              'organization':organization
                                 })
 
        return render_to_response('text.html', variables)


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
 
        return render_to_response('text.html', variables)
#end otf the main method




#the recharge view
def recharge(request):

    msg_number = request.GET['number']


    if request.user.is_authenticated():

        #call the recharge method here 
        send_mail("credit", request.user.username, request.user.email)

        #call the send_text method here 
        send_text("Tick Text", "send the money to 256703000289", "humphie")
      
        return HttpResponse('''
                             <em id="res">Thanks %s, for purchasing %s credits units. 
                             Shortly you will receive instructions via sms!</em>
                             '''%(request.user.username, msg_number))

    else:
    
        return HttpResponse('<em id="res">%s units cost %d$</em>'%(msg_number, int(msg_number)*0.01))

#end of the recharge view



#Subscribe view
def subsribe(request):
    #call the communicate.send_mail method here
    return HttpResponse('''
                        <em id="res">Hello %s, an email has been sent to you! 
                        Follow instructions!</em>
                        '''%(request.user.username))
#end if the view
