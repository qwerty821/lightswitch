var state = 0;
var serverAddress = "http://127.0.0.1:5000/";

document.getElementById("btn-switch-on").addEventListener("click", () => switchLight(1));
document.getElementById("btn-switch-off").addEventListener("click", () => switchLight(0));

async function switchLight(x) {
    if (state != x) {
        state = x;
        changeImage();
        await sendToServer(state);
    }
}

async function sendToServer(data) {
    route = state == 1 ? "/on" : "/off"
    const response = await fetch(serverAddress + route, {
        method: "POST"
    });

    if (response.status == 200) {
        document.getElementById("log-section").innerHTML = "Succes";
        document.getElementById("log-section").classList.remove("error-status");
        document.getElementById("log-section").classList.add("ok-status");
    } else {
        document.getElementById("log-section").classList.add("error-status");
        document.getElementById("log-section").classList.remove("ok-status");
        document.getElementById("log-section").innerHTML = "Fail";
    }
      
}

var light_images = [
    "img/off.png",
    "img/on.png" 
]

function changeImage() {
    document.getElementById("light-bulb")
            .setAttribute("src", light_images[state]);
}
