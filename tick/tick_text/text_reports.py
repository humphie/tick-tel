from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from tick.models import Report 
import csv

#function to retreive reports
def report_search(request):
  # check if the user is authenticated
  if request.user.is_authenticated():
    #get the date
    date = request.GET['date']
    #check if the date is empty
    if date == "":
      #get evry instance
      reports = Report.objects.filter(username=request.user.username)
    #date is not empty  
    else:
      reports = Report.objects.filter(username=request.user.username, date=date)
    
    #iterate thru the phone_numbers and send the info to the user
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=numbers.csv'
    writer = csv.writer(response)
    writer.writerow([u'%s reports(s)'%(reports.count()), u'on your account.'])
    writer.writerow([u'________________________________________________', u'___<br />'])
    #send the response
    if reports:
      #for loop to loop thru the phone numbers
      for report in reports:
        writer.writerow([u'Date:', u'%s<br />'%(report.date)])
        writer.writerow([u'Sender:', u'%s<br />'%(report.name)])
        writer.writerow([u'Message:', u'%s<br />'%(report.message)])
        writer.writerow([u'Number of recipients:', u'%s<br /><br />'%(report.recip_num)])
      #return the response
      return response
      
    #if no reports found
    else:
      writer.writerow([u'No message has been sent yet', u'from your account.'])
      #return the response
      return response
    
  #user not authenticated
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You must be logged in, click here!</a></em>")
    
    
    
#view to delete a report
def report_delete(request):
  #if user is authenticated
  if request.user.is_authenticated():
    #get the day from the request
    date = request.GET['date']
    #try statment to get the report and delete them
    try:
      # check it the request is from an admin
      user_request = User.objects.get(username=request.user)
      #get the report of that day
      report = Report.objects.filter(username=request.user.username, date=date).delete()
      #return a success message
      return HttpResponse("<em id='res'>The report(s) on %s have been deleted</em>"%(date))
    
    #if the report do nt exist
    except:
      #sendt an erro message
      return HttpResponse("<em id='err'>Report was not deleted, check your date format</em>")  
  #user not authenticated
  else:
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>You must be logged in, click here!</a></em>")
