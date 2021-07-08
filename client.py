# The client socket will be set to non-blocking because we want to routinely check for incoming messages
# inside of the event loop. Since the GUI and the socket handling code is inside the same loop, we don't want
# the socket to block execution until a new message comes in, but instead try to receive messages, and continue
# looping whether or not it receives a message

from tkinter import *
import time
from network import Network

#  First, get the name of the user in the console before opening GUI
name = input("Name: ")


# --------------------------------- GUI SETUP ----------------------------- #
root = Tk()
root.geometry("500x500")      # Set size of window to 500x500
root.resizable(False, False)

# Create a frame container for the actual chatting box (messages)
output_container = LabelFrame(root, width=480, height=400)
output_container.pack(side='top', expand=False)
output_container.pack_propagate(0)

canvas = Canvas(output_container)
scrollable_frame = Frame(canvas)
scrollbar = Scrollbar(output_container, orient="vertical", command=canvas.yview)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="s")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.yview_moveto('1.0')

output_container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

input_frame = LabelFrame(root, width=480, height=100, pady=5)
input_frame.pack(side='bottom')

t = Text(input_frame, width=480, height=4)
t.pack(padx=5, pady=5)


def send_message(event):
    user_input = t.get('1.0', 'end-2c')
    curr_time = time.localtime()
    hours = curr_time[3] % 12
    minutes = curr_time[4]
    display_output = name + "[" + str(hours) + ":" + str(minutes) + "]:  " + user_input
    msg = Message(scrollable_frame, text=display_output, anchor='w', width=480)
    msg.pack(fill='both')
    t.delete('1.0', 'end')  # Clear input field for next message

    n.send(display_output)


def show_message(message):
    output = Message(scrollable_frame, text=message, anchor='w', width=480)
    output.pack(fill='both')


# Have the enter key be the "Send" action by binding it to call the function send_message
# which takes the input in the msg box and sends it to the server + clears msg box
root.bind('<Return>', send_message)


n = Network()  # Middle man between client and server (handles sending/receiving data)

# Main event loop (updates GUI and attempts to receive messages from other clients)
while True:
    data = n.receive()  # Does not block
    if data:
        show_message(data)
    root.update_idletasks()
    root.update()

