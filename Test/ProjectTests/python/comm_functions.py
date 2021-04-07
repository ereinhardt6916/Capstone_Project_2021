#black 1 white 2 in array
from checkPiece import checkPeice
from checkPiece import addPiece




def startup(socket1, socket2):
    
    #read response from socket1
    socket1.s_appept()
    colour1 = socket1.read_data()
    print ("Reading S1:" + colour1.decode("utf-8") )
    
    #read response from socket2
    socket2.s_appept()
    colour2 = socket2.read_data()
    print ("Reading S2:" + colour2.decode("utf-8") )
    
    if (colour1 == colour2) or (colour1 == b"Blac"):

        print("Writing S1:" + b"0000Blac".decode("utf-8") )
        socket1.send_data(b"0000Blac")

        print("Writing S2:" + b"1111Whit".decode("utf-8") )
        socket2.send_data(b"1111Whit")

        socket2.s_appept()
        colour2 = socket2.read_data()
        print ("Reading S2:" + colour2.decode("utf-8") )

        colour1 = b"Blac"

    elif colour1 == b"Whit":

        print("Writing S1:" + b"1111Whit".decode("utf-8") )
        socket1.send_data(b"1111Whit")

        
        print("Writing S2:" + b"0000Blac".decode("utf-8") )
        socket2.send_data(b"0000Blac")

        socket1.s_appept()
        colour1 = socket1.read_data()
        print ("Reading S1:" + colour1.decode("utf-8") )


    return colour1


def player1first(socket1, socket2, score):
    #player one is black (1) 
    colour1 = 1 #black
    colour2 = 2 #white

    #*****************************first chunk***************************************************
    #reading peice place
    socket1.s_appept()
    location1 = socket1.read_data()
    location1de = location1.decode("utf-8")
    print ("Reading S1:" +  location1de)

    if location1de == "!sur":
        sur1(socket1, socket2, location1)
        return "end"
    else:
        addPiece(location1de, colour1)

    removethis = checkPeice(location1de)
    print(removethis)
    sending1 = score.decode("utf-8")+removethis

    #writing score
    print("Writing S1:" + sending1)
    socket1.send_data(bytes(sending1, "utf-8")) 
    
    #void
    socket1.s_appept()
    print ("Reading S1:" + (socket1.read_data()).decode("utf-8") )

    #******************************second chunk ********************************************

    #writing location
    location1 = bytes(("A"+location1de+removethis),"utf-8")
    print("Writing S2:" + "A"+location1de+removethis )
    socket2.send_data(location1) 

    #reading peice place
    socket2.s_appept()
    location2 = socket2.read_data()
    location2de = location2.decode("utf-8")
    print ("Reading S2:" + location2de )

    if location2de == "!sur":
        sur2(socket1, socket2, location2)
        return "end"
    else:
        addPiece(location2de, colour2)

    removethis = checkPeice(location2de)
    print(removethis)

    sending2 = score.decode("utf-8")+removethis

    #writing score
    print("Writing S2:" + sending2 )
    socket2.send_data(bytes(sending2, "utf-8")) 

    #void
    socket2.s_appept()
    print ("Reading S2:" + (socket2.read_data()).decode("utf-8") )

    #************************ third Chunk *************************************************
    #writing location
    location2 = bytes(("A"+location2de+removethis),"utf-8")
    print("Writing S1:" + "A"+location2de+removethis )
    socket1.send_data(location2) 

    return


def player2first(socket1, socket2, score):
    #player two is black (1) 
    colour1 = 2 #black
    colour2 = 1 #white

    #*****************************first chunk***************************************************

    #reading peice place
    socket2.s_appept()
    location2 = socket2.read_data()
    location2de = location2.decode("utf-8")
    print ("Reading S2:" + location2de )

    if location2de == "!sur":
        sur2(socket1, socket2, location2)
        return "end"
    else:
        addPiece(location2de, colour2)

    removethis = checkPeice(location2de)
    print(removethis)

    sending2 = score.decode("utf-8")+removethis


    #writing score
    print("Writing S2:" + sending2 )
    socket2.send_data(bytes(sending2, "utf-8")) 
    
 #void
    socket2.s_appept()
    print ("Reading S2:" + (socket2.read_data()).decode("utf-8") )

    #******************************second chunk ********************************************


    #writing location
    location2 = bytes(("A"+location2de+removethis),"utf-8")
    print("Writing S1:" + "A"+location2de+removethis )
    socket1.send_data(location2) 

   #reading peice place
    socket1.s_appept()
    location1 = socket1.read_data()
    location1de = location1.decode("utf-8")
    print ("Reading S1:" +  location1de)

    if location1de == "!sur":
        sur1(socket1, socket2, location1)
        return "end"
    else:
        addPiece(location1de, colour1)

    removethis = checkPeice(location1de)
    print(removethis)
    sending1 = score.decode("utf-8")+removethis

    #writing score
    print("Writing S1:" + sending1)
    socket1.send_data(bytes(sending1, "utf-8")) 

    #void
    socket1.s_appept()
    print ("Reading S1:" + (socket1.read_data()).decode("utf-8") )

    #************************ third Chunk *************************************************


    #writing location
    location1 = bytes(("A"+location1de+removethis),"utf-8")
    print("Writing S2:" + "A"+location1de+removethis )
    socket2.send_data(location1) 

    return

def sur1(socket1, socket2, i):
    #writing End Sequence
    print("Writing S1:" + i.decode("utf-8") )
    socket1.send_data(i) 

    #void
    socket1.s_appept()
    print ("Reading S1:" + (socket1.read_data()).decode("utf-8") )


    #writing End Sequence
    print("Writing S2:" + i.decode("utf-8") )
    socket2.send_data(i) 

    #WINR
    socket2.s_appept()
    location2 = socket2.read_data()
    print ("Reading S2:" + location2.decode("utf-8") )

    #writing score
    print("Writing S2:" + b"W010B005".decode("utf-8") )
    socket2.send_data(b"W010B005") 

    #WINR
    socket1.s_appept()
    print ("Reading S1:" + (socket1.read_data()).decode("utf-8") )


    #writing score
    print("Writing S1:" + b"W010B005".decode("utf-8") )
    socket1.send_data(b"W010B005") 

def sur2(socket1, socket2, i):

    #writing End Sequence
    print("Writing S2:" + i.decode("utf-8") )
    socket2.send_data(i) 

    #void
    socket2.s_appept()
    print ("Reading S2:" + (socket2.read_data()).decode("utf-8") )


    #writing End Sequence
    print("Writing S1:" + i.decode("utf-8") )
    socket1.send_data(i) 

    #void
    socket1.s_appept()
    location1 = socket1.read_data()
    print ("Reading S1:" + location1.decode("utf-8") )

    #writing score
    print("Writing S1:" + b"W010B005".decode("utf-8") )
    socket1.send_data(b"W010B005") 

    #void
    socket2.s_appept()
    print ("Reading S1:" + (socket2.read_data()).decode("utf-8") )


    #writing location
    print("Writing S2:" + b"W010B005".decode("utf-8") )
    socket2.send_data(b"W010B005") 