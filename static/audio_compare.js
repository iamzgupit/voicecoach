// calls on pitchdetect to see if the user's pitch matches the given pitch


var targetNote="A";
var targetAudio = new Audio("../static/c_note.ogg");

function playTargetNote(){
    targetAudio.play();
    setTimeout(function(){
        toggleLiveInput();
   },700
   );

}
