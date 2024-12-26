//This script will be injected into Shein’s pages 
//and handle the WebGazer.js setup and eye tracking

// Load the WebGazer.js script dynamically
var script = document.createElement('script');
script.src = "https://cdn.jsdelivr.net/gh/brownhci/WebGazer/webgazer.min.js";
document.head.appendChild(script);

 // CDN version
script.onload = function() {
    // Start WebGazer.js tracking once the script is loaded
    webgazer.setRegression('ridge')
            .setTracker('clmtrackr')
            .begin();
            
            
    // Show gaze points on screen (optional)
    webgazer.showPredictionPoints(true);
    
    // Track gaze data
    setInterval(function() {
        const gazeData = webgazer.getCurrentPrediction();
        if (gazeData) {
            console.log("User gaze position: x: " + gazeData.x + ", y: " + gazeData.y);
            // You can now link this gaze data to specific elements on Shein
        }
    }, 100);
    
    navigator.mediaDevices.getUserMedia({ video: true })
  .then(function(stream) {
    // Webcam access granted, you can start WebGazer now
    console.log("Webcam access granted!");
  })
  .catch(function(error) {
    // Handle error, e.g., user denied access
    console.error("Webcam access denied: ", error);
  });

};
document.head.appendChild(script);
