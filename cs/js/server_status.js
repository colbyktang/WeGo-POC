console.log("Running server_status.js")

function ping_server() {
    console.log("ping_server() is called!");
    var url = '/api/cs?status=1';

    //making a bridge to the web server
    var request = new XMLHttpRequest();
    //initializing request to the web server
    request.open('GET', url, true);
    //Setting the header of the API request
    request.setRequestHeader("Content-type", "application/json");

    //do something with the data being processed
    request.onload = function () {
        console.log("request.onload is called!");
        if (request.status >= 200 && request.status < 400) {
            document.getElementById("server_status").innerHTML = request.responseText;
        }
        else {
            var response = "Web server is not running! Code " + request.status;
            document.getElementById("server_status").style.color = "red";
            document.getElementById("server_status").style.fontWeight = "bolder";
            document.getElementById("server_status").innerHTML = response;
        }
    }

    //request get sent out!
    request.send();
}
