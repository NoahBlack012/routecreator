document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#newroute").onsubmit = function (e) {
        // Create JSON request for newroute page
        const request = new XMLHttpRequest();
        request.open('POST', "/newroute");
        request.onload = () => {
          // Take data from json request
          const data = JSON.parse(request.responseText);
          const title = data.title;
          const startpoint = data.startpoint;
          const endpoint = data.endpoint;
          const trip_time = data.trip_time;
          const distance = data.distance;
          const directions = data.directions;
          const url = data.url;
          
          // Display route data on page
          document.querySelector("#routetitle").innerHTML = title;
          document.querySelector("#startpoint").innerHTML = startpoint;
          document.querySelector("#endpoint").innerHTML = endpoint;
          document.querySelector("#triptime").innerHTML = trip_time;
          document.querySelector("#distance").innerHTML = distance;
          document.querySelector("#directions").innerHTML = directions;
          document.querySelector("#url").innerHTML = "Map URL";
          document.querySelector("#url").href = url; 

          //Make save button visible
          document.querySelector("#savenote").style.display = "block";

          // Make saved routes disappear and display curent route
          document.querySelector('#routeinfo').style.display = 'block';
          document.querySelector('#savedroutes').style.display = 'none';
        }

        const formdata = new FormData(this); // read form's data
        request.send(formdata);
      
        return false;
    }
});