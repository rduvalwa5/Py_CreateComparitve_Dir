import os, platform, time
import pymysql.cursors


class Collect_Data:

    def __init__(self):
        print("*************** Node Name is ", platform.uname().node)
        self.hostname = platform.uname().node
        if self.hostname == "MaxBookPro17OSX.local":
            self.base = "/Users/rduvalwa2/iTunes/iTunes Media/Music"
            
        self.fName = self.createName()
        print(self.fName)
        try:
            self.filObj = open(self.fName,"w")
        except Exception as e:
            print(e)
        
            
    
    def get_albums(self):
#        base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        albums = []
        index = 0
        artists = self.get_music_artist()
        for a in artists:
            artist = a[1]
            if os.path.isdir(self.base + "/" + artist):
                artist_albums = os.listdir(self.base + "/" + artist)
                for album in artist_albums:
                    if album != '.DS_Store':
                        albums.append((index, artist, album))
                        index = index + 1
        return albums

    def get_artist(self):
        artist = []
        index = 0
        musicDirs = os.listdir(self.base)
        for directory in musicDirs:
            if os.path.isdir(self.base + "/" + directory):
                artist.append((index, directory))
                index = index + 1
        return artist

    def get_all_songs(self):
#        base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        albums = []
        songs = []
        artist = self.get_artist()
        for a in artist:
            if os.path.isdir(self.base + "/" + a[1]):
                artist_albums = os.listdir(self.base + "/" + a[1])
                for album in artist_albums:
                    if album != '.DS_Store':
                        albums.append((a, album))
                        album_songs = os.listdir(self.base + "/" + a[1] + "/" + album)
                        for song in album_songs:
                            if song != '.DS_Store' and song != 'side1.mp3' and song != 'side2.mp3' and song != 'side3.mp3' and song != 'side4.mp3':
                                songs.append(a[1] + "," + album + ","  + song + "\n")
        return songs

    """
    Write Inventory File
    """

    def Write_Inventory_File(self): 

        hostSongs = self.get_all_songs()
        for dat in hostSongs:
            print(str(dat))
            self.filObj.write(str(dat))
        self.filObj.close()
            
    def get_songs(self, artist, album='all'):
        base = self.base
        albums = []
        songs = []
        newIndex = 0
        if os.path.isdir(base + "/" + artist):
                artist_albums = os.listdir(base + "/" + artist)
#                print("artist_albums: ", artist_albums)
                for al in artist_albums:
                        if al != '.DS_Store':
                            albums.append((artist, al))
                            album_songs = os.listdir(base + "/" + artist + "/" + al)
                            for song in album_songs:
                                    songs.append((artist,al,song))
        return songs

        
    def createName(self):
        self.myTime = time.time_ns()
        self.localFilename = self.hostname + str(self.myTime) + ".txt"
        print(self.localFilename)
        return(self.localFilename)

        
if __name__ == '__main__':
    
    hostData = Collect_Data()
    hostData.Write_Inventory_File()
