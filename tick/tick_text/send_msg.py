from django.shortcuts import HttpResponse
from tick.communicate import *
from tick.db_manager import *


#send text here
def sms_text(request, name, message, contacts, credit):
  #send an Credit in atry statment
  try:
  
    #check the counter here
    if credit != 0:
      #the messages sent
      msg_sent = 1
      for contact in contacts.split(','):
        # send the message here
        send_text(name, message, contact)
        #increament by 1
        msg_sent+=1

        #  if the number if messages sent == credit
        if msg_sent*30 > credit:
          #call the acc_ up date method here
          credit_and_update_an_account(request.user.username, (msg_sent-1)*30)
          #save areport
          report(request.user.username, name, message, msg_sent-1)
          #break the loop and send asuccess message
          break
          
      #success message here
      return HttpResponse("""
                          <em id='res'>Message has been sent to %s contact(s), 
                          and you have been charged %s units</em>
                       """%(msg_sent-1, (msg_sent-1)*30))
            
    #if credit is 0   
    else:
      # send the message here
      send_text(name, message, contacts)
      #call the acc_ up date method here
      credit_and_update_an_account(request.user.username, len(contacts.split(','))*30)
      #save areport
      report(request.user.username, name, message, len(contacts.split(',')))
      #send mail
      #send_mail("update_mail", name, request.user.email)
        
      #success message here
      return HttpResponse("""
                           <em id='res'>Message has been sent to %s contact(s), 
                           and you have been charged %s units</em>
                          """%(len(contacts.split(',')), len(contacts.split(','))*30))
  except:
    #failure message here
    return HttpResponse("""<em id='err'>the message has not been sent due to
                           server issues, try again later please</em>
                        """)
 

  
  

def text_msg(request):

  #is the user authenticated
  if request.user.is_authenticated():
  
    name    = request.GET["name"]
    message = request.GET["message"]
    contact = request.GET["contact"]

    #check for the remaining Creditz
    remaining_credit = Credit.objects.get(name=request.user.username)
    
    #if credit is zero
    if remaining_credit.credit < 30:
      #error mesage   
      return HttpResponse("<em id='err'>You don't have enough credit on your account, please recharge</em>")
        
    #if cost is less or equal to remaining credit
    elif len(contact.split(','))*30 <= remaining_credit.credit:
      #call the send function here    
      return sms_text(request, name, message, contact, 0)
      
    #cost is greater than credit remaining 
    elif len(contact.split(','))*30 > remaining_credit.credit:
      #call the send function here
      return sms_text(request, name, message, contact, remaining_credit.credit) 
    
  #user not authenticated
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You must be logged in, click here!</a></em>")
