///////////////////////////get the selected tick//////////////////////////////////////
function iaddon() {
 addon="";
 av=document.getElementsByName("unread");
 for (e=0;e<av.length;e++) {
  if (av[e].checked==true) {
   addon+=av[e].value;
   addon+=',';
   }
  }
  return addon;
 }

function zaddon() {
 zddon="";
 av=document.getElementsByName("read");
 for (e=0;e<av.length;e++) {
  if (av[e].checked==true) {
   zddon+=av[e].value;
   zddon+=',';
   }
  }
  return zddon;
 }
 
////////////////////////////////////////////////////////////////////////////////////



//function to get all tick
function sync_ticks(flag)
{
   //get the src
   var src = document.reply_form.Username.value
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
          //remove the intro div
          document.getElementById('all_ticks').style.display = 'none';
          //remove the intro div
          document.getElementById('inbox_unread').style.display = 'block';
          //append the response
          document.getElementById("inbox_unread").innerHTML=xmlhttp.responseText;
        }
      }

    data = "?src="+src+'&flag='+flag 
    xmlhttp.open("GET","/Sync_ticks/"+data,true);
    xmlhttp.send();
    
        
    }
   //no connection
   else
    {
      //append the result in the search div
      document.getElementById('chat_res').innerHTML="<em id='err'>No network connection. Tick can't sync your inbox_unread!</em>";
      return false;
    }
}



//function to send a message
function send_chat(){

   //check if the fields are empty
   var name    = document.form_tick.username.value
   var message = document.form_tick.tick_chat.value
   
   if (name != "" || message != "")
   {
   //check the network connection
   if(window.navigator.onLine)
    {
    //dispay the loading image
    document.getElementById('chat_res').innerHTML = '<img src="/static/images/Loader.gif" />';
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
                document.getElementById('form_tick').reset();
                //append the response
                document.getElementById("chat_res").innerHTML=xmlhttp.responseText;
               //sync the inbox_unread
                sync_ticks('un_read');
            }
      }
    data = "?name="+name+"&message="+message
    xmlhttp.open("GET","/send_tick/"+data,true);
    xmlhttp.send();
    
        
    }
   //no connection
   else
    {
       //dispay the loading image
      document.getElementById('chat_res').innerHTML = '<img src="/static/images/Loader.gif" />';
      //set timer
      setTimeout(function(){
              //append the result in the search div
              document.getElementById('chat_res').innerHTML=errorMsg;
          }, 3000);
       return false;
    }

   //fields are empty
   }
   else
   {
    //append the result in the search div
     document.getElementById('chat_res').innerHTML=emptyFields;
     return false;   
   }
}




//function to reply a tick
function reply_tick()
{
    //get the selectes check boxes
    var id = iaddon();
   //get the message
   var message = document.reply_form.tick_reply.value
   //ge the src
   var src = document.reply_form.Username.value

   if (message.length != 0 )
   {
   //check the network connection
   if(window.navigator.onLine)
    {
    //dispay the loading image
    document.getElementById('chat_res').innerHTML = '<img src="/static/images/Loader.gif" />';
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
                document.getElementById('reply_form').reset();
                //append the response
                document.getElementById("chat_res").innerHTML=xmlhttp.responseText;
               //sync the inbox_unread
                sync_ticks('un_read');
             }
      }
    data = "?id="+id+"&message="+message+"&src="+src
    xmlhttp.open("GET","/reply_tick/"+data,true);
    xmlhttp.send();
    
        
    }
   //no connection
   else
    {
       //dispay the loading image
      document.getElementById('chat_res').innerHTML = '<img src="/static/images/Loader.gif" />';
      //set timer
      setTimeout(function(){
              //append the result in the search div
              document.getElementById('chat_res').innerHTML=errorMsg;
          }, 3000);
       return false;
    }

   //fields are empty
   }
   else
   {
    //append the result in the search div
     document.getElementById('chat_res').innerHTML=emptyFields;
     return false;   
   }
}




//delete message
function chat_delete()
{
   //get the id value to delete
   var Id = '';
   
   //check the flag of the message
   id1 = iaddon();
   id2 = zaddon();
   //join the inbox_unread   
   Id = id1 + id2
   if (Id != "")
   {
   //check the network connection
   if(window.navigator.onLine)
    {
    //dispay the loading image
    document.getElementById('chat_res').innerHTML = '<img src="/static/images/Loader.gif" />';
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
                document.getElementById("chat_res").innerHTML=xmlhttp.responseText;
               //sync the inbox_unread
                sync_ticks('all');
            }
      }
    xmlhttp.open("GET","/tick_delete/?id="+Id,true);
    xmlhttp.send();
    
        
    }
   //no connection
   else
    {
       //dispay the loading image
      document.getElementById('chat_res').innerHTML = '<img src="/static/images/Loader.gif" />';
      //set timer
      setTimeout(function(){
            //append the result in the search div
            document.getElementById('chat_res').innerHTML=errorMsg;
          }, 3000);
       return false;
    }

   //fields are empty
   }
   else
   {
    //append the result in the search div
     document.getElementById('chat_res').innerHTML='<em id="err">Select the Tick(s) to delete please!</em>';
     return false;   
   }
}



//function to mark a tick read
function mark_read()
{

   //get the id value to delete
   var id = iaddon();

   if (id != "")
   {
   //check the network connection
   if(window.navigator.onLine)
    {
    //dispay the loading image
    document.getElementById('chat_res').innerHTML = '<img src="/static/images/Loader.gif" />';
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
                document.getElementById("chat_res").innerHTML=xmlhttp.responseText;
               //sync the inbox_unread
                sync_ticks('all');
            }
      }
    xmlhttp.open("GET","/mark_read/?id="+id,true);
    xmlhttp.send();
    
        
    }
   //no connection
   else
    {
       //dispay the loading image
      document.getElementById('chat_res').innerHTML = '<img src="/static/images/Loader.gif" />';
      //set timer
      setTimeout(function(){
            //append the result in the search div
            document.getElementById('chat_res').innerHTML=errorMsg;
          }, 3000);
       return false;
    }

   //fields are empty
   }
   else
   {
    //append the result in the search div
     document.getElementById('chat_res').innerHTML='<em id="err">Select the Tick(s) to mark please!</em>';
     return false;   
   }
}
