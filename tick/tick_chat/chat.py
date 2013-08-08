import datetime
from tick.models import Inbox
from tick .db_manager import *
from django.shortcuts import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User


#date to day
date = datetime.datetime.today()



#view to return unread ticks of a user
def sync_ticks(request):
  #check if the user is authenticated
  if request.user.is_authenticated():
    #string form
    un_read=''
    #ge the username
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
  
      #loop thru the ticks
      for tick in ticks:
        #if the flag is un_read style the tick
        if tick.flag == 'un_read':
          un_read+='<div style=background-color:#CCFFFF;>'
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
        un_read+='%s&nbsp;&nbsp;'%(tick.date)
        #put the flag if the request is for all ticks
        if flag == 'all':
          un_read+='<em id="res">%s</em><br />'%(tick.flag)
          un_read+='______________________________________________________________'
       #else
        else:
          un_read+='<br />'
          un_read+='______________________________________________________________'  
        #cloz the div if the flag i un_read
        if tick.flag == 'un_read':
          un_read+='</div>'
      un_read+='</form>'
    #no ticks
    else:
      un_read = '<strong id="res">No unread ticks!</strong>'
    #return the form
    return HttpResponse(un_read)         
  
  #user not authenticated
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")
#end of the view


#method to reply a tick
def reply_tick(request):
  #user must be authenticated
  if request.user.is_authenticated():
  
    #get the sent data
    src  = request.GET['src']
    Id      = request.GET['id']
    message = request.GET['message']
    
    
    #check if the is empty
    if Id != "" or Id == 0:

      #put a for loop incase they are multiple ids
      for recip in Id[:-1].split(','):

        #ge the inforabout the id    
        id_meta_data = Inbox.objects.get(id=recip)
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
      #rturn a success message
      return HttpResponse("<em id='res'>Tick sent successfuly to %s</em>"%(id_meta_data.sender))
    
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
    #get the request dataa
    names = request.GET['name']
    message = request.GET['message']
    
    #in case there are multiple
    for name in names.split(','):
      #check if the user really exists
      user1 = User.objects.filter(username__exact=name)
      # check also in the staff member table
      user2 = memberAcount.objects.filter(username__exact=name)
      if user1 or user2:
        #sent the tick
        tick = Inbox.objects.create(
                                    sender=request.user.username,
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
        break;
  #user no authenticated
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")  
    
    
#function to mack ticks as read
def mark_read(request):
  #if user.is_authenticated():
  if request.user.is_authenticated():
    #get the id from the user
    Id = request.GET['id']
    #check if the id is empty
    if Id !="":
      #afor loop incase they are multiple
      for tick in Id[:-1].split(','):

        #change the flag of the id tick to read
        flag = Inbox.objects.filter(id=tick).update(flag="read")
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
    Id = request.GET['id']
    #check if the id is empty
    if Id !="":
      #a for loop in case they are multiple
      for tick in Id[:-1].split(','):
        #change the flag of the id tick to read
        flag = Inbox.objects.filter(id=tick).delete()

      #send a success message
      return HttpResponse('<em id="res">Tick(s) have been deleted.</em>')
  
    #id id null
    else:
      return HttpResponse('<em id="err">All read messages hav been deleted.</em>')  
 
  #else user not 
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")
