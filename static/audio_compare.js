// calls on pitchdetect to see if the user's pitch matches the given pitch


var targetNote="C";
var targetAudio = new Audio("../static/c_note.ogg");
var userNote=[];

function playTargetNote(){
    targetAudio.play();
    // after a few seconds (enough time for the target note to play)...
    userNote=toggleLiveInput();
    console.log(userNote);
    alert(userNote);
}


// if targetNote[0]==userNote:
// alert("yay!");
// else
// alert("boo");
