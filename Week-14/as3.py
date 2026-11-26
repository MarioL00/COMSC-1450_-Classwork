#Question 1
class Playlist():
    def __init__(self, title):
      self.title = title
      self.songs = []

    def add_song(self, song_name):
      self.songs.append(song_name)

    def remove_song(self, song_name):
        if song_name in self.songs:
           self.songs.remove(song_name)
        else:
           print("Song not found.")

    def get_summary(self):
       return f"Playlist: {self.title} | Total Songs: {len(self.songs)}"
           
playlist1 = Playlist("Road Trip") 
playlist1.add_song("Can I")
playlist1.add_song("Red Button")
playlist1.add_song("Astrothunder")
playlist1.remove_song("Red Button")
print(playlist1.get_summary()) 


#Question 2
class GiftCard():
    def __init__(self, owner):
      self.__owner = owner
      self.__balance = 0.0

    def get_balance(self):
        return self.__balance

    def reload(self, amount):
        if amount > 0:
          self.__balance += amount

    def spend(self,amount):
        if amount <= self.__balance:
          self.__balance -= amount
        else: 
           print("Insufficient gift card balance!")

gcard1 = GiftCard("Jordan")
gcard1.reload(50)
gcard1.spend(75)
gcard1.spend(20)

print(gcard1.get_balance())
print(gcard1.__balance)


#Question 3
class MediaItem():
    def __init__(self, title, minutes):
        self.title = title
        self.minutes = minutes
    def play(self):
        return f" Playing {self.title} ({self.minutes} mins)"

class PodcastEpisode(MediaItem):   
    def __init__(self, title, minutes, host):
        super().__init__(title, minutes)
        self.host = host
    def play(self):
        return f"{super().play()} - Hosted by {self.host}" 

podcast1 = PodcastEpisode("Tech Talk", 45, "Alex")
print(podcast1.play()) 


#Question 4
class Character():
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage.")

class ArmoredKnight(Character):
    def __init__(self, name, health, armor):
        super().__init__(name, health)
        self.armor = armor
    def take_damage(self, amount):
        print(f"Armor blocks {self.armor} damage!")
        reduced_damage = max(0, amount - self.armor)
        super().take_damage(reduced_damage)

knight1 = ArmoredKnight("Arthur", 100, 15)
knight1.take_damage(40)
print(knight1.health) 