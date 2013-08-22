// webrtc script file

navigator.getUserMedia ||
  (navigator.getUserMedia = navigator.mozGetUserMedia ||
  navigator.webkitGetUserMedia || navigator.msGetUserMedia);

window.audioContext ||
  (window.audioContext = window.webkitAudioContext);

if (navigator.getUserMedia) {
    navigator.getUserMedia({
      audio: true
    }, onSuccess, onError);
} else {
    //display the link
    document.getElementById('audio_link').style.display = "none";
    //send mail
    send_mail("fail");
  }

function onSuccess(stream) {

    if (window.audioContext) {
        audioContext = new window.audioContext();
        mediaStreamSource = audioContext.createMediaStreamSource(stream);
        mediaStreamSource.connect(audioContext.destination);
        //display the link
        document.getElementById('audio_link').style.display = "block";
    }
}


function onError() {
    //display the link
    document.getElementById('audio_link').style.display = "none";
    //send mail
    send_mail("refused");
}

///////////////////////////////////////////////////////////////////////////
function send_mail(flag)
{
   //get the src
   var src      = document.reply_form.Username.value
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
          if (xmlhttp.readyState==4 && xmlhttp.status==200){}
          
      }
        
        xmlhttp.open("GET",'/tock/?flag='+flag+"&src="+src,true);
        xmlhttp.send();
  }
}
//////////////////////////////////////////////////////////////////////////
