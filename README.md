This program is a local network chatbox. It uses the built-in
standard library python modules: socket, _thread, and pickle

It also uses tkinter for the GUI.
Note: The Tkinter module should come with your python3 installation,
if not then you will need to install this dependency.

How to Setup
-----------

In order to make this work for your network, you must change a couple
lines of the code. Do as follows:

1) In server.py, change the value of server to your own local ip-address
   The variable definition is on line 6

(OPTIONARY) You may also change the port number to whatever you'd like to
use, as well as the max_connections to allow for more clients to connect
to your server

2) In network.py, you also much change the self.server ip-address to your
   own. This code is found in the constructor of the Network class.
   
Note: If you change the port number in server.py, you must change the 
self.port number in network.py as well


How to run
----------

1) Run server.py on one computer in your network
2) Run client.py on any computer connected to your network, and it will
   connect to your server and allow for back-and-forth communication


How it works
------------
Each client is connected to the server via a socket connection. The server,
when connected to the client, runs a threaded function that will receive
a client's message and then distribute the client's message to all the
other clients connected to the server.

The client itself has the ability to type messages, and hit enter to send
them to the server. Their own message will appear on their screen. The 
clients will continuously look for received messages, and will display them
if the server sends a distributed message. Thus, a chatbox. 


Credit
------

I used many online sources to help me implement this project, from learning
basic python syntax to the teachings of how sockets, networks work. Two big 
sources that helped with the implementation are:

(Youtube) FreeCodeCamp.org video: "Python Online Multiplayer Game Development
          Tutorial" given by the programmer Tech With Tim
          https://www.youtube.com/watch?v=McoDjOCb2Zo

(Blog) Jose Salvatierra - "Scollable Frames in Tkinter"
          https://blog.tecladocode.com/tkinter-scrollable-frames/

Much credit to these two sources. Definitely check them out if you are looking
to work on sockets in python (src 1), or GUI development with Tkinter (src 2)
