class Song:
    
    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance Attributes 
        self.name = name
        self.artist = artist
        self.genre = genre

        
        self.add_song_to_count()

        # Add genre and artist to their respective class-level lists
        self.add_to_genres()
        self.add_to_artists()

        # Increment genre and artist counts
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):

        """Increments the song count by 1."""
        cls.count += 1

    def add_to_genres(self):

        """Adds genre to the class-level genres list if it's unique."""
        if self.genre not in self.__class__.genres:
            self.__class__.genres.append(self.genre)

    def add_to_artists(self):

        """Adds artist to the class-level artists list if it's unique."""
        if self.artist not in self.__class__.artists:
            self.__class__.artists.append(self.artist)

    def add_to_genre_count(self):
        
        """Updates the genre_count dictionary by incrementing the count for the genre."""
        if self.genre in self.__class__.genre_count:
            self.__class__.genre_count[self.genre] += 1
        else:
            self.__class__.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        """Updates the artist_count dictionary by incrementing the count for the artist."""
        if self.artist in self.__class__.artist_count:
            self.__class__.artist_count[self.artist] += 1
        else:
            self.__class__.artist_count[self.artist] = 1
