// calls on pitchdetect to see if the user's pitch matches the given pitch


var targetNote="C";
var targetAudio = new Audio("../static/c_note.ogg");
var userNote=[];

function playTargetNote(){
    targetAudio.play();
    // after a few seconds (enough time for the target note to play)...
    setTimeout(function(){
        alert("go you!");
        toggleLiveInput();
   },700
   );

console.log("hellooooo is it meeee you're looking foooor");
myNote = $("#note").html();
console.log(myNote);
alert(myNote);

if (myNote==targetNote){
    alert("yay");
}
else
{
    alert("boo");
};

}


// if targetNote[0]==userNote:
// alert("yay!");
// else
// alert("boo");
