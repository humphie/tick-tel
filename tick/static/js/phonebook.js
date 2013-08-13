//network error message
var errorMsg = "<em id='err'>A network connection can not be established, please try again later!</em>";
//empty feilds message
var emptyFields = "<em id='err'>All fields must be filled in!</em>";


//phone contactber delete
function  deleteContact()
{
  var name = document.contact_deleteForm.name.value
  
  if(name == "")
  {
     //display the respose div
     document.getElementById("Response_Phonebook").style.display = 'block';
     //append the result in the search div
     document.getElementById("Response_Phonebook").innerHTML=emptyFields;
     return false;
  }
//send the dater to the server
  else{
  
 //check if there is aconnection
     if(window.navigator.onLine)
     {
     
         var xmlhttp;
         if (window.XMLHttpRequest)
          {
             xmlhttp=new XMLHttpRequest();
          }
        else
         {
          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
         
         }

          xmlhttp.onreadystatechange=function()
            {
               if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {
                 //display the respose div
                document.getElementById("Response_Phonebook").style.display = 'block';
                //append the result in the search div
                document.getElementById("Response_Phonebook").innerHTML=xmlhttp.responseText;
                //set the syncSignal to true
                document.getElementById("syncSignal").value = 'true';
                //reset the form
                document.getElementById("contact_deleteForm").reset();
                //display the updated list
                getNumbers();
            }
          }
            data = "?name=" +name
            xmlhttp.open("GET","/number_delete/"+data,true);
            xmlhttp.send();

     
     }
   //no network connection
     else
     {
      //dispay the loading image
      document.getElementById('contact_search_result').innerHTML = '<img src="/static/images/Loader.gif" />';
      //display the respose div
      document.getElementById("Response_Phonebook").style.display = 'block';
      //append the result in the search div
      document.getElementById("Response_Phonebook").innerHTML=errorMsg;
      return false;
     }   
 //end of checking network connection 
  }

}
//end of the delete



//function to edit the contact
function editContact()
{
   var name    = document.contact_editForm.name.value
   var contact = document.contact_editForm.contact.value
   var group   = document.contact_editForm.group.value
   
   if(name == "" || contact == "" || group == "")
   {
     //display the respose div
     document.getElementById("Response_Phonebook").style.display = 'block';
     //append the result in the search div
     document.getElementById("Response_Phonebook").innerHTML=emptyFields;
     return false;
   }
   else
   {
   
//check the network connection
     if(window.navigator.onLine)
      {
         var xmlhttp;
         if (window.XMLHttpRequest)
          {
             xmlhttp=new XMLHttpRequest();
          }
       else
         {
          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
         
        }

          xmlhttp.onreadystatechange=function()
            {
               if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {
                 //display the respose div
                document.getElementById("Response_Phonebook").style.display = 'block';
                //append the result in the search div
                document.getElementById("Response_Phonebook").innerHTML=xmlhttp.responseText;
                //set the syncSignal to true
                document.getElementById("syncSignal").value = 'true';
                //reset the form
                document.getElementById("contact_editForm").reset();
                //display the updated list
                getNumbers();
            }
          }
            data = "?name=" +name+ "&contact_number=" +contact+ "&group=" +group
            xmlhttp.open("GET","/contact_edit/"+data,true);
            xmlhttp.send();
      }
//no network connection
   else
    {
      //dispay the loading image
      document.getElementById('contact_search_result').innerHTML = '<img src="/static/images/Loader.gif" />';
      //display the respose div
      document.getElementById("Response_Phonebook").style.display = 'block';
      //append the result in the search div
      document.getElementById("Response_Phonebook").innerHTML=errorMsg;
      return false;
   
    }
   
   }
}
//end of the edit contact form  



//function to save aphonecontactber
function saveValidate()
{
   var name    = document.contact_saveForm.name.value
   var contact = document.contact_saveForm.contact.value
   var group   = document.contact_saveForm.group.value
   
   if(name == "" || contact == "" || group == "")
   {
     //display the respose div
     document.getElementById("Response_Phonebook").style.display = 'block';
     //append the result in the search div
     document.getElementById("Response_Phonebook").innerHTML=emptyFields;
     return false;

   }
   else
   {
   
//check the network connection
     if(window.navigator.onLine)
      {
         var xmlhttp;
         if (window.XMLHttpRequest)
          {
             xmlhttp=new XMLHttpRequest();
          }
       else
         {
          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
         
        }

          xmlhttp.onreadystatechange=function()
            {
               if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {
                 //display the respose div
                document.getElementById("Response_Phonebook").style.display = 'block';
                //append the result in the search div
                document.getElementById("Response_Phonebook").innerHTML=xmlhttp.responseText;
                //set the syncSignal to true
                document.getElementById("syncSignal").value = 'true';
                //reset the form
                document.getElementById("contact_saveForm").reset()
                //display the updated list
                getNumbers();
                
            }
          }
            data = "?name=" +name+ "&contact_number=" +contact+ "&group=" +group
            xmlhttp.open("GET","/save/"+data,true);
            xmlhttp.send();
      }
//no network connection
   else
    {
      //dispay the loading image
      document.getElementById('contact_search_result').innerHTML = '<img src="/static/images/Loader.gif" />';
      //display the respose div
      document.getElementById("Response_Phonebook").style.display = 'block';
      //append the result in the search div
      document.getElementById("Response_Phonebook").innerHTML=errorMsg;
      return false;
   
    }
   
   }

}
//end of the function



