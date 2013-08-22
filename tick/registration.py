from tick.db_manager import *
from tick.communicate import *
from tick_regulator.regulator import *
from django.shortcuts import HttpResponse

mail = '''
        Hello %s, you have received 500 units for your enjoyment! To learn more 
        <a href='#!/page_Services'>click here.</a> 
       '''

#method th create an account
def register(request):
  
  #check the request method
  if request.method == "GET":

    username   = request.GET['username']
    contact    = request.GET['contact']
    country    = request.GET['country']
    email      = request.GET['email']
    password   = request.GET['password']
    #call the create_new_user_method save the user in the data base
    create_a_user(username, password, email)
    
    #credit the user with two smsz for trial
    create_a_credit_account(username, 500)
 
    #create a staff
    create_a_staff_member(username,
                          username, 
                          password, 
                          'administrator', 
                          contact,
                          country, 
                          'admin', 
                           )

    #send confirmation mail
    sendMail("reg", username, '')
    #send credit mail
    sendMail("credit", username, mail%(username))
 
    return HttpResponse('<em id="res">Account has been successfuly created!<a href="#!/page_Login"> Click here to login</a></em>')
    
  else:
     
     return HttpResponse("Invalid request")  
