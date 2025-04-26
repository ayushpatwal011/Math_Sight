
 let recognition;
         let isListening = false;

         function startListening() {
             if (!recognition) {
                 const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                 recognition = new SpeechRecognition();
                 recognition.continuous = false;
                 recognition.interimResults = false;
                 recognition.lang = 'en-US';

                 recognition.onresult = function(event) {
                     const transcript = event.results[0][0].transcript;
                     document.getElementById("question").value = transcript;
                     isListening = false;
                 };

                 recognition.onend = function() {
                     isListening = false;
                 };
             }

             if (!isListening) {
                 recognition.start();
                 isListening = true;
             }
         }

         function sendQuestion() {
             const question = document.getElementById("question").value;
             console.log(question);
            
             fetch("/ask", {
     method: "POST",
     headers: {
         "Content-Type": "application/json"
     },
     body: JSON.stringify({ question })
 })
 .then(response => response.json()) // Return the parsed JSON here
 .then(data => {
     console.log(data); // Now you can see the correct data
     document.getElementById("answer").innerText = data.answer || data.error;
 })
 .catch(error => {
     console.error("Error:", error);
 });
 fetch("/ask", {
     method: "POST",
     headers: {
         "Content-Type": "application/json"
     },
     body: JSON.stringify({ question })
 })
 .then(response => response.json()) // Return the parsed JSON here
 .then(data => {
     console.log(data); // Now you can see the correct data
     document.getElementById("answer").innerText = data.answer || data.error;
 })
 .catch(error => {
     console.error("Error:", error);
 });
   }


