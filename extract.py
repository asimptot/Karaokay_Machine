import sys
sys.path.append(r'C:\\Projects\\Karaoke_Manatree')
from init import *

class Karaokay():
    def play_karaoke(self):
        Setup.download_chrome(self)
        Setup.go_to_site(self)
        Setup.upload_download(self)
        Setup.close_browser(self)
        Setup.unzip(self)
        Setup.rename(self)
        Setup.move_file(self)


k = Karaokay()
k.play_karaoke()