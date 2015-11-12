// calls on pitchdetect to see if the user's pitch matches the given pitch


var targetNote="C";
var targetAudio = new Audio("../static/lower_c.ogg");

function playTargetNote(){
    targetAudio.play();
    setTimeout(function(){
        toggleLiveInput();
   },700
   );

}
