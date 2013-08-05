

function CreateEvent(){

  event_title       = document.eventForm.event_title.value
  event_description = document.eventForm.description.value
  event_priority    = document.eventForm.priority.value
  event_type        = document.eventForm.event_type.value
  event_date        = document.eventForm.date.value
  
  
 if(event_title == "" || event_description == "" || event_priority == "" ||event_type == "" || event_date == "")
  {
  alert("All feilds must be filled in!");
      return false;
  }
  
  else{
  
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
                   
                document.getElementById("saveRes").innerHTML=xmlhttp.responseText;
                document.getElementById("eventForm").reset()
                
            }
      }
    data = "?title=" +event_title+ "&description=" +event_description+ "&priority=" +event_priority+ "&event_type="+event_type+ "&date="+event_date
    xmlhttp.open("GET","/create_event/"+data,true);
    xmlhttp.send();
 
    }
//no network connection
   else
    {
//check to see if the browser supports localStorage
     if(localStorage){
     
       alert("A network connection can not be established, but we hav saved the data!");
     
     }else{
       alert("A network connection can not be established, please try again later!");
       return false;
     }//no support for local storage
    }//no network
  
  }

}


//function to delete an event
function deleteEvent()
{

var event_title = document.deleteForm.event_title.value

  if(event_title == ""){

    

    alert("The Event Title must be filled out pliz!");
    return false; 

  }
//submited an empty form
  else
  {

   //check the network conection  
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
                   
                document.getElementById("delRes").innerHTML=xmlhttp.responseText;
                document.getElementById("deleteForm").reset()
                
            }
          }
           data = "?event_title="+event_title
           xmlhttp.open("GET","/delete_event/"+data,true);
           xmlhttp.send();
     
      }
  //no network connection
    else
    {
      alert('A network connection can not be established, try again later!');
      return false;
    }
 
  }
}


//function to edit an event
function editEvent()
{

  event_title       = document.eventForm.event_title.value
  event_description = document.eventForm.description.value
  event_priority    = document.eventForm.priority.value
  event_type        = document.eventForm.event_type.value
  event_date        = document.eventForm.event_date.value
  
  
 if(event_title == "" || event_description == "" || event_priority == "" || event_type == "" || event_date == "")
  {
  alert("All feilds must be filled in!");
      return false;
  }
  
  else{
  
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
                   
                document.getElementById("editRes").innerHTML=xmlhttp.responseText;
                document.getElementById("editForm").reset()
                
            }
      }
    data = "?title=" +event_title+ "&description=" +event_description+ "&priority=" +event_priority+ "&event_type="+event_type+ "&date="+event_date
    xmlhttp.open("GET","/edit_event/"+data,true);
    xmlhttp.send();
 
    }
//no network connection
   else
    {
       alert("A network connection can not be established, please try again later!");
       return false;
    }//no network
  
  }

}
