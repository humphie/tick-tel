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
}
