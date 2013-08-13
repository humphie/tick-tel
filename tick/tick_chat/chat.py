import datetime
from tick.models import Inbox
from tick .db_manager import *
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User


#date to day
date = datetime.datetime.today()
#tick search form
tick_form = '''
         <form name="tick_search_form" id="tick_search_form">
           <input class="form-control" id="tick_query" type="text"
           name="tick_query" maxlength="16"
           placeholder="type a friend to view the conversation!" 
           onkeyup="setTimeout(function(){ conversation(); }, 3000);" />
         </form>
          '''



#function to get the conversation
def conversation(request):
  #check if the user is authenticated and the method is get
  if request.user.is_authenticated() and request.method == "GET": 
    #ge the username
    src      = request.GET['src']
    username = request.GET['username']
    #string form
    conversation=''
    #get the ticks
    ticks_to_username = Inbox.objects.filter( sender=src, recipient__istartswith=username )
    #get the ticks by the user
    ticks_to_src = Inbox.objects.filter( sender__istartswith=username, recipient=src )
    #join the ticks 2getha
    ticks = list(ticks_to_username)+list(ticks_to_src)
    #check if the are ticks
    if ticks:
      #form title
      conversation+='<form name="ticks" id="ticks">'
      #add the tick search
      conversation+=tick_form
  
      #loop thru the ticks
      for tick in ticks:
        #if the flag is un_read style the tick
        if tick.flag == 'un_read':
          conversation+='<div style="background:url(/static/images/un_read.png)30% 30% no-repeat;">'
        else:
          conversation+='<div style="background:url(/static/images/read.png)30% 30% no-repeat;">'
        #the ckeck box
        conversation+='<input type="checkbox" onchange="iaddon();" name="unread" value="%s">'%(tick.id)
        #check if the user is the sender or the recipient
        if src == tick.sender:
          conversation+='Sent to:&nbsp;&nbsp;%s<br />'%(tick.recipient)
        #user is the recipient
        else:
          conversation+='From:&nbsp;&nbsp;%s<br />'%(tick.sender)
        #message         
        conversation+='%s&nbsp;&nbsp;<br />'%(tick.message)
        #date
        conversation+='%s&nbsp;&nbsp;<br />'%(tick.date)
        conversation+='______________________________________________________________</div><br />'
      #close the form
      conversation+='</form>'
      #return the form
      return HttpResponse(conversation)         
    #no ticks
    else:
      conversation += tick_form
      conversation += '<strong id="res">No conversation with %s!</strong>'%(username)
    #return the form
    return HttpResponse(conversation)         
    
    


  #not authenticated or the request method is not get
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")
  
###############################################################################3  


#view to return unread ticks of a user
def sync_ticks(request):
  #check if the user is authenticated
  if request.user.is_authenticated():
    #string form
    un_read=''

    #get the username
    username  = request.GET['src']
    flag      = request.GET['flag']
    #check the flag
    if flag == 'all':
      #get all unread ticks
      tick1 = Inbox.objects.filter( recipient=username )
      #get the ticks by the user
      tick2 = Inbox.objects.filter( sender=username )
      #joint he ticks 2getha
      ticks = list(tick1)+list(tick2)
      #the title to send
      title = "<strong>You have %s ticks!</strong><br />"%(len(ticks))
    #the flag is un_read
    elif flag == 'un_read':
      #get all unread ticks
      ticks = Inbox.objects.filter(recipient=username, flag='un_read')
      #the title
      title = "<strong>You have %s Unread tick(s)!</strong><br />"%(len(ticks))
    #none ot the above
    else:
      #get all unread ticks
      ticks = ['ooohhhh', 'my God', 'i am being', 'hacked!!!!!!!!!!!']
      return HttpResponse(ticks)
     
    #check if the are ticks
    if ticks:
      #title
      un_read+=title
      #form title
      un_read+='<form name="ticks" id="ticks">'
      #add the tick search
      un_read+=tick_form
  
      #loop thru the ticks
      for tick in ticks:
        #if the flag is un_read style the tick
        if tick.flag == 'un_read':
          un_read+='<div style="background:url(/static/images/un_read.png)30% 30% no-repeat;">'
        else:
          un_read+='<div style="background:url(/static/images/read.png)30% 30% no-repeat;">'
        #the ckeck box
        un_read+='<input type="checkbox" onchange="iaddon();" name="unread" value="%s">'%(tick.id)
        #check if the user is the sender or the recipient
        if username == tick.sender:
          un_read+='Sent to:&nbsp;&nbsp;%s<br />'%(tick.recipient)
        #user is the recipient
        else:
          un_read+='From:&nbsp;&nbsp;%s<br />'%(tick.sender)
        #message         
        un_read+='%s&nbsp;&nbsp;<br />'%(tick.message)
        #date
        un_read+='%s&nbsp;&nbsp;<br />'%(tick.date)
        un_read+='______________________________________________________________</div><br />'  
      un_read+='</form>'
      #return all unread ticks
      return HttpResponse(un_read)
    #no ticks
    else:
      un_read += tick_form
      un_read += '<strong id="res">No unread ticks!</strong>'
      #return the form
      return HttpResponseRedirect('/Sync_ticks/?src=%s&flag=%s'%(username, 'all'))         
  
  #user not authenticated
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")
#end of the view


