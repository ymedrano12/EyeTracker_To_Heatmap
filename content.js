// This script will be injected into Shein’s pages 
// and handle the WebGazer.js setup and eye tracking

// Load the WebGazer.js script dynamically
var script = document.createElement('script');
script.src = "https://cdn.jsdelivr.net/gh/brownhci/WebGazer/webgazer.min.js";
document.head.appendChild(script);

// Wait for the WebGazer.js script to load
script.onload = function() {
    // Request webcam access first
    navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
        // Webcam access granted
        console.log("Webcam access granted!");
        
        // Initialize WebGazer.js after webcam access is granted
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
                // Here, you can map the gaze data to specific elements on Shein's page
                // Example: If user is looking at a product image, you can track which image they're focusing on
            }
        }, 100); // Collect data every 100ms
    })
    .catch(function(error) {
        // Handle error, e.g., user denied access
        console.error("Webcam access denied: ", error);
    });
};
