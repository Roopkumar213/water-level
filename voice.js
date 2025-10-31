function startListening() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-IN";
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  recognition.start();

  recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    document.getElementById("spokenText").innerText = `You said: "${transcript}"`;
  };

  recognition.onerror = function(event) {
    document.getElementById("spokenText").innerText = "Error: " + event.error;
  };
}