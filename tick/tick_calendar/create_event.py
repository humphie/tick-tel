import csv
from tick.db_manager import *
from django.shortcuts import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

#create an event
def calendar_create_event(request):
  # if the user is authenticated
  if request.user.is_authenticated():
    
    event_title       = request.GET['title']
    event_description = request.GET['description']
    event_priority    = request.GET['priority']
    event_type        = request.GET['event_type']
    contacts          = request.GET['numbers']
    day               = request.GET['day']
    month             = request.GET['month']
    year              = request.GET['year']
   
    #call the create_event method here in atry statment
    try:
      # set the date format
      date='%s-%s-%s'%(year, month, day)
      #call the methos to save the date
      create_a_calendar_event(request.user.username, event_title, date, event_description, event_priority, event_type, contacts)       
      #return a success method
      return HttpResponse("<em id='res'>Event '%s' has been saved!</em>"%(event_title))
    #if an error occurs
    except:
      return HttpResponse("<em id='err'>Event '%s' has not been saved, try again later!</em>"%(event_title))
      
  #if user is not logged in  
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")
#####################################################################    


#method to delete an event    
def delete_event(request):
  if request.user.is_authenticated():
  
    event_title = request.GET['event_title']
    
    #call the dlete metod here
    delete_an_event(request.user.username, event_title)
    
    return HttpResponse("<em id='res'>Event '%s' has been deleted!</em>"%(event_title))
  
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")
################################################################################    


#view to edit an event
def edit_an_event(request):
  if request.user.is_authenticated():
    
    event_title       = request.GET['title']
    event_description = request.GET['description']
    event_priority    = request.GET['priority']
    event_type        = request.GET['event_type']
    contacts          = request.GET['numbers']
    day               = request.GET['day']
    month             = request.GET['month']
    year              = request.GET['year']
    
    # set the date format
    date='%s-%s-%s'%(year, month, day) 
    
    #delete the event 1st
    delete_an_event(request.user.username, event_title)

    #create a new event
    create_a_calendar_event(request.user.username, event_title, date, event_description, event_priority, event_type, contacts)
    
    return HttpResponse("<em id='res'>Event '%s' has been edited!</em>"%(event_title))   

  #user not authenticated
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You are logged out, click here to proceed!</a></em>")
    
################################################################################################################    


#search an event
def date_search(request):
  if request.user.is_authenticated():
    
    day   = request.GET['day']
    month = request.GET['month']
    year  = request.GET['year']
    
    #set the date formay
    date = '%s-%s-%s'%(year, month, day)
    
    #check for the date in the db
    events = Event.objects.filter(owner=request.user, date=date)
    #initialize the data format to send to the user
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=events.csv'
    writer = csv.writer(response)
    writer.writerow([u'%s Events(s)'%(events.count()), u'set for %s.<br />'%(date)])
    writer.writerow([u'_________________________________', u'_<br />'])
    
    #if the event query has events
    if events:
      #loop thru the events
      for event in events:
        writer.writerow([u'Title:', u'%s<br />'%(event.event_title)])
        writer.writerow([u'Description:', u'%s<br />'%(event.description)])
        writer.writerow([u'Priority:', u'%s<br /><br />'%(event.priority)])
      #return the events on that date
      return response
      
      
    #there is no event
    else:
      writer.writerow([u'No event on %s,'%(date), u'click on the date to set an event!'])
      #return the events on that date
      return response

  #user no authenticated
  else:    
    return HttpResponse("""<em>
                          <a href='#!/page_Login' id='err'>Sorry you are logged out,
                          please Click here to login!</a>
                          </em>""")
###################################################################################
