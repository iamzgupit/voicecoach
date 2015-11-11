// calls on pitchdetect to see if the user's pitch matches the given pitch


var targetNote="A";
var targetAudio = new Audio("../static/c_note.ogg");
var userNote=[];

function playTargetNote(){

    targetAudio.play();
    // after a few seconds (enough time for the target note to play)...
    setTimeout(function(){
        toggleLiveInput();
   },700
   );

myNote = $("#note").html();

if (myNote != "--" || "-"){
    alert(myNote);
    if (myNote==targetNote){
        alert("yay");
    } else {
        alert("no");
    }
}


// if (myNote==targetNote){
//     alert("yay");
// }
// else
// {
//     alert("boo");
// }

}


// if targetNote[0]==userNote:
// alert("yay!");
// else
// alert("boo");
