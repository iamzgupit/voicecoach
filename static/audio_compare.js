// calls on pitchdetect to see if the user's pitch matches the given pitch


var targetNote="A";
var targetAudio = new Audio("../static/c_note.ogg");
var userNote=[];

function playTargetNote(){
    targetAudio.play();
    setTimeout(function(){
        toggleLiveInput();
        myNote = $("#note").html();
        if (myNote != "--" && myNote != "-"){
            if (myNote===targetNote){
                alert("yay");
            } else {
                alert("no");
            }
        }
   },700
   );






}

