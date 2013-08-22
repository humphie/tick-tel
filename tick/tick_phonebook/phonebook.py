import csv
from tick.models import Phone, memberAcount
from tick.db_manager import *
from django.shortcuts import HttpResponse


#view for searching a contact
def book_search(request):
    
  if request.user.is_authenticated():
    #get the user input
    query = request.GET['query']
    #check if the query is empty    
    if query == "":
      search_result  = Phone.objects.filter(username=request.user)
      staff_result   = memberAcount.objects.filter(owner=request.user)
    #if query is not empty
    else:    
      search_result  = Phone.objects.filter(username=request.user, name__istartswith=query)
      staff_result   = memberAcount.objects.filter(owner=request.user, username__istartswith=query)

    #initialize the csv data format to send to the user
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=numbers.csv'
    writer = csv.writer(response)
    writer.writerow([u'%s contact(s)'%(search_result.count()+staff_result.count()), u'in your phonebook'])
    writer.writerow([u'________________________________________________', u'<br />'])
    
    #check if the search result has values
    if search_result or staff_result:
      #for loop to loop thru the phone numbers
      for result in search_result:
        writer.writerow([u'Name:', u'%s<br />'%(result.name)])
        writer.writerow([u'Contact:', u'%s<br />'%(result.contact)])
        writer.writerow([u'Email:', u'%s<br />'%(result.email)])
        writer.writerow([u'Group:', u'%s<br /><br />'%(result.group)])
      #loop thru the member account
      for result in staff_result:
        writer.writerow([u'Name:', u'%s<br />'%(result.username)])
        writer.writerow([u'Contact:', u'%s<br />'%(result.contact)])
        writer.writerow([u'Group:', u'%s<br /><br />'%(result.group)])
            
      #return the response
      return response

    else:
      writer.writerow([u'No contact in your', u'phonebook.'])        
      #return the response
      return response
    
  else:    
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>Click here to login</a></em>")




#view for editing and deleting a phone number
def contact_edit(request):

  if request.user.is_authenticated():
    #if the request is a POST
    name    = request.GET['name']
    contact = request.GET['contact_number']
    group   = request.GET['group']
    email   = request.GET['email']
    current_name = request.GET['curr_name']

    #check the group
    if group != "staff":
      #function to delete the number
      delete_a_contact(request.user.username, current_name)
      #create anew contact
      save_a_contact(request.user.username, name, group, contact, email)        
      #send response
      return HttpResponse('<em id="res">%s has been edited!</em>'%(name)) 

    #if group is staff
    else:
      return HttpResponse('<em id="err">Staff %s has not been edited. To edit go to the staff member page!</em>'%(name)) 

  else:    
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>Click here to login</a></em>")
#end of the edit view




#view for deleting a number
def delete(request):

  if request.user.is_authenticated():
    
    name = request.GET['name']            
    
    #try statment to check if its the staff member
    try: 
      #function to delete the number
      delete_a_contact(request.user.username, name)    
      return HttpResponse('<em id="res">%s has been deleted!</em>'%(name))     
    #user is a staff member
    except:
      return HttpResponse('''
                     <em id="err">%s has not been deleted! Perform this action from the Staff Member page!</em>
                      '''%(name))     
  #user not authenticated
  else:    
    return HttpResponse("<em id='err'><a href='#!/page_Login' id='err'>Click here to login</a></em>")

#end of the delete view

    


#view for the send
def save(request):

  if request.user.is_authenticated():
       
    name    = request.GET['name']
    contact = request.GET['contact_number']
    group   = request.GET['group']
    email   = request.GET['email']
        
           
    #call save the contact method
    save_a_contact(request.user.username, name, group, contact, email)        
            
    #send response
    return HttpResponse('<em id="res">%s has been saved!</em>'%(name))
            
        
        #method not authenticated
  else:
    #send response
    return HttpResponse('<em id="err"><a href="#!/page_Login" id="err">Click here to login</a></em>')

