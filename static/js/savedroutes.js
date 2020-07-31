document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#openroute").onsubmit = function (e) {
        document.getElementById("routes_title_ul").innerHTML = "";
        request = new XMLHttpRequest();
        request.open('POST', '/savedroutes');
        request.onload = () => {
            const data = JSON.parse(request.responseText);
            const titles = data.titles; 
            title_size = Object.keys(titles).length
            for (i = 0; i < title_size; i++) {
                title = titles[i]
                let li = document.createElement('li');
                li.innerHTML = title;
                document.querySelector("#routes_title_ul").append(li);
            }
            // Make current route info disappear and saved routes open
            document.querySelector('#routeinfo').style.display = 'none';
            document.querySelector('#savedroutes').style.display = 'block';
        }
        const formdata = new FormData(this);
        request.send(formdata);
        return false; 
    }
});