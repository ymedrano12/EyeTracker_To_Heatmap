//This script will be injected into Shein’s pages 
//and handle the WebGazer.js setup and eye tracking

// Load the WebGazer.js script dynamically
var script = document.createElement('script');
script.src = "https://cdn.jsdelivr.net/npm/webgazer/dist/webgazer.min.js"; // CDN version
script.onload = function() {
    // Start WebGazer.js tracking once the script is loaded
    webgazer.setRegression('ridge')
            .setTracker('clmtrackr')
            .begin();
            
    // Show gaze points on screen (optional)
    webgazer.showPredictionPoints(true);
    
    // Track gaze data
    setInterval(function() {
        var gazeData = webgazer.getCurrentPrediction();
        if (gazeData) {
            console.log("User gaze position: x: " + gazeData.x + ", y: " + gazeData.y);
            // You can now link this gaze data to specific elements on Shein
        }
    }, 100);
};
document.head.appendChild(script);
