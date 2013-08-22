'''momo 
a class to communicate with the database
'''
import datetime
from models import *
from django.contrib import auth


# the create a user view
def create_a_user(username, password, email):
  #use try statement to avoin repetition
  try:
    new_user = User.objects.get(username=username)
  #if the account does not exist  
  except User.DoesNotExist:
    new_user = User.objects.create_user(username=username, password=password, email=email) 
#end of the create a user view


#vew t create a new staff member
def new_staff_member( owner, full_name, username, password, position, contact ):
  #a try statment to create amember
  staff_member = memberAcount.objects.filter(owner=owner, full_name=full_name, password=password)
  # if the staff members is ther
  if staff_member:
    print staff_member
  #staff is not there
  else:
    staff_member  = memberAcount.objects.create(
                                                owner=owner,
                                                full_name=full_name, 
                                                username=username,
                                                password=password,
                                                position=position, 
                                                contact=contact,
                                                country='',
                                                group='staff',
                                                acc_type='public',
                                                short_desc='',
                                                thumbnail=''
                                             )


#create a staff member
def create_a_staff_member(owner, username, password, position, contact, country, group):
  #a try statment to create amember
  staff_member = memberAcount.objects.filter(owner=owner, username=username, password=password)
  # if the staff members is ther
  if staff_member:
    print staff_member
  #staff is not there
  else:
    staff_member  = memberAcount.objects.create(
                                                owner=owner,
                                                full_name='', 
                                                username=username,
                                                password=password,
                                                position=position, 
                                                contact=contact,
                                                country=country,
                                                group=group,
                                                acc_type='private',
                                                short_desc='',
                                                thumbnail=''
                                             )
#end of the create member function



#delete a staff member
def delete_staff_member(owner, username):
  #a try statment to create amember
  staff_member = memberAcount.objects.filter(owner=owner, username=username).delete()
#end of the delete member view  


#create a credit account view
def create_a_credit_account(username, credit):
  #use try statment to create astatnment
  try:
    credit_account = Credit.objects.get(name=username)
  #if the account does not axist
  except Credit.DoesNotExist:
    credit_account = Credit.objects.create(name=username, credit=credit)
#end of the create a credit account view

#credit an account 
def credit_an_acount(username, amount):
  #try statment
  try:
    actual_balance = Credit.objects.get(name=username)
    new_balance = Credit.objects.filter(name=username).update(credit=amount)

  #account does not axist
  except Credit.DoesNotExist:
    return
    
 
def credit_and_update_an_account(username, credit):
  #get the initial Credit_countaining mesages
  credit_on_the_account = Credit.objects.get(name=username)

  #get the actual balance
  balance = credit_on_the_account.credit - credit

  #update the user account!
  actual_balance = Credit.objects.filter(name=username).update(credit=balance)


def create_a_calendar_event(owner, event_title, date, description, priority, event_type, contact):
  #save in atry statment
  try:
    event = Event.object.get(event_title=event_title)
    print event.date
    print event.owner
  #if the event is anot there
  except:
    event = Event.objects.create(owner=owner, event_title=event_title, date=date, description=description, priority=priority, event_type=event_type, contact=contact)



def delete_an_event(owner, event_title):
  delete_the_event = Event.objects.filter(owner=owner, event_title=event_title).delete()
  
  
def save_a_contact(username, name, group, contact, email):
  new_contact = Phone.objects.create(username=username, 
                                     name=name,
                                     group=group, 
                                     contact=contact,
                                     email=email)


def delete_a_contact(username, name):
  print username, name
  contact = Phone.objects.filter(username=username, name=name).delete()


#make areport
def report(username, name, message, recip_num):
  print username, name, message, recip_num
  reportIt = Report.objects.create(username=username, name=name, message=message, recip_num=recip_num, date=datetime.datetime.now())
