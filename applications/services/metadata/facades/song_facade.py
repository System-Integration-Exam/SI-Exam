from entities.song import Song


def createSong(song):
    # todo persist to database

    statusMessage = "200 ok"
    return statusMessage


def getSongById(id):
    # todo get from database
    # fixed value for now
    song = Song(id, "title", 120)

    return song


def updateSong(song):
    # todo persist updates to database

    statusMessage = "200 ok"
    return statusMessage


def deleteSongById(id):
    # todo remove persisted data

    statusMessage = "200 ok"
    return statusMessage
