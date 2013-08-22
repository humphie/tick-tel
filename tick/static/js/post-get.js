//network error message
var errorMsg = "<em id='err'>A network connection can not be established, please try again later!</em>";
//empty feilds message
var emptyFields = "<em id='err'>All fields must be filled in!</em>";
///////////////////////////////////////////////////////////////



//check the internet connection
function networkConnection(){

  if(window.navigator.onLine)
   {
       return true;
   }
   else
   {
      alert("A network connection can not be established, please try again later!");
      return false;
   }
}   


//function to validate the login
function loginValidate()
{

   username = document.loginForm.username.value
   password = document.loginForm.password.value
   
   if (username == "" || password == "")
   {
      //display the error message
      document.getElementById("login_Response").innerHTML=emptyFields;
      return false;
   
   }
   else{
   
   if(window.navigator.onLine)
   {
     document.getElementById('login_Response').innerHTML = '<img src="/static/images/Loader.gif" />';
     return true;
   }
    else
   {
      //display the loading image
      document.getElementById('login_Response').innerHTML = '<img src="/static/images/Loader.gif" />';
      //set timer
      setTimeout(function(){
        //dispay the empty fields message
        document.getElementById('login_Response').innerHTML = errorMsg;
      }, 3000);
      return false;
   }
   
  }

}
//end of the loginvalidate



//function to send mail
function mailValidate()
{
 //get the src
 var src     = document.reply_form.Username.value
 var subject = document.mailForm.subject.value
 var email   = document.mailForm.email.value
 var message = document.mailForm.message.value
 
 if(subject == "" || email == "" || message == "")
 {
   alert("All feilds must be filled!");
   return false;
 }
 else
 {

//check for internet connection
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
                   
                document.getElementById("mailRes").innerHTML=xmlhttp.responseText;
                document.getElementById("mailForm").reset()
                
            }
      }
    data = "?name=tick&message="+email+'===='+subject+'===='+message +"&src="+src
    xmlhttp.open("GET", "/send_tick/"+data, true);
    xmlhttp.send();
   
    }
//no network connection
   else
    {
      alert("A network connection can not be established, please try again later!");
      return false;    
    }
 
 }
 
}

//end of the mail validator



function updateSlider(slideAmount) {
//get the element
var display = document.getElementById("chosen");
   //show the amount
  display.innerHTML=slideAmount;
  //get the element
 
  }


function Recharge(value)
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
                   
                document.getElementById("prices").innerHTML=xmlhttp.responseText;
                
            }
      }
    
    xmlhttp.open("GET","/recharge/?number="+value,true);
    xmlhttp.send();
  
  
    }
//no network connection
   else
    {
       alert("A network connection can not be established, please try again later!")
    }

}


//api subscription
function Subscribe(){

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
                   
                document.getElementById("sub").innerHTML=xmlhttp.responseText;
                $("#sub").delay(10000).hide(800);
            }
      }
    xmlhttp.open("GET","/subscribe/",true);
    xmlhttp.send();

   
   }
//no network connection
  else
   {
      alert("A network connection can not be established, please try again later!");
      return false;
   }
   
}
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
//function to count how many x-ters a user has typed so far
function counter(div, id)
{
  var message = document.getElementById(id).value
  document.getElementById("Response_Phonebook").innerHTML=message.length+" characters.";
  //alert(message.length+" characters.");
}
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
function Reg_validator()
{   
    var username  = document.getElementById('username').value
    var contact   = document.getElementById('contact').value
    var password  = document.getElementById('password').value
    var password2 = document.getElementById('password2').value
    var email     = document.getElementById('email').value 
    var e         = document.getElementById("country");
    var country   = e.options[e.selectedIndex].value;
   
 if(username == "" || 
     contact == "" || 
     country == "Select your Country:" ||
     password == "" ||
     password2 == "" ||
     email == "")

    {
   //dispay the empty fields message
    document.getElementById('registration_Response').innerHTML = emptyFields;
    return false;
   }
  else if( password != password2 )
  {
   //dispay the empty fields message
    document.getElementById('registration_Response').innerHTML = "<em id='err'>The passwords are not matching!</em>";
    return false;
  }

  else
  {
//check for network connection
  if(window.navigator.onLine)
   {
   //dispay the loading image
    document.getElementById('registration_Response').innerHTML = '<img src="/static/images/Loader.gif" />';
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
                //display the response   
                document.getElementById("registration_Response").innerHTML=xmlhttp.responseText;
                //reset the form
                document.getElementById("reg_Form").reset()
                
            }
      }
    data = "?username=" +username+ "&contact=" +contact+ "&country=" +country+ "&email=" +email+ "&password=" +password
    xmlhttp.open("GET","/sign_up/"+data,true);
    xmlhttp.send();
   }
//no network connection
  else
   {
      //dispay the loading image
    document.getElementById('registration_Response').innerHTML = '<img src="/static/images/Loader.gif" />';
    //set timer
    setTimeout(function(){
        //dispay the empty fields message
        document.getElementById('registration_Response').innerHTML = errorMsg;
      }, 3000);
    return false;
   }
  }


}
//////////////////////////////////////////////////////////////////////////////////////////
