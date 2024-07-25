function predictResult() {
    var value = document.getElementById("predict");
    var result = document.getElementById("result");

    console.log(value)

    if (value == "1") {
        result.textContent = "Passed";
        result.style.color = "green";
    } else if (value == "0") {
        result.textContent = "Failed";
        result.style.color = "red";
    } else {
        result.textContent = "Invalid input";
        result.style.color = "black";
    }

}