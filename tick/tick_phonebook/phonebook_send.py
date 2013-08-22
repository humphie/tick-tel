from itertools import chain
from tick.communicate import *
from tick.models import *
from tick.db_manager import *
from django.shortcuts import HttpResponse


def phonebook(request):

  if request.user.is_authenticated():
    
    msg_sent = 1
    group   = request.GET['group']
    message = request.GET['message']
    #check the group
    if group == "staff":
      #get the numbers in the phonebook
      phonebook_numbers = memberAcount.objects.filter(owner=request.user.username )
    #group is all
    elif group  == "all":
      #call the send to all method 
      contacts1 = list(memberAcount.objects.filter(owner=request.user.username ))
      #list the secont set
      contacts2 = list(Phone.objects.filter(username=request.user.username, group=group))
      #join the two listas 2getha
      phonebook_numbers = contacts1 + contacts2
      
    #else a given group
    else:
      phonebook_numbers = Phone.objects.filter(username=request.user.username, group=group)
      
    #check for the remaining Creditz
    credit = Credit.objects.get(name=request.user.username)
        
    if credit.credit > 30:
      if phonebook_numbers:
          
        #call the communicate.send_text method inside the loop
        for contact in phonebook_numbers:

          send_text(request.user.username, message, contact.contact)

          #increament by 1
          msg_sent+=1
          #  if the number if messages sent > credit
          if msg_sent*30 > credit.credit:
            #call the acc_ up date method here
            credit_and_update_an_account(request.user.username, (msg_sent-1)*30)
            #save areport
            report(request.user.username, "phonebook-to-%s"%(group), message, msg_sent-1)
            #jump out of the loop
            break
        #if there is only one contact
        if len(phonebook_numbers) == 1:
          #call the acc_ up date method here
          credit_and_update_an_account(request.user.username, 30)
          #save areport
          report(request.user.username, "phonebook-to-%s"%(group), message, msg_sent-1)
        else:
          #call the acc_ up date method here
          credit_and_update_an_account(request.user.username, (msg_sent-1)*30)
          #save areport
          report(request.user.username, "phonebook-to-%s"%(group), message, msg_sent-1)

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

