from lib.music_tracker import MusicTracker 

def test_of_the_tracker():
    tracker = MusicTracker()
    tracker.song_names.append("WHAM - Last Christmas")
    assert tracker.album()