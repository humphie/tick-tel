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
      current_acc_type = memberAcount.objects.get(username=request.user.username)
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
        return HttpResponse("<em id='res'>Your account has been changed successfuly.<a href='/private_user/'>Click here to continue!</a></em>")
      
      #account type is private
      elif current_acc_type.acc_type == "private" and acc_type == "public":
        #update the account cow
        new_account = memberAcount.objects.filter(owner=request.user.username).update(acc_type=acc_type)
        #send a success message
        return HttpResponse("<em id='res'>Your account has been changed successfuly.<a href='/super_user/'>Click here to continue!</a></em>")
      
      
      #acount is not defined
      else:
        return HttpResponse("<em id='err'>There is nothing to be changed!!</em>")
    #the request is epmty
    else:
      return HttpResponse("<h1 id='err'>Hacker????????????????</h1>")  
  #not authenticated
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")
################################################################################



#method to change the password
def change_password(request):
  #check if the user is authenticated
  if request.user.is_authenticated():
    #get the paswords
    password = request.GET['password']
    username = request.GET['Username']
    #a try styatment to check if the user is an admin or staff
    try:
      #get the user and change the password
      new_password = User.objects.get(username__exact=username)
      new_password.set_password(password)
      new_password.save()
      #also change the password in the membersAccount
      staff = memberAcount.objects.filter(username=username).update(password=password)
      #redierect to the home page
      return HttpResponse("<em id='res'>Your password has been changed successfuly.<a href='/'>Click here to continue!</a></em>")
    #user is not in the main table
    except User.DoesNotExist:
      #get the username of the user
      staff = memberAcount.objects.filter(username=username).update(password=password)
      #redierect to the home page
      return HttpResponse("<em id='res'>Your password has been changed successfuly.<a href='/'>Click here to continue!</a></em>")
    
    #none of the above
    else:
      #
      return HttpResponse("<em id='err'><a id='err' href='/'>Hacker????????????????????</a></em>")
      
      
    #none og the above  
  #not authenticated
  else:
    return HttpResponseRedirect("/")
################################################################################  




#method to change the account type
def profile_edit(request):
  #check if the user is authenticated
  if request.user.is_authenticated():
    #get the user data
    username    = request.POST['Username']
    full_name   = request.POST['edit_full_name']
    contact     = request.POST['edit_contact']
    simple_desc = request.POST['edit_desc']
    thumbnail   = request.FILES['thumbnail']
    #save the data
    profile = memberAcount.objects.filter(username=username).update( full_name=full_name,
                                                                      contact=contact,
                                                                      short_desc=simple_desc,
                                                                      thumbnail=thumbnail
                                                                    )
    return HttpResponseRedirect('/')
       
  #not authenticated
  else:
    return HttpResponseRedirect("/")
################################################################################  



################################################################################
def user_search(request):
  #authenticated
  if request.user.is_authenticated():
    #get the query
    query = request.GET['username']
    #initialize  form
    form = ''
    #get he users in the memberAccount
    users = memberAcount.objects.filter(username__istartswith=query)
    form+="""
     <form name="user_search_form" id="user_search_form">
       <input class="form-control" id="user_query_on_fly" type="text" name="user_query" maxlength="16" placeholder="search for a friend!" />
        <img src="/static/admin/img/icon_searchbox.png"  onClick="return search_user('');"alt="Search" height="23px" width="23px" />
         </form>
      """

    #if there user
    if users:
      #loop thru the ticks
      for user in users:
        #decide which thumbnail to display
        if user.thumbnail:
          thumnail = '/static/images/profile_bg.png'
        else:        
          thumnail = '/static/images/profile_pic.png'    
        #get the name 
        if user.full_name:
          name     = '''
                        Full Name:&nbsp;&nbsp;&nbsp;%s<br />
                        Username:&nbsp;&nbsp;&nbsp;%s
                     '''%(user.full_name, user.username)
        else:
          name     = 'Username:&nbsp;&nbsp;&nbsp;%s'%(user.username)
        
        #get the short desc
        if user.short_desc:
          short_desc = """
                         About Me:&nbsp;&nbsp;&nbsp;%s<br />
                       """%(user.short_desc)
        else:
          short_desc = ""
        form+="""
                   <table>
                     <tr>
                       <td style="padding-left:10px;">
                        <img src="%s" class="img-circle">
                       </td>
     
                       <td id="info">
                           %s<br />
                           Location:&nbsp;&nbsp;%s<br />
                           %s<br /> 
                       </td>
                     </tr>
                   </table>
                 """%(thumnail, name, user.country, short_desc)
        form+="<p style=background-color:#CCFFFF;></p>"  
      #return the form
      return HttpResponse(form)
    #no users
    else:
      form+='<em id="err">No user by that name!</em>' 
      return HttpResponse(form)
  #not authenticated
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")
################################################################################
