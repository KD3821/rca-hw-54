const eventSource = new EventSource("/events");

eventSource.onmessage = function(event) {
    const newElement = document.createElement("div");
    newElement.innerText = event.data;
    document.getElementById("events").appendChild(newElement);
};
