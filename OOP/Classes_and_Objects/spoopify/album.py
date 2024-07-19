from project.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs: list[Song] = []
        self.args = args
        self.published = False

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        for song in self.songs:
            if song.name == song_name:
                if self.published:
                    return f"Cannot remove songs. Album is published."
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        songs_str = '\n'.join(f"== {song.get_info()}" for song in self.songs)
        return (f"Album {self.name}\n"
                f"{songs_str}")

    def song_parameters(self):
        if self.args:
            for song in self.args:
                self.songs.append(song)
