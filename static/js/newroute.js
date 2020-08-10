document.addEventListener("DOMContentLoaded", () => {
  document.querySelector("#newroute").onsubmit = function (e) {
    //Make saved routes dissappear
    document.querySelector('#savedroutes').style.display = 'none';
    // Make loading animation visible
    document.querySelector("#loadingword").style.visibility = "visible";
    document.querySelector("#logo").style.display = "inline";
    document.querySelector(".container").style.visibility = "visible";
    document.querySelector(".vertical-center").style.visibility = "visibile";
    // Create JSON request for newroute page
    const request = new XMLHttpRequest();
    request.open("POST", "/newroute");
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
      const duplicate = data.duplicate;

      // Display route data on page
      document.querySelector("#routetitle").innerHTML = title;
      document.querySelector("#startpoint").innerHTML = startpoint;
      document.querySelector("#endpoint").innerHTML = endpoint;
      document.querySelector("#triptime").innerHTML = trip_time;
      document.querySelector("#distance").innerHTML = distance;
      document.querySelector("#directions").innerHTML = directions;
      document.querySelector("#url").innerHTML = "Map URL";
      document.querySelector("#url").href = url;

      //Show warning if title is a duplicate
      if (duplicate) {
        document.querySelector("#warning").innerHTML =
          "That title has already been used and you will erase the other route when saved";
      } else {
        // Remove warning when title is not a duplicate
        document.querySelector("#warning").innerHTML = "";
      }

      //Make save button visible
      document.querySelector("#saveroute").style.display = "inline";

      // Make saved routes disappear and display curent route
      document.querySelector("#routeinfo").style.display = "inline";
      document.querySelector("#savedroutes").style.display = "none";
      // Make loading animation disappear
      document.querySelector("#loadingword").style.visibility = "hidden";
      document.querySelector("#logo").style.display = "none";
      document.querySelector(".container").style.visibility = "hidden";
      document.querySelector(".vertical-center").style.visibility = "hidden";
    };

    const formdata = new FormData(this); // read form's data
    request.send(formdata);

    return false;
  };
});
