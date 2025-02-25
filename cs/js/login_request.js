console.log("Running login_request.js!");

// Sends a JSON Object to the back-end using a dictionary
function send_login_demand(login_dictionary){
  //API key for connection
  console.log("send_login_demand() is called!");
  var url = 'api/cs/login';
  var jsonObject = JSON.stringify(login_dictionary);

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
      document.cookie = "demand_username = " + login_dictionary["username"];
      names_dictionary = JSON.parse(request.response);
      document.cookie = "demand_firstname = " + names_dictionary["first_name"];
      document.cookie = "demand_lastname = " + names_dictionary["last_name"];
      load_page("https://demand.team12.softwareengineeringii.com/dashboard.html");
    }

    // Bad Response, error handling
    else {
      console.log(request.status);
      alert ("Login error: " + request.status + " (" + request.response +  ")");
    }
  }
  
  // Send JSON Object to back-end
	request.send(jsonObject);
}


  // Sends a JSON Object to the back-end using a dictionary
  function send_login_supply(login_dictionary){
    //API key for connection
    console.log("send_login_supply() is called!");
    var url = 'api/cs/login';
    var jsonObject = JSON.stringify(login_dictionary);

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
        document.cookie = "supply_username = " + login_dictionary["username"];
        names_dictionary = JSON.parse(request.response);
        document.cookie = "supply_firstname = " + names_dictionary["first_name"];
        document.cookie = "supply_lastname = " + names_dictionary["last_name"];
        load_page("https://supply.team12.softwareengineeringii.com/dashboard.html");
      }

      // Bad Response, error handling
      else {
        console.log(request.status);
        alert ("Login error: " + request.status + " (" + request.response +  ")");
      }
    }

  // Send JSON Object to back-end
	request.send(jsonObject);
}
