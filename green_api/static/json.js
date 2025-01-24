
document.addEventListener("DOMContentLoaded", function() {
    let responseField = document.getElementById('response');
    let formattedJson = JSON.parse(responseField.textContent);
    responseField.textContent = JSON.stringify(formattedJson, null, 4);
});