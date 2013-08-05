from tick.forms import CreditForm
from tick.communicate import *
from tick.db_manager import *
from django.shortcuts import HttpResponse

'''
class that handles message purchasing issues
'''


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
    
  
