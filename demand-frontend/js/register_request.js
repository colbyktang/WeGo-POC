console.log("Running registerPageHandling.js")

/*
//Whenever the submit button is click, the user credential will be created
//a json object and send to the python server
var registerObject = $('#my-registration')
{
    regisUserName = document.forms["myForm"]["fname"].value;
    regisPassWord = document.forms["myForm"]["fpass"].value;
    regisLocation = document.forms["myForm"]["flocation"].value;

}

//Getting the submit button for an event listener
var submit = document.getElementById("submit");

//event listenter:
submit.addEventListener( 'submit', function(e) {
    const
})
*/

function send_register(register_dictionary) {
    //API key for connection
    console.log("register's toPython() is called!");
    var url = '/api/cs/register';
    var json_object = JSON.stringify(register_dictionary);
    console.log (json_object);

    //making a bridge to the web server
    var request = new XMLHttpRequest();
    //initializing request to the web server
    request.open('POST',  url, true);
    //Setting the header of the API request
    request.setRequestHeader("Content-type", "application/json");

    //do something with the data being processed
    request.onload = function()
    {
       console.log("request.onload is called!");

       // Good response
      if (request.status >= 200 && request.status < 400){
        console.log("Request is sent!");
        console.log("Response: " + request.response);
        console.log(request.statusText);
        alert("Registration of user " + register_dictionary['username'] + " successful!");
        load_page("../index.html");
      }

      else {
        //Error handling
        const errorMessage = document.createElement('error');
        errorMessage.textContent = "Connection Error!";
        alert(request.status + " FAILED: Registration of user " + register_dictionary['username'] + " failed! (" + request.response + ")");
        console.log(request.status);
      }
    }

        //request get sent out!
      request.send(json_object);
}
