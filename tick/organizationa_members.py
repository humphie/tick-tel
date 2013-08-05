import datetime
import csv
from django.contrib import auth
from django.contrib.auth.models import User
from tick.db_manager import *
from tick.models import memberAcount, Inbox
from django.shortcuts import HttpResponse



#date to day
date = datetime.datetime.today()

#welcome tick
welcome_tick = 'Hello %s, welcome to %s. For more inquries contacts the admin for help. God bless you!!'

#function to add a member
def staff_delete(request):
  #check if the user is authenticated
  if request.user.is_authenticated():
    #get the data form the request
    name = request.GET['username']
    org  = request.user.username             
    
    #check if the user is an administrator
    pozition = memberAcount.objects.filter(owner=org, username=org, position="administrator")
    #send the user to the rigt direction
    if pozition:
      #check if the request is from an admin
      user_request = User.objects.get(username=request.user)
      #delete the staff
      delete_staff_member(request.user.username, name)
      #delete all the ticks 
      ticks = Inbox.objects.filter(recipient=name).delete()
      #success message
      return HttpResponse('<em id="res">Staff %s has been removed!</em>'%(name))     

    else:
      #failure message
      return HttpResponse('<em id="err">You are not allowed to add a sfaff member!</em>')     

  else:
    return HttpResponse("<em><a href='#!/page_Login' id='err'>Click here to login</a></em>")
#and of the staff addtion view      
     



#function to add a staff member
def add_staff(request):
  #check if the user is authenticated
  if request.user.is_authenticated():
  
    #pick datsa fofrom the request
    org      = request.user.username
    full_name = request.GET['full_name']
    username = request.GET['username']
    password = request.GET['password']
    position = request.GET['position']
    contact  = request.GET['contact']

    #check if the user is an administrator
    pozition = memberAcount.objects.filter(owner=org, username=org, position="administrator")
    #send the user to the rigt direction
    if pozition:
      #create a staff
      create_a_staff_member(org, full_name, username, password, position, contact, 'staff', 'public', '')
      
      #send the staff a welcome tick
      tick = Inbox.objects.create(
                                   sender=org,
                                   recipient=username,
                                   message=welcome_tick%(username, org), 
                                   flag='un_read',
                                   date=date
                                 )
      #success message    
      return HttpResponse('''
                            <em id="res">Staff %s has been added in %s position.</em>
                          '''%(username, position))
    else:
      #failure message    
      return HttpResponse('<em id="err">You are not allowed to add a sfaff member!</em>')
 
  #if user is not authenticated
  else:
    return HttpResponse("<em><a href='#!/page_Login' id='err'>Click here to login</a></em>")
  
#and of the staff addtion view      


     
#method tho sync the members
def sync_members(request):
  #if user is authenticated
  if request.user.is_authenticated():
    #get the query from the use
    query = request.GET["query"]
    #if query is empty
    if query == "":
      #get all instances of the users members
      members = memberAcount.objects.filter(owner=request.user.username)
    else:
      members = memberAcount.objects.filter(username__istartswith=query, owner=request.user.username)

    #iterate thru the phone_numbers and send the info to the user
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=numbers.csv'
    writer = csv.writer(response)
    writer.writerow([u'%s Staff members(s)'%(members.count()), u'  in %s!<br />'%(request.user.username)])
    writer.writerow([u'_____________________________________________', u'_________<br />'])

    #use csv format to senfd the date
    if members:
      #for loop to loop thru the phone numbers
      for member in members:
        writer.writerow([u'Name:', u'%s<br />'%(member.full_name)])
        writer.writerow([u'Username:', u'%s<br />'%(member.username)])
        writer.writerow([u'Position:', u'%s<br /><br />'%(member.position)])
      #return the response
      return response

    #no search results have beem found
    else:
      writer.writerow([u'No staff member on your ', u'account!'])
      #return the response
      return response
    
  
  #if user is not authenticated
  else:
    return HttpResponse("<em><a href='#!/page_Login' id='err'>Click here to login</a></em>")


#function to get the list of staff members
def staff_list(request):
  #get all the staff members
  staffs = memberAcount.objects.filter(owner=request.user.username)
  #initialize astring
  staff_List=''
  #the form name
  staff_List+='<form name="members" id="members">'
  #iterate the staff list
  for staff in staffs:
    staff_List+='''
              <input type="checkbox" onchange="naddon();" id="member" name="member" value="%s">
              Name:&nbsp:&nbsp;&nbsp;&nbsp;%s<br />&nbsp:&nbsp;&nbsp;&nbsp;
              Username:&nbsp;&nbsp;&nbsp;%s<br />&nbsp:&nbsp;&nbsp;&nbsp;
              Position:&nbsp;&nbsp;%s <br /><br />
              '''%(staff.username, staff.full_name, staff.username, staff.position)
  staff_List+='</form>'
  return HttpResponse(staff_List)            
