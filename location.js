// Grabs input directly from the URL query parameters
const params = new URLSearchParams(window.location.search);
const username = params.get('name'); 

// Insecure: Directly inserts the unvalidated string as HTML
document.getElementById('welcome-msg').innerHTML = "Welcome, " + username; 

// Attack Payload: ?name=<img src=x onerror=alert('Hacked!')>
