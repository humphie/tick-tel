//network error message
var errorMsg = "<em id='err'>A network connection can not be established, please try again later!</em>";
//empty feilds message
var emptyFields = "<em id='err'>All fields must be filled in!</em>";



function display(obj ,type) {
txt = obj.options[obj.selectedIndex].value;
document.getElementById(type).style.display = 'none';

  if ( txt.match(type) ) 
  {
      document.getElementById(type).style.display = 'block';
  } 
}


//create an event
function CreateEvent(){

  var event_title       = document.event_createForm.event_title.value
  var event_description = document.event_createForm.description.value
  var event_priority    = document.event_createForm.priority.value
  var event_type        = document.event_createForm.event_type.value
  var numbers           = document.event_createForm.numbers.value
  var day               = document.getElementById("day_selected").value
  var month             = document.frmCalendarSample.tbSelMonth.value
  var year              = document.frmCalendarSample.tbSelYear.value


 if(event_title == "" || event_description == "" || event_priority == "Please select:" || event_type == "Please select:")
  {
     //display the respose div
     document.getElementById("Response_Calendar").style.display = 'block';
     //append the result in the search div
     document.getElementById("Response_Calendar").innerHTML=emptyFields;
     return false;
  }
  
  else{
  
//check for network connection
   if(window.navigator.onLine)
    {
       //display the response message div 
       document.getElementById("Response_Calendar").style.display = 'block';
       //dispay the loading image
       document.getElementById('Response_Calendar').innerHTML = '<img src="/static/images/Loader.gif" />';
 
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
                //append the response message here   
                document.getElementById("Response_Calendar").innerHTML=xmlhttp.responseText;
                //reset the save form
                document.getElementById("event_createForm").reset();
                
            }
      }
    data = "?title="+event_title+ "&description="+event_description+ "&priority="+event_priority+ "&event_type="+event_type+ "&date="+day+ "&numbers="+numbers+ "&day="+day+ "&month="+month+ "&year="+year
    xmlhttp.open("GET","/create_event/"+data,true);
    xmlhttp.send();
 
    }
//no network connection
   else{
     //display the response div 
     document.getElementById("Response_Calendar").style.display = 'block';
     //dispay the loading image
     document.getElementById('Response_Calendar').innerHTML = '<img src="/static/images/Loader.gif" />';
     //set timer
     setTimeout(function(){
        //append the result in the search div
         document.getElementById("Response_Calendar").innerHTML=errorMsg;
      }, 3000);
     return false;

   }
  
  }

}


//function to delete an event
function deleteEvent()
{

var event_title = document.event_deleteForm.event_title.value

  if(event_title == ""){

     //display the respose div
     document.getElementById("Response_Calendar").style.display = 'block';
     //append the result in the search div
     document.getElementById("Response_Calendar").innerHTML=emptyFields;
     return false;

  }
//submited an empty form
  else
  {

   //check the network conection  
     if(window.navigator.onLine)
     {
       //dispay the loading image
       document.getElementById('Response_Calendar').innerHTML = '<img src="/static/images/Loader.gif" />';
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
                //display the response div
                document.getElementById("Response_Calendar").style.display = 'block';
                //append the message   
                document.getElementById("Response_Calendar").innerHTML=xmlhttp.responseText;
                //reset the form
                document.getElementById("event_deleteForm").reset();
            }
          }
           data = "?event_title="+event_title
           xmlhttp.open("GET","/delete_event/"+data,true);
           xmlhttp.send();
     
      }
  //no network connection
    else
    {
     //display the response div 
     document.getElementById("Response_Calendar").style.display = 'block';
     //dispay the loading image
     document.getElementById('Response_Calendar').innerHTML = '<img src="/static/images/Loader.gif" />';
     //set timer
     setTimeout(function(){
        //append the result in the search div
         document.getElementById("Response_Calendar").innerHTML=errorMsg;
      }, 3000);
     return false;
    }
 
  }
}


