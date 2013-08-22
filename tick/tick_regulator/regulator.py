from tick.models import *
from django.contrib.auth.models import User


################################################################################
#def send_tick(username):
################################################################################


################################################################################
def requlator(username):
  #get or create the hacker in a try statment
  try:
    #if the is there already check his/her chances and they are 0 delete all his/her instances
    hacker = Hacker.objects.get(username=username)
    #update his/her chances.
    new_chance = hacker.chance+1
    #if the new_chance == 3send_mail_tick(username)
    if new_chance == 3:
      #call the delete method here  
      delete_user_instance(username)
    #chance not equal to 3
    else:
      #update the chances 
      decreamented_chances = Hacker.objects.filter(username=username).update(chance=new_chance)
    #return
    return
    
  #hacker is new  
  except:
    #create a hacker
    hacker = Hacker.objects.create(username=username, chance=1)
    #send the harcker an message 
    send_mail_tick(username)
    return
################################################################################


################################################################################
def delete_user_instance(username):
  #super/private user
  try:
    super_private_user = User.objects.get(username=username)
  #not a super user
  except:
    staff_member = memberAcount.objects.get(username=username)

  #check wch user it is
  if super_private_user:
    #send mail first
    
    #delete credit instance
    credit = Credit.objects.filter(name=username).delete()
    #delete all phone instaces
    phonebook = Phone.objects.filter(username=username).delete()
    #all ticks received
    ticks = Inbox.objects.filter(recipient=username).delete()
    #remove every instanse in the memberAcount
    staff = memberAcount.objects.filter(owner=username).delete()
    #remove all the report
    reports = Report.objects.filter(username=username).delete()
    #remove all the events of the user
    event = Event.objects.filter(owner=username).delete()
  #user is staff
  else:
  #delete the staff member
    #send the admin a tick and an email

    #all ticks received
    ticks = Inbox.objects.filter(recipient=username).delete()
    #remove every instanse in the memberAcount
    staff = memberAcount.objects.filter(username=username).delete()
    
  return
################################################################################