//function for the phonebook
function phonebookForm(Form){

  var group   = document.FormBook.group.value
  var message = document.FormBook.message.value

  if (group == 'Select a group:' || message == ''){
     
     //display the respose div
     document.getElementById("Response_Phonebook").style.display = 'block';
     //append the result in the search div
     document.getElementById("Response_Phonebook").innerHTML=emptyFields;
     return false;
  } 
  else
  {
  
//check for network connection
   if(window.navigator.onLine)
    {
         var xmlhttp;
    if (window.XMLHttpRequest)
      {
         xmlhttp=new XMLHttpRequest();
               }
    else
      {
          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
         
      }

       xmlhttp.onreadystatechange=function()
       {
          if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {
                   
                 //display the respose div
                document.getElementById("Response_Phonebook").style.display = 'block';
                //append the result in the search div
                document.getElementById("Response_Phonebook").innerHTML=xmlhttp.responseText;
                //reset the form
                document.getElementById("FormBook").reset()
            }
       }
    
       xmlhttp.open("GET", "/phonebook/?group="+group+"&message="+message, true);
       xmlhttp.send();
  
  
    }
//no network connection
   else
    {
      //dispay the loading image
      document.getElementById('contact_search_result').innerHTML = '<img src="/static/images/Loader.gif" />';
      //display the respose div
      document.getElementById("Response_Phonebook").style.display = 'block';
      //append the result in the search div
      document.getElementById("Response_Phonebook").innerHTML=errorMsg;
      return false;
    }
  }

}
//end of the forne book function

//phonebook search function
function searchValidate()
{
  var query = document.contact_searchForm.query.value
  
  if (query == "")
  {
     return false;
  }
  else
  {
  
//check te network connection
   if(window.navigator.onLine)
    {
       //remove the contact number div
      document.getElementById("contact_numbers").style.display = 'none';
     //display the respose div
     document.getElementById("contact_search_result").style.display = 'block';
     //dispay the loading image
     document.getElementById('contact_search_result').innerHTML = '<img src="/static/images/Loader.gif" />';

    var xmlhttp;
    if (window.XMLHttpRequest)
      {
         xmlhttp=new XMLHttpRequest();
               }
    else
      {
          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
         
      }

    xmlhttp.onreadystatechange=function()
      {
          if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {
                //append the result in the search div  
                document.getElementById("contact_search_result").innerHTML=xmlhttp.responseText;
                //reset the form
                document.getElementById("contact_searchForm").reset();
                //set the syncSignal to false
                document.getElementById("syncSignal").value = "true";
            }
      }
    
    xmlhttp.open("GET","/booksearch/?query="+query,true);
    xmlhttp.send();
    
        
    }
//no connection
   else
    {
      //dispay the loading image
      document.getElementById('contact_search_result').innerHTML = '<img src="/static/images/Loader.gif" />';
      //display the respose div
      document.getElementById("Response_Phonebook").style.display = 'block';
      //append the result in the search div
      document.getElementById("Response_Phonebook").innerHTML=errorMsg;
      return false;
    }

  
  }

}
//end of the search

//function to get the numbers
function getNumbers()
{
 //check te network connection
   if(window.navigator.onLine)
    {
    //display the respose div
    document.getElementById("contact_search_result").style.display = 'block';
    //dispay the loading image
     document.getElementById('contact_search_result').innerHTML = '<img src="/static/images/Loader.gif" />';
    var xmlhttp;
    if (window.XMLHttpRequest)
      {
         xmlhttp=new XMLHttpRequest();
               }
    else
      {
          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
         
      }

    xmlhttp.onreadystatechange=function()
      {
          if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {
                //append the response
                document.getElementById("contact_search_result").innerHTML=xmlhttp.responseText;
                //set the syncSignal to false
            }
      }
    
    xmlhttp.open("GET","/booksearch/?query=",true);
    xmlhttp.send();
    
        
    }
//no connection
   else
    {
       //dispay the loading image
      document.getElementById('contact_search_result').innerHTML = '<img src="/static/images/Loader.gif" />';
          //set timer
          setTimeout(function(){
              //display the respose div
              document.getElementById("Response_Phonebook").style.display = 'block';
              //append the result in the search div
              document.getElementById("Response_Phonebook").innerHTML=errorMsg;
          }, 3000);
       return false;
    }
 
}
