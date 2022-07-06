from os import path
from pydub import AudioSegment

# files
src = input("In: ")
dst = input("Out: ")

# convert mp3 to wav
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")