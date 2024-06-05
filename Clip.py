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

>>> clip.set_position((45,150)) # x=45, y=150
>>>
>>> # clip horizontally centered, at the top of the picture
>>> clip.set_position(("center","top"))
>>>
>>> # clip is at 40% of the width, 70% of the height:
>>> clip.set_position((0.4,0.7), relative=True)
>>>
>>> # clip's position is horizontally centered, and moving up !
>>> clip.set_position(lambda t: ('center', 50+t) )

>>> # cut the last two seconds of the clip:
>>> newclip = clip.subclip(0,-2)

>>> # The scene between times t=3s and t=6s in ``clip`` will be
>>> # be played twice slower in ``newclip``
>>> newclip = clip.subapply(lambda c:c.speedx(0.5) , 3,6)

>>> # slow down clip 50% and make it a gif
>>> myClip.speedx(0.5).to_gif('myClip.gif')

>>> from moviepy.editor import VideoFileClip
>>> clip = VideoFileClip("myvideo.mp4").subclip(100,120)
>>> clip.write_videofile("my_new_video.mp4")
>>> clip.close()

>>> clip = VideoFileClip("myHolidays.mp4")
>>> clip.close()
>>> with VideoFileClip("myMaskVideo.avi") as clip2:
>>>    pass  # Implicit close called by context manager.

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

>>> clip.set_position((45,150)) # x=45, y=150
>>>
>>> # clip horizontally centered, at the top of the picture
>>> clip.set_position(("center","top"))
>>>
>>> # clip is at 40% of the width, 70% of the height:
>>> clip.set_position((0.4,0.7), relative=True)
>>>
>>> # clip's position is horizontally centered, and moving up !
>>> clip.set_position(lambda t: ('center', 50+t) )

>>> # cut the last two seconds of the clip:
>>> newclip = clip.subclip(0,-2)

>>> # The scene between times t=3s and t=6s in ``clip`` will be
>>> # be played twice slower in ``newclip``
>>> newclip = clip.subapply(lambda c:c.speedx(0.5) , 3,6)

>>> # slow down clip 50% and make it a gif
>>> myClip.speedx(0.5).to_gif('myClip.gif')

>>> from moviepy.editor import VideoFileClip
>>> clip = VideoFileClip("myvideo.mp4").subclip(100,120)
>>> clip.write_videofile("my_new_video.mp4")
>>> clip.close()

>>> clip = ImageClip("myHouse.jpeg")
>>> clip = ImageClip( someArray ) # a Numpy array represent

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

>>> clip.set_position((45,150)) # x=45, y=150
>>>
>>> # clip horizontally centered, at the top of the picture
>>> clip.set_position(("center","top"))
>>>
>>> # clip is at 40% of the width, 70% of the height:
>>> clip.set_position((0.4,0.7), relative=True)
>>>
>>> # clip's position is horizontally centered, and moving up !
>>> clip.set_position(lambda t: ('center', 50+t) )

>>> # cut the last two seconds of the clip:
>>> newclip = clip.subclip(0,-2)

>>> # The scene between times t=3s and t=6s in ``clip`` will be
>>> # be played twice slower in ``newclip``
>>> newclip = clip.subapply(lambda c:c.speedx(0.5) , 3,6)

>>> # slow down clip 50% and make it a gif
>>> myClip.speedx(0.5).to_gif('myClip.gif')

>>> from moviepy.editor import VideoFileClip
>>> clip = VideoFileClip("myvideo.mp4").subclip(100,120)
>>> clip.write_videofile("my_new_video.mp4")
>>> clip.close()

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

>>> clip.set_position((45,150)) # x=45, y=150
>>>
>>> # clip horizontally centered, at the top of the picture
>>> clip.set_position(("center","top"))
>>>
>>> # clip is at 40% of the width, 70% of the height:
>>> clip.set_position((0.4,0.7), relative=True)
>>>
>>> # clip's position is horizontally centered, and moving up !
>>> clip.set_position(lambda t: ('center', 50+t) )

>>> # cut the last two seconds of the clip:
>>> newclip = clip.subclip(0,-2)

>>> # The scene between times t=3s and t=6s in ``clip`` will be
>>> # be played twice slower in ``newclip``
>>> newclip = clip.subapply(lambda c:c.speedx(0.5) , 3,6)

>>> # slow down clip 50% and make it a gif
>>> myClip.speedx(0.5).to_gif('myClip.gif')

>>> from moviepy.editor import VideoFileClip
>>> clip = VideoFileClip("myvideo.mp4").subclip(100,120)
>>> clip.write_videofile("my_new_video.mp4")
>>> clip.close()

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

>>> # Find all the available fonts which contain "Courier"
>>> print ( TextClip.search('Courier', 'font') )

>>> clip.set_position((45,150)) # x=45, y=150
>>>
>>> # clip horizontally centered, at the top of the picture
>>> clip.set_position(("center","top"))
>>>
>>> # clip is at 40% of the width, 70% of the height:
>>> clip.set_position((0.4,0.7), relative=True)
>>>
>>> # clip's position is horizontally centered, and moving up !
>>> clip.set_position(lambda t: ('center', 50+t) )

>>> # cut the last two seconds of the clip:
>>> newclip = clip.subclip(0,-2)

>>> # The scene between times t=3s and t=6s in ``clip`` will be
>>> # be played twice slower in ``newclip``
>>> newclip = clip.subapply(lambda c:c.speedx(0.5) , 3,6)

>>> # slow down clip 50% and make it a gif
>>> myClip.speedx(0.5).to_gif('myClip.gif')


>>> from moviepy.editor import VideoFileClip
>>> clip = VideoFileClip("myvideo.mp4").subclip(100,120)
>>> clip.write_videofile("my_new_video.mp4")
>>> clip.close()

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

>>> clip.set_position((45,150)) # x=45, y=150
>>>
>>> # clip horizontally centered, at the top of the picture
>>> clip.set_position(("center","top"))
>>>
>>> # clip is at 40% of the width, 70% of the height:
>>> clip.set_position((0.4,0.7), relative=True)
>>>
>>> # clip's position is horizontally centered, and moving up !
>>> clip.set_position(lambda t: ('center', 50+t) )

>>> # cut the last two seconds of the clip:
>>> newclip = clip.subclip(0,-2)

>>> # The scene between times t=3s and t=6s in ``clip`` will be
>>> # be played twice slower in ``newclip``
>>> newclip = clip.subapply(lambda c:c.speedx(0.5) , 3,6)

>>> # slow down clip 50% and make it a gif
>>> myClip.speedx(0.5).to_gif('myClip.gif')

>>> from moviepy.editor import VideoFileClip
>>> clip = VideoFileClip("myvideo.mp4").subclip(100,120)
>>> clip.write_videofile("my_new_video.mp4")
>>> clip.close()

