#black 1 white 2 in array
from checkPiece import checkPeice
from checkPiece import addPiece
from checkPiece import finalScore

skip1 = 0
skip2 = 0

def convertScore(wScore, bScore):
    
    if wScore < 10:
        wScore = "0" + str(wScore)

    if bScore < 10:
        bScore = "0" + str(bScore)

    
    finalscore = "B0" + str(bScore) + "W0" + str(wScore)
    return(finalscore)

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


def player1first(socket1, socket2):
    #player one is black (1) 
    colour1 = 1 #black
    colour2 = 2 #white
    global skip2
    global skip1
    #*****************************first chunk***************************************************
    #reading peice place
    socket1.s_appept()
    location1 = socket1.read_data()
    location1de = location1.decode("utf-8")
    print ("Reading S1:" +  str(location1de))

    if location1de == "!sur":
        sur1(socket1, socket2, location1de, "black")
        return "end"
    elif location1de == "Skip":
        skip1 = 1
        if (skip1 * skip2) > 0:
            sur1(socket1, socket2, location1de, "none")
            return "end"
        sending1 = ""
    else:
        addPiece(location1de, colour1)
        skip1 = 0
        removethis = checkPeice(float(location1de))
        print(removethis)
        sending1 = removethis



    #writing removed pieces
    print("Writing S1:" + sending1 + "Skip")
    socket1.send_data(bytes(sending1 + "Skip", "utf-8")) 
    
    #void
    socket1.s_appept()
    print ("Reading S1:" + (socket1.read_data()).decode("utf-8") )

    #******************************second chunk ********************************************

    #writing location
    if location1de == "Skip":
        print("Writing S2:" + location1de)

    else:
        location1 = bytes(("A"+location1de+removethis),"utf-8")
        print("Writing S2:" + "A"+location1de+removethis )


    socket2.send_data(location1) 

    #reading peice place
    socket2.s_appept()
    location2 = socket2.read_data()
    location2de = location2.decode("utf-8")
    print ("Reading S2:" + location2de )


    if location2de == "!sur":
        sur2(socket1, socket2, location2de, "white")
        return "end"
    elif location2de == "Skip":
        skip2 += 1
        if (skip1 * skip2) > 0:
            sur2(socket1, socket2, location2de, "none")
            return "end"
        sending2 = ""

    else:
        addPiece(location2de, colour2)
        skip2 = 0
        removethis = checkPeice(location2de)
        print(removethis)
        sending2 = removethis

    #writing score
    print("Writing S2:" + sending2 + "Skip")
    socket2.send_data(bytes(sending2 + "Skip", "utf-8")) 

    #void
    socket2.s_appept()
    print ("Reading S2:" + (socket2.read_data()).decode("utf-8") )

    #************************ third Chunk *************************************************  
    #writing location
    if location2de == "Skip":
        print("Writing S1:" + location2de)

    else:
        location2 = bytes(("A"+location2de+removethis),"utf-8")
        print("Writing S1:" + "A"+location2de+removethis )
        
    socket1.send_data(location2) 

    return


