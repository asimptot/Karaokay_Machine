import sys
sys.path.append(r'C:\\Projects\\Karaoke_Voice_Commands')
from init import *

class Karaokay():
    def play_karaoke(self):
        Setup.play_rules_instrumental(self)
        Setup.play_rules_lyrics(self)

k = Karaokay()
k.play_karaoke()

