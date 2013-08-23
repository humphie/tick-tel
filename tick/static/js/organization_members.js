//network error message
var errorMsg = "<em id='err'>A network connection can not be established, please try again later!</em>";
//empty feilds message
var emptyFields = "<em id='err'>All fields must be filled in!</em>";


///////////////////////////////
function naddon() {
 addon="";
 av=document.getElementsByName("member");
 for (e=0;e<av.length;e++) {
  if (av[e].checked==true) {
   addon+=av[e].value+',';
   }
  }
  return addon;
 }
//////////////////



//function to send a message
function member_chat(){

   //check if the fields are empty
   var name = naddon();
   //get the src
   var src      = document.getElementById("Username").value
   //get the message
   var message = document.staff_form.staff_text.value
   
   if (name != "" || message != "")
   {
   //check the network connection
   if(window.navigator.onLine)
    {
    //dispay the loading image
    document.getElementById('membersPage_response').innerHTML = '<img src="/static/images/Loader.gif" />';
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
                //reset the form
                document.getElementById("staff_form").reset()
                //reload the staff list 
                staff_list();                
                //append the response
                document.getElementById("membersPage_response").innerHTML=xmlhttp.responseText;
            }
      }
    data = "?name="+name+"&message="+message+ "&src="+src
    xmlhttp.open("GET","/send_tick/"+data,true);
    xmlhttp.send();
    
        
    }
   //no connection
   else
    {
       //dispay the loading image
      document.getElementById('membersPage_response').innerHTML = '<img src="/static/images/Loader.gif" />';
      //set timer
      setTimeout(function(){
              //append the result in the search div
              document.getElementById('membersPage_response').innerHTML=errorMsg;
          }, 3000);
       return false;
    }

   //fields are empty
   }
   else
   {
    //append the result in the search div
     document.getElementById('membersPage_response').innerHTML=emptyFields;
     return false;   
   }
}









//function for the organization member to login
function memberValidate()
{
  
   organization = document.Loginform.org.value
   username     = document.Loginform.username.value
   password     = document.Loginform.password.value

   if (username == "" || password == "" || organization == "")
   {
     //display the error message 
     document.getElementById("memberslogin_response").innerHTML=emptyFields;
     return false;
   }
   else{
   
   if(window.navigator.onLine)
   {
     return true;
   }
    else
   {
       //dispay the loading image
      document.getElementById('memberslogin_response').innerHTML = '<img src="/static/images/Loader.gif" />';
     //set timer
     setTimeout(function(){
    //display the error message 
     document.getElementById("memberslogin_response").innerHTML=errorMsg;
     }, 3000);
     return false;
   }
   
  }
}

//save amember
function SaveMember()
{
  
   var full_name    = document.saveMember.full_name.value
   var username     = document.saveMember.username.value
   var contact      = document.saveMember.contact.value
   var password     = document.saveMember.password.value
   var position     = document.saveMember.position.value


   if (username == "" || password == "" || position == "" || contact == "" || full_name == "")
   {
     //display the error message 
     document.getElementById("membersPage_response").innerHTML=emptyFields;
     return false;
   }
   else{
    
    
   if(window.navigator.onLine)
   {
    //dispay the loading image
    document.getElementById('membersPage_response').innerHTML = '<img src="/static/images/Loader.gif" />';
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
                //display the response message  
                document.getElementById("membersPage_response").innerHTML=xmlhttp.responseText;
                //reset the form
                document.getElementById("saveMember").reset()
                //cal the syncing function
                syncMembers("");
                
            }
      }
        data = "?username="+username+"&full_name="+full_name+"&contact="+contact+"&password="+password+ "&position="+position
        xmlhttp.open("GET","/add_staff/"+data,true);
        xmlhttp.send();
   
     }

    else
     {
       //dispay the loading image
      document.getElementById('membersPage_response').innerHTML = '<img src="/static/images/Loader.gif" />';
     //set timer
     setTimeout(function(){
     //display the error message 
     document.getElementById("membersPage_response").innerHTML=errorMsg;
     }, 3000);
     return false;
    }
   
  }

}


//function for the organization member to login
function DeleteMember()
{
  
   var username = document.deleteMember.name.value

   if (username == "" )
   {
     //display the error message 
     document.getElementById("membersPage_response").innerHTML=emptyFields;
     return false;
   }
   else{
   
   if(window.navigator.onLine)
   {
       //dispay the loading image
       document.getElementById('membersPage_response').innerHTML = '<img src="/static/images/Loader.gif" />';
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
                 //send the response message  
                document.getElementById("membersPage_response").innerHTML=xmlhttp.responseText;
                //reset the form
                document.getElementById("deleteMember").reset()
                //cal the syncing function
                syncMembers("");
            }
      }
    
    xmlhttp.open("GET","/staff_delete/?username="+username,true);
    xmlhttp.send();
   
     }

    else
     {
       //dispay the loading image
      document.getElementById('membersPage_response').innerHTML = '<img src="/static/images/Loader.gif" />';
     //set timer
     setTimeout(function(){
     //display the error message 
     document.getElementById("membersPage_response").innerHTML=errorMsg;
     }, 3000);
     return false;
    }
   
  }

}


// the syncing function to load members in case the signal is true
function syncMembers(query)
{
   if(window.navigator.onLine)
   {
     //dispay the loading image
     document.getElementById('members').innerHTML = '<img src="/static/images/Loader.gif" />';
    
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
                //reset the form
                document.getElementById("member_searchForm").reset();
                //display the response message  
                document.getElementById("members").innerHTML=xmlhttp.responseText;
                
            }
      }
        xmlhttp.open("GET","/sync_members/?query="+query,true);
        xmlhttp.send();
   
     }

    else
     {
       //dispay the loading image
      document.getElementById('membersPage_response').innerHTML = '<img src="/static/images/Loader.gif" />';
     //set timer
     setTimeout(function(){
     //display the error message 
     document.getElementById("membersPage_response").innerHTML=errorMsg;
     }, 3000);
     return false;
    }

}


//function to search aphonenumber
function searchMembers()
{
  //get the search query
  var query = document.member_searchForm.mem_query.value;
  
  if (query != ""){
    //get the search result
    syncMembers(query);
   }
}


//function for member list
function staff_list()
{

   if(window.navigator.onLine)
   {
     //dispay the loading image
     document.getElementById('members').innerHTML = '<img src="/static/images/Loader.gif" />';
    
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
                //reset the form
                document.getElementById("member_searchForm").reset();
                //display the response message  
                document.getElementById("members").innerHTML=xmlhttp.responseText;
                
            }
      }
        xmlhttp.open("GET","/staff_list/",true);
        xmlhttp.send();
   
     }

    else
     {
       //dispay the loading image
      document.getElementById('membersPage_response').innerHTML = '<img src="/static/images/Loader.gif" />';
     //set timer
     setTimeout(function(){
     //display the error message 
     document.getElementById("membersPage_response").innerHTML=errorMsg;
     }, 3000);
     return false;
    }
}
