//This javascript file will make a POST request for a vehicle, vehicle name
//The request sending in would also contains a username
//Once the connection is made and the request is sent out, a response would come back with the same username, vehicle and vehicle name.
//The JS file would then output the info from the reponse to the html file.
console.log("Running order_request.js")

function send_order_request (order_dictionary){
    //Opening a connection to the server
    console.log("running toSupplyBackend.js");
    var url = "/api/cs/order";
    //constructing a json obbject to store the information
    //in the request to be sent out.
    var json_object = JSON.stringify(order_dictionary);
    console.log(json_object);

    //Making a bridge to the server through XMLHttpRequest()
    var request = new XMLHttpRequest();

    //Initializaing a request to the order
    request.open('POST', url, true);

    //Setting the header of the API request
    request.setRequestHeader("Content-type", "application/json");

    //do something with the data being processed
    request.onload = function()
    {
        console.log("request.onload is called!");

       //if the request is good and valid, store the response in session storage
       if (request.status >= 200 && request.status < 400){

        console.log("Request is sent!");
        console.log("Response: " + request.response);
        console.log("Status Text: " + request.statusText);
        var final_response = request.response;
        sessionStorage.setItem("final_response", final_response);
        load_page('confirmation_page.html');
       }

       else {
         //Error handling
         const errorMessage = document.createElement('error');
         errorMessage.textContent = "Connection Error!";
         console.log(request.status);
         alert("FAILED: Order Submission failed!, Please Try Again or Contact Support");
       }
     }
         //request get sent out!
       request.send(json_object);
 }
