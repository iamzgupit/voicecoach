// calls on pitchdetect to see if the user's pitch matches the given pitch


var targetNote=[];
var userNote=[];


// take a stream of audio and change it into a letter note using some function in pitchdetect
function targetNoteGetter() {
    // use this file "../static/whistling3.ogg"
    // it's a C and that's specified in this dictionary
    // put it in an array

    alert('This will eventually give you a letter that stands for a note.');
}

// turn the stream into a letter 
// use stuff from pitchdetect to get the note that the file passed in 

function userNoteGetter(){
    toggleLiveInput();
    userNote=noteStrings[note%12];
}


// if targetNote==userNote:
// alert("yay!");
// else
// alert("boo");