function displayDate(day){
   var timer;
   var el = document.getElementById('day');

   el.onmouseover = function(){
     timer = setTimeout(function(){
            searchEvent(day);
       }, 2000);
     }

  el.onmouseout = function(){
        clearTimeout(timer);
     }
} 

//phonebook search function
function searchEvent(day)
{

  var month = document.frmCalendarSample.tbSelMonth.value
  var year  = document.frmCalendarSample.tbSelYear.value

  
  if (day == "")
  {
     //display the respose div
     document.getElementById("Response_Calendar").style.display = 'block';
     //append the result in the search div
     document.getElementById("Response_Calendar").innerHTML="<em id='err'>No date selected!</em>";
     return false;
  }
  else
  {
    
//check te network connection
   if(window.navigator.onLine)
    {
       //clear the caledar page
       clearAll('calendar');
       //display the right div 
       document.getElementById("calendar").style.display = 'block';
       //display the search result div 
       document.getElementById("searchResult").style.display = 'block';
       //dispay the loading image
       document.getElementById('searchResult').innerHTML = '<img src="/static/images/Loader.gif" />';
  
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
                document.getElementById("searchResult").innerHTML=xmlhttp.responseText;
                //display the links
                if (!xmlhttp.responseText.match("click"))
                {
                document.getElementById("links_2").style.display = 'block';
                }
                               
            }
      }
    //send day, month and year to the server
    data = "?day="+day+'&month='+month+'&year='+year
    xmlhttp.open("GET","/date_search/"+data,true);
    xmlhttp.send();
    
        
    }
//no connection
   else
    {
     //display the response div 
     document.getElementById("Response_Calendar").style.display = 'block';
     //dispay the loading image
     document.getElementById('Response_Calendar').innerHTML = '<img src="/static/images/Loader.gif" />';
     //set timer
     setTimeout(function(){
        //append the result in the search div
         document.getElementById("Response_Calendar").innerHTML=errorMsg;
      }, 3000);
     return false;
    }

  
  }

}
//end of the search



//function to edit an event
function editEvent()
{

  var event_title       = document.event_editForm.event_title.value
  var event_description = document.event_editForm.description.value
  var event_priority    = document.event_editForm.priority.value
  var event_type        = document.event_editForm.event_type.value
  var numbers           = document.event_editForm.numbers.value
  var day               = document.getElementById("day_selected").value
  var month             = document.frmCalendarSample.tbSelMonth.value
  var year              = document.frmCalendarSample.tbSelYear.value

  
 if(event_title == "" || event_description == "" || event_priority == "Please select:" || event_type == "Please select:" || day == "")
  {
     //display the respose div
     document.getElementById("Response_Calendar").style.display = 'block';
     //append the result in the search div
     document.getElementById("Response_Calendar").innerHTML=emptyFields;
     return false;
  }
  
  else{
  
//check for network connection
   if(window.navigator.onLine)
    {
       //dispay the loading image
       document.getElementById('Response_Calendar').innerHTML = '<img src="/static/images/Loader.gif" />';
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
                //display response div
                document.getElementById("Response_Calendar").style.display = 'block';
                //append the response
                document.getElementById("Response_Calendar").innerHTML=xmlhttp.responseText;
                //reset the edit form
                document.getElementById("event_editForm").reset()
                //clear the page
                clearAll("calendar");
            }
      }
    data = "?title="+event_title+ "&description="+event_description+ "&priority="+event_priority+ "&event_type="+event_type+ "&date="+day+ "&numbers="+numbers+ "&day="+day+ "&month="+month+ "&year="+year
    xmlhttp.open("GET","/edit_event/"+data,true);
    xmlhttp.send();
 
    }
//no network connection
   else
    {
     //display the response div 
     document.getElementById("Response_Calendar").style.display = 'block';
     //dispay the loading image
     document.getElementById('Response_Calendar').innerHTML = '<img src="/static/images/Loader.gif" />';
     //set timer
     setTimeout(function(){
        //append the result in the search div
         document.getElementById("Response_Calendar").innerHTML=errorMsg;
      }, 3000);
     return false;
    }//no network
  
  }

}