def player2first(socket1, socket2):
    #player two is black (1) 
    colour1 = 2 #black
    colour2 = 1 #white
    global skip2
    global skip1

    #*****************************first chunk***************************************************

    #reading peice place
    socket2.s_appept()
    location2 = socket2.read_data()
    location2de = location2.decode("utf-8")
    print ("Reading S2:" + location2de )

    if location2de == "!sur":
        sur2(socket1, socket2, location2de, "black")
        return "end"
    elif location2de == "Skip":
        skip2 += 1
        if (skip1 * skip2) > 0:
            sur2(socket1, socket2, location2de, "none")
            return "end"
        sending2 = ""

    else:
        addPiece(location2de, colour2)
        skip2 = 0
        removethis = checkPeice(location2de)
        print(removethis)
        sending2 = removethis


    #writing score
    print("Writing S2:" + sending2 + "Skip")
    socket2.send_data(bytes(sending2 + "Skip", "utf-8")) 

    #void
    socket2.s_appept()
    print ("Reading S2:" + (socket2.read_data()).decode("utf-8") )
    #******************************second chunk ********************************************


 #writing location
    if location2de == "Skip":
        print("Writing S1:" + location2de)

    else:
        location2 = bytes(("A"+location2de+removethis),"utf-8")
        print("Writing S1:" + "A"+location2de+removethis )

    socket1.send_data(location2) 

   #reading peice place
    socket1.s_appept()
    location1 = socket1.read_data()
    location1de = location1.decode("utf-8")
    print ("Reading S1:" +  location1de)

    if location1de == "!sur":
        sur1(socket1, socket2, location1de, "white")
        return "end"
    elif location1de == "Skip":
        skip1 = 1
        if (skip1 * skip2) > 0:
            sur1(socket1, socket2, location1de, "none")
            return "end"
        sending1 = ""
    else:
        addPiece(location1de, colour1)
        skip1 = 0
        removethis = checkPeice(float(location1de))
        print(removethis)
        sending1 = removethis


    #writing removed pieces
    print("Writing S1:" + sending1 + "Skip")
    socket1.send_data(bytes(sending1 + "Skip", "utf-8")) 
    
    #void
    socket1.s_appept()
    print ("Reading S1:" + (socket1.read_data()).decode("utf-8") )


    #************************ third Chunk *************************************************


    #writing location
    if location1de == "Skip":
        print("Writing S2:" + location1de)

    else:
        location1 = bytes(("A"+location1de+removethis),"utf-8")
        print("Writing S2:" + "A"+location1de+removethis )

    socket2.send_data(location1) 

    return

def sur1(socket1, socket2, i, colour):
    WhiteScore = 0
    BlackScore = 0
 
    if i == "!sur":
        if colour == "black": #black surrendered 
            WhiteScore = 1

        elif colour == "white": #white surrendered
            BlackScore = 1
    else:
        score = finalScore()
        BlackScore = score[0]
        WhiteScore = score[1]
    
    send = bytes(convertScore(WhiteScore, BlackScore),"utf-8")

    #writing End Sequence
    print("Writing S1:!sur")
    socket1.send_data(b"!sur") 

    #void
    socket1.s_appept()
    print ("Reading S1:" + (socket1.read_data()).decode("utf-8") )


    #writing End Sequence
    print("Writing S2:!sur")
    socket2.send_data(b"!sur") 

    #WINR
    socket2.s_appept()
    location2 = socket2.read_data()
    print ("Reading S2:" + location2.decode("utf-8") )

    #writing score
    print("Writing S2:" + send.decode("utf-8") )
    socket2.send_data(send) 

    #WINR
    socket1.s_appept()
    print ("Reading S1:" + (socket1.read_data()).decode("utf-8") )


    #writing score
    print("Writing S1:" + send.decode("utf-8") )
    socket1.send_data(send) 

def sur2(socket1, socket2, i, colour):

    WhiteScore = 0
    BlackScore = 0
 
    if i == "!sur":
        if colour == "black": #black surrendered 
            WhiteScore = 1

        elif colour == "white": #white surrendered
            BlackScore = 1
    else:
        score = finalScore()
        BlackScore = score[0]
        WhiteScore = score[1]
    
    send = bytes(convertScore(WhiteScore, BlackScore),"utf-8")


    #writing End Sequence
    print("Writing S2: !sur" )
    socket2.send_data(b"!sur") 

    #void
    socket2.s_appept()
    print ("Reading S2:" + (socket2.read_data()).decode("utf-8") )


    #writing End Sequence
    print("Writing S1: !sur" )
    socket1.send_data(b"!sur") 

    #void
    socket1.s_appept()
    location1 = socket1.read_data()
    print ("Reading S1:" + location1.decode("utf-8") )

    #writing score
    print("Writing S1:" + send.decode("utf-8") )
    socket1.send_data(send) 

    #void
    socket2.s_appept()
    print ("Reading S1:" + (socket2.read_data()).decode("utf-8") )


    #writing location
    print("Writing S2:" + send.decode("utf-8") )
    socket2.send_data(send) 


