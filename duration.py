import moviepy
from moviepy.editor import VideoFileClip
import os
spath="I:\Mr.Robot.Season.1.720p.BluRay.x264.ShAaNiG"
x = os.listdir(spath)
s = 0.0

for elements in x:
	if('.mkv' in elements):
		my_clip = VideoFileClip(spath+'/'+elements)
		s = s + my_clip.duration
print(s)