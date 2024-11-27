function sleep(time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}


async function receiveData(socket, element) {
    socket.onmessage = (event) => {
        let data = JSON.parse(event.data);
        console.log('data:', data);
        element.innerText = data.text;
    }
    if (element.innerText === "🚀") {
        socket.close();
        console.log("Connection closed for socket: ", socket);
        let altitude = 1;
        do {
            await setAltitude(element, altitude*10);
            altitude++;
        } while (altitude <= 20);
    } else {
        setTimeout(() => sendData(socket, element, `Confirmed: ${element.innerText}`), 1000);
    }
}


async function sendData(socket, element, text) {
    socket.send(JSON.stringify(text));
    await receiveData(socket, element);
}


async function setAltitude(element, altitude) {
    let boom = document.getElementById("boom");
    if (altitude === 10) {
        boom.style.visibility = "visible";
    } else {
        boom.style.visibility = "hidden";
    }
    await sleep(300);
    if (altitude === 150) {
        element.innerText = "💥";
    } else if (altitude === 200) {
        element.style.visibility = "hidden";
    } else if (altitude > 150) {
        element.innerText = "💨";
    }
    element.style.marginLeft = `${altitude}px`;
}


async function getWebsocketConn() {
    let element = document.getElementById("events");
    let req = new XMLHttpRequest();
    req.open("GET", document.location, true);
    req.send(null);
    req.onload = () => {
        const sessionId = req.getResponseHeader("Session_id");
        const eventSocket = new WebSocket(`ws://0.0.0.0:8000/events?session_id=${sessionId}`);
        eventSocket.onopen = () => {
            console.log(`WebSocket connection ${sessionId} established.`);
        };
        receiveData(eventSocket, element);
    }
}