#method to reply a tick
def reply_tick(request):
  #user must be authenticated
  if request.user.is_authenticated():
  
    #get the sent data
    src     = request.GET['src']
    Id      = request.GET['id']
    message = request.GET['message']
    
    
    #check if the is empty
    if Id != "" or Id == 0:

      #put a for loop incase they are multiple ids
      for recip in Id[:-1].split(','):

        #ge the inforabout the id    
        id_meta_data = Inbox.objects.get(id=recip)
        #if the source is the recipient
        if id_meta_data.sender != src:
          # send the tick
          tick = Inbox.objects.create(
                                      sender=src,
                                      recipient=id_meta_data.sender,
                                      message=message, 
                                      flag='un_read',
                                      date=date
                                     )
          #change the flag of the id tick to read
          flag = Inbox.objects.filter(id=recip).update(flag="read")
          #return a success message
          return HttpResponse("<em id='res'>Tick sent successfuly to %s</em>"%(id_meta_data.sender))

        #user not the recipient
        else:
          #return a success message
          return HttpResponse("<em id='err'>Hello %s, you cant tick your self!!</em>"%(src))
    
    #id is emty
    else:
      return HttpResponse("<em id='err'>the Tick wasn't sent, select the user to reply!</em>")    
  
  #user not authenticated
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")




#function to send a tick
def send_tick(request):
  #check if user is authenticated
  if request.user.is_authenticated():
    #get the request data
    src   = request.GET['src']
    names = request.GET['name']
    message = request.GET['message']
    #get the sender
    if src == request.user.username:
      sender = request.user.username
    else:
      sender = src  
    #in case there are multiple
    for name in names.split(','):
      #check if the user really exists
      user1 = User.objects.filter(username__exact=name)
      # check also in the staff member table
      user2 = memberAcount.objects.filter(username__exact=name)
      if user1 or user2:
        #sent the tick
        tick = Inbox.objects.create(
                                    sender=sender,
                                    recipient=name,
                                    message=message, 
                                    flag='un_read',
                                    date=date
                                  )
        #return a success message
        return HttpResponse('<em id="res">Tick has been delivered successfuly.</em>')

      #user not found
      else:
        return HttpResponse('<em id="err">Sorry, the user %s does not exist on Tick.</em>'%(name))
  #user no authenticated
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")  
    


    
#function to mack ticks as read
def mark_read(request):
  #if user.is_authenticated():
  if request.user.is_authenticated():
    #get the id from the user
    src = request.GET['src']
    Id  = request.GET['id']
    #check if the id is empty
    if Id !="":
      #afor loop incase they are multiple
      for tick in Id[:-1].split(','):

        #change the flag of the id tick to read
        flag = Inbox.objects.filter( id=tick, recipient=src ).update(flag="read")
      #send a success message
      return HttpResponse('<em id="res">Tick(s) have been marked read.</em>')
      
    #id id null
    else:
      return HttpResponse('<em id="err">No Tick has been selected.</em>')  
 
  #else user not 
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")
    

    
#function to delete a Tick
def tick_delete(request):
  #if user.is_authenticated():
  if request.user.is_authenticated():
    #get the id from the user
    Id  = request.GET['id']
    src = request.GET['src']
    #check if the id is empty
    if Id !="":
      #a for loop in case they are multiple
      for tick in Id[:-1].split(','):
        #change the flag of the id tick to read
        flag = Inbox.objects.filter(id=tick, recipient=src).delete()

      #send a success message
      return HttpResponse('<em id="res">Tick(s) have been deleted.</em>')
  
    #id id null
    else:
      return HttpResponse('<em id="err">All read messages hav been deleted.</em>')  
 
  #else user not 
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")

