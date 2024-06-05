>>> # Plays the note A (a sine wave of frequency 440HZ)
>>> import numpy as np
>>> make_frame = lambda t: 2*[ np.sin(440 * 2 * np.pi * t) ]
>>> clip = AudioClip(make_frame, duration=5)
>>> clip.preview()

>>> fl = lambda gf,t : gf(t)[int(t):int(t)+50, :]
>>> newclip = clip.fl(fl, apply_to='mask')


>>> # plays the clip (and its mask and sound) twice faster
>>> newclip = clip.fl_time(lambda: 2*t, apply_to=['mask', 'audio'])
>>>
>>> # plays the clip starting at t=3, and backwards:
>>> newclip = clip.fl_time(lambda: 3-t)

>>> newclip = clip.fx(resize, 0.2, method='bilinear')

>>> newclip = resize(clip, 0.2, method='bilinear')

>>> from moviepy.video.fx import volumex, resize, mirrorx
>>> clip.fx( volumex, 0.5).fx( resize, 0.3).fx( mirrorx )
>>> # Is equivalent, but clearer than
>>> resize( volumex( mirrorx( clip ), 0.5), 0.3)

>>> # prints the maximum of red that is contained
>>> # on the first line of each frame of the clip.
>>> from moviepy.editor import VideoFileClip
>>> myclip = VideoFileClip('myvideo.mp4')
>>> print ( [frame[0,:,0].max()
             for frame in myclip.iter_frames()])

>>> # cut the last two seconds of the clip:
>>> newclip = clip.subclip(0,-2)

>>> snd = AudioFileClip("song.wav")
>>> snd.close()
>>> snd = AudioFileClip("song.mp3", fps = 44100)
>>> second_reader = snd.coreader()
>>> second_reader.close()
>>> snd.close()
>>> with AudioFileClip(mySoundArray, fps=44100) as snd:  # from a numeric array
>>>     pass  # Close is implicitly performed by context manager.

>>> fl = lambda gf,t : gf(t)[int(t):int(t)+50, :]
>>> newclip = clip.fl(fl, apply_to='mask')

>>> # plays the clip (and its mask and sound) twice faster
>>> newclip = clip.fl_time(lambda: 2*t, apply_to=['mask', 'audio'])
>>>
>>> # plays the clip starting at t=3, and backwards:
>>> newclip = clip.fl_time(lambda: 3-t)

>>> newclip = clip.fx(resize, 0.2, method='bilinear')

>>> newclip = resize(clip, 0.2, method='bilinear')

>>> from moviepy.video.fx import volumex, resize, mirrorx
>>> clip.fx( volumex, 0.5).fx( resize, 0.3).fx( mirrorx )
>>> # Is equivalent, but clearer than
>>> resize( volumex( mirrorx( clip ), 0.5), 0.3)

>>> # prints the maximum of red that is contained
>>> # on the first line of each frame of the clip.
>>> from moviepy.editor import VideoFileClip
>>> myclip = VideoFileClip('myvideo.mp4')
>>> print ( [frame[0,:,0].max()
             for frame in myclip.iter_frames()])

>>> # cut the last two seconds of the clip:
>>> newclip = clip.subclip(0,-2)

>>> fl = lambda gf,t : gf(t)[int(t):int(t)+50, :]
>>> newclip = clip.fl(fl, apply_to='mask')

>>> # plays the clip (and its mask and sound) twice faster
>>> newclip = clip.fl_time(lambda: 2*t, apply_to=['mask', 'audio'])
>>>
>>> # plays the clip starting at t=3, and backwards:
>>> newclip = clip.fl_time(lambda: 3-t)

>>> newclip = clip.fx(resize, 0.2, method='bilinear')

>>> newclip = resize(clip, 0.2, method='bilinear')

>>> from moviepy.video.fx import volumex, resize, mirrorx
>>> clip.fx( volumex, 0.5).fx( resize, 0.3).fx( mirrorx )
>>> # Is equivalent, but clearer than
>>> resize( volumex( mirrorx( clip ), 0.5), 0.3)

>>> # prints the maximum of red that is contained
>>> # on the first line of each frame of the clip.
>>> from moviepy.editor import VideoFileClip
>>> myclip = VideoFileClip('myvideo.mp4')
>>> print ( [frame[0,:,0].max()
             for frame in myclip.iter_frames()])


>>> # cut the last two seconds of the clip:
>>> newclip = clip.subclip(0,-2)

