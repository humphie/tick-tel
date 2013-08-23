//network error message
var errorMsg = "<em id='err'>A network connection can not be established, please try again later!</em>";
//empty feilds message
var emptyFields = "<em id='err'>All fields must be filled in!</em>";

////////////////////////////////////////////////////////////////////////////////
//change the account type
function acc_change(acc_type)
{
      //check network connection
   if(window.navigator.onLine)
    {
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
                document.getElementById('change_acc_form').reset();
                //remove the all ticks
                document.getElementById('all_ticks').style.display = 'block';
                //remove the right div
                document.getElementById('left_div').style.display = 'none';
                
                //return the connect method
                document.getElementById('chat_res').innerHTML=xmlhttp.responseText;
            }
          
      }
        
        xmlhttp.open("GET",'/change_account/?acc_type='+acc_type,true);
        xmlhttp.send();

   }
   else
   {
    //return the connect method
    document.getElementById('chat_res').innerHTML= errorMsg;   
    return false;
   }
}
////////////////////////////////////////////////////////////////////////////////

/////////////////////////edit an account////////////////////////////////////////
function edit_acc()
{
  //get the fields
  full_name = document.edit_acc_form.edit_full_name.value
  contact   = document.edit_acc_form.edit_contact.value
  short_desc = document.edit_acc_form.edit_desc.value

  if (full_name != "" || contact != "" || short_desc != "")
  {
  
  //check if there is an internet connection
   if (window.navigator.onLine)
   {
     return true;
   }
   //no network connection
   else
   {
    //return the connect method
    document.getElementById('chat_res').innerHTML= errorMsg;   
    return false;
   }
  }
   else
   {
    //return the connect method
    document.getElementById('chat_res').innerHTML= emptyFields;   
    return false;
   }
  
}
////////////////////////////////////////////////////////////////////////////////
///////////////////////////////function to change the password//////////////////
function pword_change()
{
  //get the fields
  password  = document.change_pword_form.change_password.value
  password1 = document.change_pword_form.change_password1.value
  username  = document.change_pword_form.Username.value

 if (password == "" || password1 == "" )
    {
    //reset the form 
    document.getElementById("change_pword_form").reset();
    //return the connect method
    document.getElementById('chat_res').innerHTML= "<em id='err'>Please enter the passwords.</em>";   
    return false;

   }
  else if (password != password1){
    //reset the form 
    document.getElementById("change_pword_form").reset();
    //return the connect method
    document.getElementById('chat_res').innerHTML= "<em id='err'>The passwords dont match.</em>";   
    return false;


   }
  else
  {
  //check if there is an internet connection
   if (window.navigator.onLine)
   {
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
                document.getElementById('change_pword_form').reset();
                //remove the all ticks
                document.getElementById('all_ticks').style.display = 'block';
                //remove the right div
                document.getElementById('left_div').style.display = 'none';
                //return the connect method
                document.getElementById('chat_res').innerHTML=xmlhttp.responseText;
            }
          
      }
        data = "?password="+password+ "&Username="+username
        xmlhttp.open("GET",'/change_password/'+data,true);
        xmlhttp.send();

   }
   //no network connection
   else
    {
      //return the connect method
      document.getElementById('chat_res').innerHTML= errorMsg;   
      return false;
     }
  }

}
////////////////////////////////////////////////////////////////////////////////

