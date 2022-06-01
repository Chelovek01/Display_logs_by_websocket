document.addEventListener('DOMContentLoaded', function () {

    const buttonOpen = document.querySelector("#open_connection")

    const buttonClose = document.querySelector("#close_connection")

    const textContainer = document.querySelector("#container_log_text")

    buttonOpen.onclick = function () {


        let webSocket = new WebSocket('ws://localhost:12345/')

        webSocket.onopen = function () {
            webSocket.send('is_open')
        }
        alert('Open')

        webSocket.onmessage = function (event) {

            let text = event.data.split('\n')
            for (let i = 0; i < text.length; i++) {
                if (text[i].length !== 0) {
                    let li = document.createElement("li")
                    li.append(text[i])
                    textContainer.append(li)
                }
            }
        }


        buttonClose.onclick = function () {

            if (webSocket.readyState === 1) {
                webSocket.close(1000, "работа закончена");
                alert('конец')
            } else {
                alert('соединеие не было открыто')
            }
            alert("Сlose")
        }
    }


}, false)


// function startSocket() {
//     var ws = new WebSocket("ws://localhost:8765/")
//     ws.onopen = function(event) {
//         ws.send("Sent this from client.js")
//     }
// }
// startSocket();