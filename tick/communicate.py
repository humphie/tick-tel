'''
this class does the communication. that is email, text messaging and chating too
'''
import datetime
from models import Inbox
import urllib2, urllib
from django.shortcuts import HttpResponse
from django.core.mail import send_mail



#date to day
date = datetime.datetime.today()



#registration mail
reg_mail = '''
           Hello %s. Thank you for creating an account
           with Tick.'\n'
           Managment Tick Int.  
           '''


#send all messages from here
def send_text(name, message, contact):
  #a dict to hold the data
  data = {}
  #data in the dict
  data["username"]   = "256703000289"
  data["password"]   = "humphrey"
  data["sender"]     = name
  data["message"]    = message
  data["recipients"] = contact
  data["type"]       = "normal"
  #do the networking here
  mydata=urllib.urlencode(data)
  path='http://www.smsjaja.com/smsjaja-api.php'
  req=urllib2.Request(path, mydata)
  req.add_header("Content-type", "application/x-www-form-urlencoded")
  page=urllib2.urlopen(req)
  return 
#end of the send module


def sendMail(mail_type, name, mail):

  #check the type of mail to send
  if mail_type == "reg":
    #send mail here
    mail = Inbox.objects.create(
                                 sender='tick',
                                 recipient=name,
                                 message=reg_mail%(name), 
                                 flag='un_read',
                                 date=date
                                 )
#    print mail.id
    return
    
  elif mail_type == "credit":
    #send mail here
    mail = Inbox.objects.create(
                                sender='tick',
                                recipient=name,
                                message=mail,
                                flag='un_read',
                                date=date
                               )
#    print mail.id
    return
    
    
#method to dend mail
def mail(request):
  
  subject  = request.GET["subject"]
  email    = request.GET["email"]
  message  = request.GET["message"]
    
  #send mail here
  mail = Inbox.objects.create(
                              sender=email,
                              recipient="tick",
                              message=message,
                              flag='un_read',
                              date=date
                             )
  
  #if user is authenticated
  if request.user.is_authenticated():
  
    return HttpResponse('<em id="res">Thanks %s, your email has been received! You will be contacted shortly</em>'%(request.user.username))
    
  else:
    return HttpResponse('<em id="res">Thanks, your email has been received! You will be contacted shortly</em>')
