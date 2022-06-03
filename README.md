# Display_logs_by_websocket

This programm, can display a log file in your browser. 
For get started, you have to clone the ptoject on the own computer and install/import 3 modules (asyncio, os, websockets) in your python console
and change the path to the log file in a variable 'filename', also you can integrate this cod in own project.
How does it work? If (last date change) files was changed, the programm send message to a client. After star, the programm will send last 100 strings
to your browser and all change text in a file after, if (last date change) files change.
