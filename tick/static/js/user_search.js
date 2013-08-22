//network error message
var errorMsg = "<em id='err'>A network connection can not be established, please try again later!</em>";
//empty feilds message
var emptyFields = "<em id='err'>All fields must be filled in!</em>";

//toggle the disply
 function home()
 {
  var display = '';
  //check the chat display style
  if ( document.getElementById("reply_form_div").style.display == "block" )
  {
     clearAll('dashboard');
     document.getElementById("reply_form_div").style.display = "block";
  }
  document.getElementById('inbox_unread').style.display = 'none';
  document.getElementById('all_ticks').style.display = 'block';
 }
/////////////////////////////////////////////////////////////////////////////




//function to search a user
function search_user(div)
{
  if (div == ""){
    //get the user name
    var username = document.user_search_form.user_query_on_fly.value
  
  }
  else if (div == 'not_on_fly')
  {
    //get the user name
    var username = document.user_searchForm.user_query.value
  
  }
  
  //check if the var are empty
  if (username != "")
  {
      //check network connection
   if(window.navigator.onLine)
   {
     document.getElementById('inbox_unread').innerHTML = '<img src="/static/images/Loader.gif" />';
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
                document.getElementById('user_searchForm').reset();
                //remove the all ticks
                document.getElementById('all_ticks').style.display = 'none';
                //display the result
                document.getElementById('inbox_unread').style.display = 'block';
                //return the connect method
                document.getElementById('inbox_unread').innerHTML=xmlhttp.responseText;
            }
          
      }
        
        xmlhttp.open("GET",'/user_search/?username='+username,true);
        xmlhttp.send();

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

//function to invite afriend
function invitation()
{
  //get the username
  var username = document.getElementById('Username').value;
  //get the user name
  var number = document.invitation_form.invitation,value;

  if (username != '' || number != ''){
   //check network connection
   if(window.navigator.onLine)
   {
    var xmlhttp;
    var response = '';
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
                document.getElementById('user_searchForm').reset();
                //remove the all ticks
                document.getElementById('all_ticks').style.display = 'none';
                //display the result
                document.getElementById('inbox_unread').style.display = 'block';
                //return the connect method
                document.getElementById('inbox_unread').innerHTML=xmlhttp.responseText;
            }
          
      }
        
        xmlhttp.open("GET",'/invitation/?number='+number,true);
        xmlhttp.send();
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
//the credit function
function creditFormValidator()
{

  username = document.creditForm.username.value
  amount_paid   = document.creditForm.amount_paid.value

  if(username == "" || amount_paid == "")
   {
     //dispay the loading image
     document.getElementById('creditRes').innerHTML = emptyFields;
     return false;
   }
  else{
  
//check for network connection
      if(window.navigator.onLine)
       {
         //dispay the loading image
         document.getElementById('creditRes').innerHTML = '<img src="/static/images/Loader.gif" />';

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
          //display the loading image
          document.getElementById('creditRes').innerHTML = '<img src="/static/images/Loader.gif" />';
          //set timer
          setTimeout(function(){
            //dispay the empty fields message
            document.getElementById('creditRes').innerHTML = errorMsg;
          }, 3000);
          return false;
       }
  }

}
//end of the credit function

