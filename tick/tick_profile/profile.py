from tick.models import memberAcount, Inbox
from tick .db_manager import *
from django.shortcuts import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


#methos to edit the the profile
def change_account(request):
  #check if the user is authenticated
  if request.user.is_authenticated():
    #get the account type
    acc_type = request.GET['acc_type']
    #check if the request was empty
    if acc_type != "":
      #get the current account type
      current_acc_type = memberAcount.objects.get(owner=request.user.username)
      #account type organization
      if current_acc_type.acc_type == "public" and acc_type == "private":
        #delete all the staff members 
        staff_members = memberAcount.objects.filter(owner=request.user.username)
        # a for loop to delete
        for staff in staff_members:
          #if the user is an admin
          if staff.position != "administrator":
            #delete the staff
            staff.delete()
            #remove the ticks too
            ticks = Inbox.objects.filter(recipient=staff.username).delete()
      
        #update the account cow
        new_account = memberAcount.objects.filter(owner=request.user.username).update(acc_type=acc_type)
        #send a success message
        return HttpResponse("<em id='res'>Your account has been changed successfuly.<a href='/'>Click here to continue!</a></em>")
      
      #account type is private
      elif current_acc_type.acc_type == "private" and acc_type == "public":
        #update the account cow
        new_account = memberAcount.objects.filter(owner=request.user.username).update(acc_type=acc_type)
        #send a success message
        return HttpResponse("<em id='res'>Your account has been changed successfuly.<a href='/'>Click here to continue!</a></em>")
      
      
      #acount is not defined
      else:
        return HttpResponse("<em id='err'>There is nothing to be changed!!</em>")
    #the request is epmty
    else:
      return HttpResponse("<em id='err'>Hacker????????????????</em>")  
  #not authenticated
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")
###########################################################################################################S  



#method to change the password
def change_password(request):
  #check if the user is authenticated
  if request.user.is_authenticated():
    #get the paswords
    password = request.POST['change_password']
    #get the user and change the password
    new_password = User.objects.get(username__exact=request.user.username)
    new_password.set_password(password)
    new_password.save()
    #redierect to the home page
    return HttpResponseRedirect("/")
  #not authenticated
  else:
    return HttpResponseRedirect("/")
###########################################################################################################S  




#method to change the account type
def profile_edit(request):
  #check if the user is authenticated
  if request.user.is_authenticated():
    #get the user data
    full_name   = request.POST['edit_full_name']
    contact     = request.POST['edit_contact']
    simple_desc = request.POST['edit_desc']
    thumbnail   = request.FILES['thumbnail']
    #save the data
    profile = memberAcount.objects.filter(owner=request.user.username).update( full_name=full_name,
                                                                               contact=contact,
                                                                               short_desc=simple_desc,
                                                                               thumbnail=thumbnail
                                                                              )
    return HttpResponseRedirect('/')
       
  #not authenticated
  else:
    return HttpResponseRedirect("/")
###########################################################################################################S  



########################################################################
def user_search(request):
  #authenticated
  if request.user.is_authenticated():
    #get the query
    query = request.GET['username']
    #initialize  form
    form = ''
    #get he users in the memberAccount
    users = memberAcount.objects.filter(username__istartswith=query)
    #create aform
    form+='<form name="ticks" id="ticks">'

    #if there user
    if users:
      #loop thru the ticks
      for user in users:
        form+='''
                 <input type="checkbox" onchange="iaddon();" name="unread" value="%s">
                 Name:&nbsp;&nbsp;%s<br />
                 '''%(user.username, user.full_name)
         #if the user has a description        
        if not user.short_desc:
          form+='Member of:&nbsp;&nbsp; <em id="res">%s</em> &nbsp; organization.<br />'%(user.owner)             
          form+="<em id='res'>____________________________________________________________________________</em>"
        #no description
        else:
          form+="<em id='res'>%s</em><br />"%(user.short_desc)
          form+="<em id='res'>____________________________________________________________________________</em>"
      form+='</form>'
      #return the form
      return HttpResponse(form)
    #no users
    else: 
      return HttpResponse('<em id="err">No user by that name!</em>')
  #not authenticated
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")
########################################################################
