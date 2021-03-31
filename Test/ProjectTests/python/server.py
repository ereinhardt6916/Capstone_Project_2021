#https://github.com/Net4ky/PPsocket

import time

from shelper import SocketHelper

sockethelper = SocketHelper("localhost",10231)


mesg = [b"1111Whit",b"A9.9",b"W003B050",b"A1.1",b"W020B000",b"A2.2",b"W030",b"A3.3",b"R2.2",b"A1.2",b"R1.1!sur",b"void",b"W020B010"]
for i in mesg:
    sockethelper.s_appept()
    print ("Reading:" + str(sockethelper.read_data()))
    time.sleep(1)
    print("Writing:" + str(i))
    sockethelper.send_data(i) 


sockethelper.close_socket
