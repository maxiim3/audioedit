from pydub import AudioSegment, audio_segment
from pydub import effects
from pydub import playback
from pathlib import Path
from os import system
from os import listdir
from os import path
from glob import glob

#   ............ F I E L D S ...........

audio_edit = AudioSegment
audio_fx = effects
audio_play = playback

audiofile_list = list


#   ............ p a t h s  ...........

audio_path = Path(
    "SOURCE_FILE")
audiofile_list = glob(f"{audio_path}/*.m4a")


#   ............ M E T H O D S ...........

audio_part_01 = audio_edit.from_file(f"{audiofile_list[0]}", format="m4a")
