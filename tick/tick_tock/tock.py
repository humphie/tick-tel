from tick.models import Inbox, Credit
from tick.communicate import *
from tick.db_manager import *
import datetime


#date to day
date = datetime.datetime.today()
#fail message
fail = """
       Hey %s, sorry your browser can't support Tock(a browser to 
       browser calling app).
       You can grade or install the latest browser'\n'
       Tick Int
       """


################################################################################
def credit_deduct(request):
  #get the initial credit
  init_credit = Credit.objects.get(name=request.user.username)
  #deduct the amount
  amount = init_credit.credit-50
  #save the amount
  current_account = Credit.objects.filter(name=request.username).update(credit=amount)
  #return
  return 
################################################################################


################################################################################
def tock(request):
  flag     = request.GET['flag']
#  location = request.GET['location']
  #check the flag and then send the right mail
  if flag == "fail":
    #send a tick
    mail = Inbox.objects.create(
                                sender='tick',
                                recipient=request.user.username,
                                message=fail%(request.user.username),
                                flag='un_read',
                                date=date
                               )
    return
    
  elif flag == "credit":
    #call the acc_ up date method here
    credit_and_update_an_account(request.user.username, 50)
    return

  else:
    
    return HttpResponseRedirect('/')
################################################################################

