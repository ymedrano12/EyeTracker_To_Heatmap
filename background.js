//This is where you can handle background processes, 
// such as managing the extension’s lifecycle.

// background.js (optional)
chrome.runtime.onInstalled.addListener(function() {
    console.log("WebGazer.js initialized!");
});
