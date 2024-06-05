from moviepy.audio.fx.volumex import volumex
newaudio = audioclip.fx( vfx.volumex, 0.5)

import moviepy.audio.fx.all as afx
newaudio = (audioclip.afx( vfx.normalize)
                     .afx( vfx.volumex, 0.5)
                     .afx( vfx.audio_fadein, 1.0)
                     .afx( vfx.audio_fadeout, 1.0))

from moviepy.editor import *

>>> from moviepy.editor import *
>>> videoclip = VideoFileClip('myvideo.mp4')
>>> music = AudioFileClip('music.ogg')
>>> audio = afx.audio_loop( music, duration=videoclip.duration)
>>> videoclip.set_audio(audio)

>>> from moviepy.editor import *
>>> videoclip = VideoFileClip('myvideo.mp4').fx(afx.audio_normalize)

>>> newclip = volumex(clip, 2.0) # doubles audio volume
>>> newclip = clip.fx( volumex, 0.5) # half audio, use with fx
>>> newclip = clip.volumex(2) # only if you used "moviepy.editor"

