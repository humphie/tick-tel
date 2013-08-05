from tick.communicate import *
from tick.models import *
from tick.db_manager import *
from django.shortcuts import HttpResponse


def phonebook(request):

  if request.user.is_authenticated():
    
    msg_sent = 1
    group   = request.GET['group']
    message = request.GET['message']

    #get the numbers in the phonebook
    phonebook_numbers = Phone.objects.filter(username=request.user.username, group=group)

    #check for the remaining Creditz
    credit = Credit.objects.get(name=request.user.username)
        
    if credit.credit >= 30:
      
      if phonebook_numbers:
    
        #call the communicate.send_text method inside the loop
        for contact in phonebook_numbers:
          #send the msg
#          send_text(request.user.username, message, contact.contact)
          #increament by 1
          msg_sent+=1
          #  if the number if messages sent > credit
          if msg_sent*30 > credit.credit:
            #call the acc_ up date method here
            credit_and_update_an_account(request.user.username, (msg_sent-1)*30)
            #jump out of the loop
            break
        #send a success message
        return HttpResponse("""
                             <em id='res'>Message has been sent to %d contact(s).
                             You have been charged %d units.
                             </em>
                           """%(msg_sent-1, (msg_sent-1)*30))
      
      #phonebook is empty
      else:
        return HttpResponse("<em id='err'>phonebook is empty or there is no such agroup!</em>")  
    #if credit is less than 30 units
    else:
      return HttpResponse("""
                           <em id='err'>Sorry you have insurficient credit on your account,
                            please recharge</em>
                          """)
  #user not authenticated
  else:
    return HttpResponse('<em><a href="#!/page_Login" id="err">Click here to login</a></em>')

