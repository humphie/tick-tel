
//function to draw the forms
function drawDiv(div)
{
//divs of calendar page 
   if (div == "create_event")
   {
     //clear the page
     clearAll("calendar");
     //display the right div
     document.getElementById('calendar').style.display = 'block';
     //display the create form name
     document.getElementById("create_event").style.display = 'block';
   }
   else if (div == "delete_event")
   {
     //clear the page
     clearAll("calendar");
     //display the right div
     document.getElementById('calendar').style.display = 'block';
     //remove the event search result
     document.getElementById("searchResult").style.display = 'block';
     //display the delete form name
     document.getElementById("delete_event").style.display = 'block';

   }
   else if (div == "edit_event")
   {
     //clear the page
     clearAll("calendar");
     //display the right div
     document.getElementById('calendar').style.display = 'block';
     //display the delete form name
     document.getElementById("edit_event").style.display = 'block';
   }



//divisions for the phnebook page 
  if(div == 'phonebook_text')
  {
     // clear the page
     clearAll('phonebook');
     //disply the right div
     document.getElementById("PhoneBook").style.display = 'block';
     //display the phonebook send form
     document.getElementById("phonebook_text").style.display = 'block';  
   }
   else if (div == 'contact_save')
   {
     //clear the page
     clearAll('phonebook');
     //disply the right div
     document.getElementById("PhoneBook").style.display = 'block';
     //display the save form
     document.getElementById("contact_save").style.display = 'block';
   }
   else if (div == 'contact_edit')
   {
     //clear the page
     clearAll('phonebook');
     //disply the right div
     document.getElementById("PhoneBook").style.display = 'block';
     //display the edit form
     document.getElementById("contact_edit").style.display = 'block';
   }
   else if (div == 'contact_delete')
   {
     //clear the page
     clearAll('phonebook');
     //disply the right div
     document.getElementById("PhoneBook").style.display = 'block';
     //display the delete form
     document.getElementById("contact_delete").style.display = 'block';
   }
   else if (div == "contact_numbers")
   {
     //clear the page
     clearAll("phonebook");
   }

//send_msg form
  if (div == "msg_report")
   {
     //clear the page
     clearAll("send_text");
     //siplay the the reports div
     document.getElementById("main_report").style.display = 'block';
     //get the phonenumbers
     get_report("");
   }


//dash boards forms
  if (div == "chat_send")
  {
  //clear the page
  clearAll("dashboard");
  //display the right div
  document.getElementById("left_div").style.display = "block";
  //get the contacts
  sync_ticks('all');
  //display the chat_send form
  document.getElementById("tick_form_div").style.display = "block";
  }
 //reply_send
   if (div == "reply_send")
  {
  //clear the page
  clearAll("dashboard");
  //get the conversation
  conversation();
  //display the right div
  document.getElementById("left_div").style.display = "block";
  //display the chat_send form
  document.getElementById("reply_form_div").style.display = "block";
  }
  if (div == "change_acc")
  {
   //clear the page
  clearAll("dashboard");
  //display the right div
  document.getElementById("left_div").style.display = "block";
  //remove the unread ticks div
  document.getElementById("inbox_unread").style.display = "none";
  //display thr prifile div
  document.getElementById("all_ticks").style.display = "block";
  //display the form
  document.getElementById("change_acc_form_div").style.display = "block";
  }
  if (div == "edit_profile")
  {
   //clear the page
  clearAll("dashboard");
  //display the right div
  document.getElementById("left_div").style.display = "block";
  //remove the unread ticks div
  document.getElementById("inbox_unread").style.display = "none";
  //display thr prifile div
  document.getElementById("all_ticks").style.display = "block";
  //display the form
  document.getElementById("edit_acc_form_div").style.display = "block";
  }
  if (div == "change_pword")
  {
   //clear the page
  clearAll("dashboard");
  //display the right div
  document.getElementById("left_div").style.display = "block";
  //remove the unread ticks div
  document.getElementById("inbox_unread").style.display = "none";
  //display thr prifile div
  document.getElementById("all_ticks").style.display = "block";
  //display the form
  document.getElementById("change_pword_form_div").style.display = "block";
  }


  
//staff member page
  if (div == "member_tick" )
  {
  //clear the page
  clearAll("member_page");
  //remove the save number
  document.getElementById('save_member').style.display = 'none';
  //remove the  membersdiv
  document.getElementById('members').style.display = 'block';
  //display the tick form
  document.getElementById('member_tick').style.display = 'block';
  }
  if (div == "delete_member" )
  {
    //clear all
    clearAll('member_page');
    //remove the save number
    document.getElementById('save_member').style.display = 'none';
    //display the tick form
    document.getElementById('member_delete_form').style.display = 'block';
    //display the update list
    syncMembers('');
  }
  if (div == "save_member" )
  {
    //clear all
    clearAll('member_page');
    //display the update list
    syncMembers('');
  }

}



//function to clear every din on the phonebook page
function clearAll(page)
{
  if (page == "calendar")
  {
     //remove the event search result
     document.getElementById("searchResult").style.display = 'none';
     //remove the create form in case its there
     document.getElementById("create_event").style.display = 'none';
     //remove delete form
     document.getElementById("edit_event").style.display = 'none';
     //remove delete form
     document.getElementById("delete_event").style.display = 'none';
     //remove the links div
     document.getElementById('links').style.display = 'none';
     //remove the links div
     document.getElementById('links_2').style.display = 'none';
     //remove response div
     document.getElementById("Response_Calendar").style.display = 'none';
     //remove the right div
     document.getElementById('calendar').style.display = 'none';
  }
  else if(page == "phonebook")
  {
     //send text form
     document.getElementById("phonebook_text").style.display = 'none';
     //remove the save form
     document.getElementById("contact_save").style.display = 'none';
     //remove the delete form
     document.getElementById("contact_delete").style.display = 'none';
     //remove the edit form
     document.getElementById("contact_edit").style.display = 'none';
     //remove response div
     document.getElementById("Response_Phonebook").style.display = 'none';
     //remove the phonenumbers
     document.getElementById("PhoneBook").style.display = 'none';
     //remove the search result
     document.getElementById("contact_search_result").style.display = 'block';
     //get the numbers
     getNumbers();
  }
  //if page is for sending sn sms
  else if (page == "send_text")
  {
     //remove the reports div
     document.getElementById("main_report").style.display = 'none';
	 //display the delete form
     document.getElementById("delete_report").style.display = "none";
	 //remove the testinf form
	 document.getElementById("texting").style.display = "block";
  }
  else if ( page == "dashboard" )
  {
   //tick form
  document.getElementById("tick_form_div").style.display = "none";
  //tick reply form
  document.getElementById("reply_form_div").style.display = "none";
  //remove the search result div
  document.getElementById("all_ticks").style.display = "none";
  //remove the form
  document.getElementById("edit_acc_form_div").style.display = "none";
  //remove the form
  document.getElementById("change_pword_form_div").style.display = "none";
  //remove the form
  document.getElementById("change_acc_form_div").style.display = "none";
  //remove the search result div
  document.getElementById("inbox_unread").style.display = "block";

  }
  else if ( page == "member_page" )
  {
  //remove the  membersdiv
  document.getElementById('members').style.display = 'block';
  //remove the delete form
  document.getElementById('member_delete_form').style.display = 'none';
  //remove the tick form
  document.getElementById('member_tick').style.display = 'none';
  //remove the save number
  document.getElementById('save_member').style.display = 'block';
  }

}
