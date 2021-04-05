#https://github.com/Net4ky/PPsocket

import time
from shelper import SocketHelper


port1 = 10231
port2 = 10236
host1 = "localhost"
host2 = "localhost"

socket1 = SocketHelper(host1,port1)
socket2 = SocketHelper(host2,port2)

socket1.s_appept()
colour1 = socket1.read_data()
print ("Reading S1:" + colour1.decode("utf-8") )
print("Writing S1:" + b"0000,Whit".decode("utf-8") )
socket1.send_data(b"0000,Blac")

socket2.s_appept()
colour2 = socket2.read_data()
print ("Reading S2:" + colour2.decode("utf-8") )
print("Writing S2:" + b"1111,Blac".decode("utf-8") )
socket2.send_data(b"1111,Whit")

socket2.s_appept()
colour2 = socket2.read_data()
print ("Reading S2:" + colour2.decode("utf-8") )


# b needed because we can only sen bytes object in python, need to decode it to get a string
mesg = [b"W001B050",b"W002B050.9",b"W003B050",b"W004B050",b"W005B050.9",b"W006B050",b"W007B070",b"W008B080",b"W009B090.9",b"W0010B010"]
for i in mesg:
    
    #reading peice place
    socket1.s_appept()
    location1 = socket1.read_data()
    print ("Reading S1:" + location1.decode("utf-8") )
    
    #writing score
    print("Writing S1:" + i.decode("utf-8") )
    socket1.send_data(i) 
    
    #void
    socket1.s_appept()
    print ("Reading S1:" + (socket1.read_data()).decode("utf-8") )



    #writing location
    location1 = bytes(("A"+location1.decode("utf-8")),"utf-8")
    print("Writing S2:" + location1.decode("utf-8") )
    socket2.send_data(location1) 

    #reading peice place
    socket2.s_appept()
    location2 = socket2.read_data()
    print ("Reading S2:" + location2.decode("utf-8") )

    #writing score
    print("Writing S2:" + i.decode("utf-8") )
    socket2.send_data(i) 

    #void
    socket2.s_appept()
    print ("Reading S2:" + (socket2.read_data()).decode("utf-8") )



    #writing location
    location2 = bytes(("A"+location2.decode("utf-8")),"utf-8")
    print("Writing S1:" + location2.decode("utf-8") )
    socket1.send_data(location2) 



socket1.close_socket
socket2.close_socket
