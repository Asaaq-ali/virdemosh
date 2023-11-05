from source.AnonXMusic.core.bot import Anony
from source.AnonXMusic.core.dir import dirr
from source.AnonXMusic.core.git import git
from source.AnonXMusic.core.userbot import Userbot
from source.AnonXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
