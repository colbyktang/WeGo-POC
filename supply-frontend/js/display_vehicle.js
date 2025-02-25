console.log("Running display_vehicle.js")


function get_vehicle(vehicle){
    //API key for connection
    console.log("get_vehicle() is called!");
    var url = '/api/cs?vehicle=22&get=all';


    //making a bridge to the web server
    var request = new XMLHttpRequest();


    request.onreadystatechange = function() {
      console.log("request.onreadystatechange called")

      if(this.readyState == 4 && this.status == 200)
        {
          //response is received
          console.log("request is sent")
          var json_object = JSON.parse(this.responseText);
          document.getElementById("VehiclesDiv").innerHTML = request.responseText;


        }

    };
    //initializing request to the web server
    request.open('GET',  url, true);


        //request get sent out!
      request.send();
}
