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
     //send the form
     return true; 
   }
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

  if (password != "" || password1 != "" && password1 == password )
  {
  
  //check if there is an internet connection
   if (window.navigator.onLine)
   {
     //send the form
     return true; 
   }
   else
    {
      //return the connect method
      document.getElementById('chat_res').innerHTML= errorMsg;   
      return false;
 
     }
 
  }
  else
  {
    //reset the form 
    document.getElementById("change_pword_form").reset();
    //return the connect method
    document.getElementById('chat_res').innerHTML= "<em id='err'>Please re-enter the passwords.</em>";   
    return false;
  
  }

}
////////////////////////////////////////////////////////////////////////////////

