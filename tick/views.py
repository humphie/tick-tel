from django.contrib import auth
from tick.forms import *
from models import *
from tick.db_manager import *
from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, render_to_response
from django.http import HttpResponseRedirect




#view for terms page
def main(request):

  if request.user.is_authenticated():

    return HttpResponseRedirect('/logout/')

  else:
    
    login    = LoginForm()
    mail     = MailForm()  
    variables = RequestContext(request, { 'mail':mail, 
                                          'login':login, 
                                          }) 
    return render_to_response('tick.html', variables)
#end of the services view


#credit purchase
def credit(request):

  if request.user.username == "tick":
  
    username = request.GET['username']
    amount   = request.GET['amount']

    #send the values to the db_mnager module module
    credit_an_acount(username, amount)

    #send mail to the user
            

    return HttpResponse('''
                          <em id="res">The account %s has been credited with %s units!</em>
                        '''%(username, amount))

    
  else:
    return HttpResponse('<em id="err">You are not allowed to make this transaction!</em>') 



#view forlogout
def logout(request):
  auth.logout(request)
  return HttpResponseRedirect('/')


#view for logsIn
def login(request):
  
  #check the post method 
  if request.method == "POST":
    form = LoginForm(request.POST)
    
    #check if the form is valid
    if form.is_valid():        
    
      #extract from the form
      username     = form.cleaned_data['username']
      password     = form.cleaned_data['password']

      try:
        #check if the username  the password
        super_User = User.objects.get(username=username)
      except:
        super_User = []
      #it the user is in the User table
      if super_User:
        #authenticate the user
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
          #authenticate the user
          auth.login(request, user) 
          #check if the user is the account is private or organizatio
          account_type = memberAcount.objects.filter(owner=username, username=username, acc_type="public")
          #send the user to the rigt direction
          if account_type:
            #set the destination to super user
            destination = HttpResponseRedirect('/super_user/')
          #not a super user
          else:
            #set the destination to private user
            destination = HttpResponseRedirect('/private_user/')
        #send the user to admins site's home
        return destination

          

      #the staff user not the super user
      else:
        #check if the user is a staff user
        staff_User = memberAcount.objects.filter(username=username, password=password)
 
        if staff_User:
          #get the organization
          staff = memberAcount.objects.get(password=password)
          #get the arganization in which the staff belongd
          organization = User.objects.get(username=staff.owner)
          #authenticate the user
          user = auth.authenticate(username=organization, password=organization)
          if user is not None and user.is_active:
 
            #authenticate the user
            auth.login(request, user) 
        
            #send the user to the staff home
            return HttpResponseRedirect('/user_staff/?org_acc/id-name=%s'%(username))


        else:
          return HttpResponseRedirect('/') 
    else:              
      return HttpResponseRedirect('/') 

  else:              
    return HttpResponseRedirect('/') 

#end of the loggin view






#redirection for the account owners
def super_user(request):
  #if user is authenticated
  if request.user.is_authenticated():
    
    #check for the remaining smsz
    credit     = Credit.objects.get(name=request.user.username)
    #get the unread inbox
    un_read   = Inbox.objects.filter(recipient=request.user.username, flag="un_read")
    #get all the ticks
    all_ticks = Inbox.objects.filter(recipient=request.user.username)
    #get the phonenumbers
    numbers      = Phone.objects.filter(username=request.user.username)
    send         = SendForm()
    phoneBook    = PhoneBookForm()
    saveNum      = BookForm()
    deleteNum    = DeleteForm()
    searchNum    = TextSearchForm()
    mail         = MailForm()
    calendar     = calendarForm()
    login        = LoginForm()
    creditForm   = CreditForm()
    deleteEve    = deleteEvent()
    addMember    = MemberForm()
    deleteMember = DeleteForm()
    members      = memberAcount.objects.get(username=request.user.username)
       
    variables    = RequestContext(request, { 
                                            'deleteMember':deleteMember,
                                            'super_user':'super_user',
                                            'members':members,
                                            'mail':mail,
                                            'send':send,
                                            'all_ticks':all_ticks,
                                            'phoneBook':phoneBook,
                                            'deleteNum':deleteNum,
                                            'numbers':numbers,
                                            'saveNum':saveNum,
                                            'searchNum':searchNum,
                                            'credit':credit,
                                            'creditForm':creditForm,
                                            'deleteForm':deleteEve,
                                            'un_read':un_read,
                                            'login':login,
                                            'members':members,
                                            'addMember':addMember }) 
    return render_to_response('tick.html', variables)
      
  #user not admin
  else:  
    return HttpResponseRedirect('/')
    
    
    
#view for the staff user
def staff_user(request):
    
  if request.user.is_authenticated():
    #get the name
    name = request.GET['org_acc/id-name']
    if name != '':
      #get the organisation numbers
      members    = memberAcount.objects.get(username=request.user.username)
      #check for the remaining smsz
      credit     = Credit.objects.get(name=request.user.username)
      #get the unread inbox
      un_read   = Inbox.objects.filter(recipient__exact=name, flag="un_read")
      #get all the ticks
      all_ticks = Inbox.objects.filter(recipient__exact=name)
      #get the phonenumbers
      numbers    = Phone.objects.filter(username=request.user.username)
      #get the phonenumbers
      send       = SendForm()
      phoneBook  = PhoneBookForm()
      searchNum  = TextSearchForm()
      mail       = MailForm()
      login      = LoginForm()
      variables  = RequestContext(request, {
                                            'un_read':un_read,
                                            'all_ticks':all_ticks,
                                            'name':name,
                                            'mail':mail,
                                            'send':send,
                                            'phoneBook':phoneBook,
                                            'numbers':numbers,
                                            'members':members,
                                            'searchNum':searchNum,
                                            'credit':credit,
                                            'login':login,
                                   })
 
      return render_to_response('tick.html', variables)
    #if the name is none
    else:
      return HttpResponseRedirect('/')
  #user not authenticated
  else:
    return HttpResponseRedirect('/')



#view for the private account
def private_user(request):
  #if user is authenticated
  if request.user.is_authenticated():  
    #get the organisation numbers
    members    = memberAcount.objects.get(username=request.user.username)
    #check for the remaining smsz
    credit    = Credit.objects.get(name=request.user.username)
    #get the unread inbox
    un_read   = Inbox.objects.filter(recipient=request.user.username, flag="un_read")
    #get all the ticks
    all_ticks = Inbox.objects.filter(recipient=request.user.username)
    #get the phonenumbers
    numbers   = Phone.objects.filter(username=request.user.username)
    send      = SendForm()
    phoneBook = PhoneBookForm()
    saveNum   = BookForm()
    deleteNum = DeleteForm()
    searchNum = TextSearchForm()
    mail      = MailForm()
    calendar  = calendarForm()
    login     = LoginForm()
    deleteEve = deleteEvent()
    variables = RequestContext(request, { 
                                            'mail':mail,
                                            'send':send,
                                            'phoneBook':phoneBook,
                                            'members':members,
                                            'deleteNum':deleteNum,
                                            'all_ticks':all_ticks,
                                            'numbers':numbers,
                                            'saveNum':saveNum,
                                            'credit':credit,
                                            'un_read':un_read,
                                            'private_user':'private_user',
                                            'searchNum':searchNum,
                                            'credit':credit,
                                            'calendar':calendar,
                                            'deleteForm':deleteEve,
                                            'login':login,
                                             }) 
    return render_to_response('tick.html', variables)
      
  #user not admin
  else:  
    return HttpResponseRedirect('/')
  
