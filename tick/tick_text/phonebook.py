from tick.models import Phone
from tick.db_manager import *
from django.shortcuts import HttpResponse


#view for searching a contact
def book_search(request):
    
  if request.user.is_authenticated():
    
    query = request.GET['query']
    
    search_result  = Phone.objects.filter(name__istartswith=query, username=request.user)
    
    if search_result:
      print search_result[0].contact 
    
      return HttpResponse('<em>Name: %s<br />Number: %s<br />Group: %s<br /></em>'%(search_result[0].name, search_result[0].contact,search_result[0].group))

    else:
      return HttpResponse("<em id='err'>there is no such acontact in here.</em>")    
    
  else:    
    return HttpResponse("<em><a href='#!/page_Login' id='err'>Click here to login</a></em>")




#view for editing and deleting a phone number
def contact_edit(request):

  if request.user.is_authenticated():
    print 'logged in'
    #if the request is a POST
    name    = request.GET['name']
    contact = request.GET['contact_number']
    group   = request.GET['group']

    #function to delete the number
    delete_a_contact(request.user.username, name)

    #create anew contact
    save_a_contact(request.user.username, name, group, contact)        

    return HttpResponse('<em id="res">%s has been edited!</em>'%(name)) 

  else:    
    return HttpResponse("<em><a href='#!/page_Login' id='err'>Click here to login</a></em>")
#end of the edit view




#view for deleting a number
def delete(request):

  if request.user.is_authenticated():
    
    name = request.GET['name']            
    
    #function to delete the number
    delete_a_contact(request.user.username, name)
    
    return HttpResponse('<em id="res">%s has been deleted!</em>'%(name))     

  else:    
    return HttpResponse("<em><a href='#!/page_Login' id='err'>Click here to login</a></em>")

#end of the delete view

    


#view for the send
def save(request):

  if request.user.is_authenticated():
       
    name     = request.GET['name']
    contact  = request.GET['contact_number']
    group    = request.GET['group']
        
           
    #code to save the contact
    save_a_contact(request.user.username, name, group, contact)        
            
    #send response
    print 'saved'
    return HttpResponse('<em id="res">%s has been saved!</em>'%(name))
            
        
        #method not authenticated
  else:
    #send response
    return HttpResponse('<em><a href="#!/page_Login" id="err">Click here to login</a></em>')



#end of the save view

