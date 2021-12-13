from entities.vinyl import Vinyl


def createVinyl(vinyl):
    #todo persist to database

    statusMessage = "200 ok"
    return statusMessage


def getVinylById(id):
    #todo get from database
    #fixed value for now
    vinyl = Vinyl(id, "artist", "genre") 

    return vinyl


def updateVinyl(vinyl):
    #todo persist updates to database

    statusMessage = "200 ok"
    return statusMessage
    

def deleteVinylById(id):
    #todo remove persisted data
    
    statusMessage = "200 ok"
    return statusMessage
