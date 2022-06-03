document.addEventListener('DOMContentLoaded', function () {

    const buttonOpen = document.querySelector("#open_connection")

    const buttonClose = document.querySelector("#close_connection")

    const textContainer = document.querySelector("#container_log_text")

    buttonOpen.onclick = function () {

        textContainer.innerHTML = ''
        buttonOpen.disabled = true
        buttonOpen.style.background = '#8b8b8b'

        let webSocket = new WebSocket('ws://localhost:12345/')

        webSocket.onopen = function () {
            webSocket.send('is_open')
            textContainer.innerHTML = ''
            buttonOpen.disabled = true
            buttonOpen.style.background = '#8b8b8b'
            alert('Connection is open')
        }


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

            buttonOpen.disabled = false
            buttonOpen.style.background = '#2fb380'


            if (webSocket.readyState === 1) {
                webSocket.close(1000, "Work ended");
                alert('Connection closed')
            } else {
                alert('The connection was not opened')
            }
        }
    }

    buttonClose.onclick = function () {

        alert('The connection was not opened')
    }

}, false)
