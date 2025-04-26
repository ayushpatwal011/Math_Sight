const commands ={
    "classroom":"/classroom",
    "progress" : "/progress",
    "community" : "/community",
    "test": "/test"

};

const synth = window.speechSynthesis;
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.continous = false;
recognition.lang ='en-US';

recognition.interimResults = false;
recognition.maxAlternatives =1;

//speak text aloud 
function speak(text,callback){
    const utter = new SpeechSynthesisUtterance(text);
    utter.onend = callback;
    synth.speak(utter);
}

function startListening(){
    recognition.start();
}

recognition.onresult =(event) =>{
    const transcript = event.results[0][0].transcript.toLowerCase();
    console.log("User said:",transcript);
    for(let key in commands){
        if(transcript.includes(key)){
            window.location.href = commands[key];
            return;
        }
    }
    speak("I didn't understand that. please say 'classroom','progress','community','profile'or 'test'",()=>{
        startListening();
    });
};
recognition.onspeechend = () =>{
    recognition.stop();
    speak("okay",()=>{
        
    });
};

recognition.onerror = (event) =>{
    console.error("speech recognition error:", event.error);
    speak("I didnot hear anything. Please say your choice.",()=>{
        startListening();
    });
};
window.onload =()=>{
    speak("Hello! Welcome to MathSight. You can choose from 'classroom','progress','community','exam environment'",()=>{
        startListening();
    });

};