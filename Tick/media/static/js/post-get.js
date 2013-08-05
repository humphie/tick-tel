//check the internet connection
function internetConnection(){

  if(window.navigator.onLine)
   {
   
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
      alert("All feilds must be filled in!");
      return false;
   
   }
   else{
   
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

}
//end of the loginvalidate


//texting function
function TextForm(Form)
{
name    = document.Form.name.value
contact = document.Form.contact_numbers.value
message = document.Form.message_to_send.value

if(name == "" || contact == "" || message == "")
    {
        
        alert("Please fill out all fields before Texting!");
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
                   
                document.getElementById("send").innerHTML=xmlhttp.responseText;
                document.getElementById("Form").reset()
                
            }
      }
    data = "?name=" +name+ "&contact="+contact+ "&message=" +message
    xmlhttp.open("GET","/text_msging/"+data,true);
    xmlhttp.send();   

   
   }
   else
   {
   
      alert("A network connection can not be established, please try again later!");
      return false;
   
   }
   
   
  }
}
//end of the texting function


//function to send mail
function mailValidate()
{
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
    data = "?subject=" +subject+ "&email=" +email+ "&message=" +message
    xmlhttp.open("GET", "/mail/"+data, true);
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


//the credit function
function creditFormValidator()
{

  username = document.creditForm.username.value
  amount_paid   = document.creditForm.amount_paid.value

  if(username == "" || amount_paid == "")
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
                   
                document.getElementById("creditRes").innerHTML=xmlhttp.responseText;
                document.getElementById("creditForm").reset()
                
              }
        }
            data = "?username=" +username+ "&amount=" +amount_paid
            xmlhttp.open("GET","/credit/"+data,true);
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
//end of the credit function


//function to save aphonenumber
function saveValidate()
{
   var name   = document.saveForm.name.value
   var number = document.saveForm.num.value
   var group  = document.saveForm.group.value
   
   if(name == "" || number == "" || group == "")
   {
      alert("All feilds must be filled in!");
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
                document.getElementById("saveRes").innerHTML=xmlhttp.responseText;
                document.getElementById("saveForm").reset()
                
            }
          }
            data = "?name=" +name+ "&contact_number=" +number+ "&group=" +group
            xmlhttp.open("GET","/save/"+data,true);
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
//end of the function



//function for the phonebook
function phonebookForm(Form){

  var group   = document.FormBook.group.value
  var message = document.FormBook.message.value

  if (group == '' || message == ''){
     
     alert("Type the message to send pliz!");
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
                   
                document.getElementById("sendBook").innerHTML=xmlhttp.responseText;
                document.getElementById("FormBook").reset()
            }
       }
    
       xmlhttp.open("GET", "/phonebook/?group="+group+"&message="+message, true);
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
//end of the forne book function


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

//phonebook search function
function searchValidate()
{
  var query = document.searchForm.query.value
  
  if (query == "")
  {
     alert("Input the name to search!");
     return false;
  }
  else
  {
  
//check te network connection
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
                   
                document.getElementById("searchRes").innerHTML=xmlhttp.responseText;
                document.getElementById("searchForm").reset()
                
            }
      }
    
    xmlhttp.open("GET","/booksearch/?query="+query,true);
    xmlhttp.send();
    
    
    }
//no connection
   else
    {
      alert("A network connection can not be established, please try again later!")
      return false;
    }

  
  }

}
//ens of the search

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



function RegValidate()
{
    var username  = document.regForm.username.value
    var contact   = document.regForm.contact.value
    var country   = document.regForm.country.value
    var password  = document.regForm.password.value
    var password2 = document.regForm.password2.value
    var email     = document.regForm.email.value 

  if(username == "" || contact == "" || country == "" || password == "" || password2 == "" || email == "")
    {
     alert("All fields must be filled!");
     return false;
   }
  else if( password != password2 )
  {
    alert("The passwords you have entered don't match!");
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
                   
                document.getElementById("reg").innerHTML=xmlhttp.responseText;
                document.getElementById("regForm").reset()
                
            }
      }
    data = "?username=" +username+ "&contact=" +contact+ "&country=" +country+ "&email=" +email+ "&password=" +password
    xmlhttp.open("GET","/sign_up/"+data,true);
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
