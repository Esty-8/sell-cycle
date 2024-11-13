// static/js/validate.js

document.getElementById("data_field").addEventListener("input", function() {
    var value = this.value;
    if (value < 0) {
        document.getElementById("dataFieldError").textContent = "Value cannot be negative.";
    } else {
        document.getElementById("dataFieldError").textContent = "";
    }
});
