class MusicTracker:
    def __init__(self):
        self.song_names = []

    def add_song(self, new_song):
        self.song_names.append(new_song)

    def album(self):
        in_album = "I've listened to:"
        in_album += ','.join(self.song_names)
        return in_album  
