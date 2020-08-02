function open_route(id) {
    alert ("Open route");
    let request = new XMLHttpRequest();
    const url = '/openroute/' + id; 
    request.open('POST', url);
    request.onload = () => {
        //const route_data = JSON.parse(request.responseText);
        // Get route data 
        // Display route data
    }
    // Send XML request to open route
    // Make page display that routes properties
    const data = new FormData();
    request.send(data);
    return false; 
}      
document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#openroute").onsubmit = function () { 
        let display_route = false; 
        document.querySelector("#savedroutes").innerHTML = "";
        let request = new XMLHttpRequest();
        request.open('POST', '/savedroutes');
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            const titles = data.titles; 
            let title_size = Object.keys(titles).length
            for (i = 0; i < title_size; i++) {
                // Make sure onclick is applied to button element 
                // Change button var name
                title = titles[i]
                let title_button = document.createElement('input');
                title_button.type = 'submit';
                title_button.value = title;
                title_button.id = title;
                title_button.onclick = () => {
                    let route_request = new XMLHttpRequest();
                    const route = '/openroute/' + title_button.id; 
                    route_request.open('POST', route);
                    route_request.onload = () => {
                        const route_data = JSON.parse(route_request.responseText);
                        let title = route_data.title;
                        let start = route_data.start;
                        let end = route_data.end;
                        let time = route_data.time;
                        let distance = route_data.distance;
                        let directions = route_data.directions;
                        let url = route_data.url; 
                        // Display route data
                        document.querySelector("#routetitle").innerHTML = title;
                        document.querySelector("#startpoint").innerHTML = start;
                        document.querySelector("#endpoint").innerHTML = end;
                        document.querySelector("#triptime").innerHTML = time;
                        document.querySelector("#distance").innerHTML = distance;
                        document.querySelector("#directions").innerHTML = directions;
                        document.querySelector("#url").innerHTML = "Map URL";
                        document.querySelector("#url").href = url; 
                    }
                    // Make page display that routes properties
                    document.querySelector('#routeinfo').style.display = 'block';
                    document.querySelector('#savedroutes').style.display = 'none';
                    display_route = true;
                    //document.querySelector("#saved")
                    const data = new FormData();
                    route_request.send(data);
                    return false; 
                };
                document.querySelector("#savedroutes").appendChild(title_button);
            }
            if (display_route) {
                // Make current route info appear and saved routes disappear
                document.querySelector('#routeinfo').style.display = 'block';
                document.querySelector('#savedroutes').style.display = 'none';
            }else{
                // Make current route info disappear and saved routes open
                document.querySelector('#routeinfo').style.display = 'none';
                document.querySelector('#savedroutes').style.display = 'block';
            }
        }
        const formdata = new FormData();
        request.send(formdata);
        return false; 
    }
});