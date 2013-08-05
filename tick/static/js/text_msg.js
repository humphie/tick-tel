//network error message
var errorMsg = "<em id='err'>A network connection can not be established, please try again later!</em>";
//empty feilds message
var emptyFields = "<em id='err'>All fields must be filled in!</em>";

//texting function
function TextForm()
{
name    = document.textForm.name.value
contact = document.textForm.contacts.value
message = document.textForm.message.value

if(name == "" || contact == "" || message == "")
    {
        
        //send the error msg   
        document.getElementById("send_Response").innerHTML=emptyFields;
        return false;
   }

  else
   {
   
   //check network connection
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
                //send the response msg   
                document.getElementById("send_Response").innerHTML=xmlhttp.responseText;
//                alert(xmlhttp.responseText);
                //reset the form
                document.getElementById("textForm").reset()
                //get the updated report
                get_report("");
                
                
            }
      }
    data = "?name=" +name+ "&contact="+contact+ "&message=" +message
    xmlhttp.open("GET","/text_msging/"+data,true);
    xmlhttp.send();   

   
   }
   else
   {
     //display the loading image
      document.getElementById('send_Response').innerHTML = '<img src="/static/images/Loader.gif" />';
      //set timer
       setTimeout(function(){
        //dispay the empty fields message
        document.getElementById("send_Response").innerHTML=errorMsg;
      }, 3000);
      return false;

    }
  }
}
//end of the texting function

//function to fet all the reports
function get_report(date){
 
   //check network connection
   if(window.navigator.onLine)
   {
     //display the loading image
      document.getElementById('msg_report').innerHTML = '<img src="/static/images/Loader.gif" />';
   
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
                //send the response msg   
                document.getElementById("msg_report").innerHTML=xmlhttp.responseText;
            }
      }
    xmlhttp.open("GET","/report_search/?date="+date,true);
    xmlhttp.send();   

   
   }
   else
   {
     //display the loading image
      document.getElementById('send_Response').innerHTML = '<img src="/static/images/Loader.gif" />';
      //set timer
       setTimeout(function(){
        //dispay the empty fields message
        //send the error msg   
        document.getElementById("send_Response").innerHTML=errorMsg;
      }, 3000);
      return false;

    }
 

}
//end of the report functhon



//function to search for areport
function report_search()
{
  //get te date
  var date = document.report_searchForm.report_query.value
  if (date != ""){get_report(date); document.report_searchForm.reset();}
}
//end of the report seach function



//report delete
function deleteform(){

  var date = document.report_deleteForm.report_query.value

 if (date != "")
 {
 
     //check network connection
   if(window.navigator.onLine)
   {
     //display the loading image
      document.getElementById('msg_report').innerHTML = '<img src="/static/images/Loader.gif" />';

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
                //send the response msg   
                document.getElementById("send_Response").innerHTML=xmlhttp.responseText;
                //reset the delete form
                document.report_deleteForm.reset();
                //show the updated report
                drawDiv('msg_report');
            }
      }
    xmlhttp.open("GET","/report_delete/?date="+date,true);
    xmlhttp.send();   
   
   }
   else
   {
     //display the loading image
      document.getElementById('send_Response').innerHTML = '<img src="/static/images/Loader.gif" />';
      //set timer
       setTimeout(function(){
        //dispay the empty fields message
        //send the error msg   
        document.getElementById("send_Response").innerHTML=errorMsg;
      }, 3000);
      return false;

    }
 
 }
 //date field is empty
 else
 {
  //remove the testinf form
 document.getElementById("texting").style.display = "none";
 //display the delete form
 document.getElementById("delete_report").style.display = "block";
 
 } 
}
//end of report delete
