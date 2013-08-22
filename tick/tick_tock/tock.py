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
       You can upgrade or install the latest browser.\n
       Tick Int
       """
       
refused = """
           Hey %s, you have denied Tick access to your microphone for Tock
            (a abrowser to browser audio chating app), to anble Tock, change
             the settings, reload the page, 
             then allow your browser to access your microphone.\n Thanks Tick Int   
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
  src  = request.GET['src'] 
  flag = request.GET['flag']
  #location = request.GET['location']
  #check the flag and then send the right mail
  if flag == "fail":
    #set the message
    message = fail%(src)
  elif flag == "refused":
    message = refused%(src)   
  else:
    message = "Hey %s, if you are trying to hack, then sorry, i am un-hackable!!!!!!"%(request.user.username)
  #send a tick
  mail = Inbox.objects.create(
                                sender='tick',
                                recipient=src,
                                message=message,
                                flag='un_read',
                                date=date
                               )
  return
################################################################################

