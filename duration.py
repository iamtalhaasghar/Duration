from moviepy.editor import VideoFileClip
import os
from datetime import datetime, timedelta


def traverseFolder(folderPath):
    globalDuration = 0
    for i in os.walk(folderPath):
        if len(i[1]) != 0:
            print("SubFolders of %s:\n%s" % (i[0], i[1]))
        print("Opening folder:", i[0])
        durationOfCurrentFolder = getDurationOfAllVideos(i[0], i[2])
        print("Duration of Videos in %s : %s\n" % (i[0], formatTime(durationOfCurrentFolder)))
        globalDuration = globalDuration + durationOfCurrentFolder
    print("Duration of Videos in %s : %s\n" % (folderPath, formatTime(globalDuration)))

def getDurationOfAllVideos(folderPath, filesList):

    totalDuration = 0.0

    for i in filesList:
        itemFullPath = os.path.join(folderPath, i)
        if itemFullPath.endswith('.mp4') or itemFullPath.endswith('.mkv'):
            try:
                videoFile = VideoFileClip(itemFullPath)
                duration = videoFile.duration
                totalDuration = totalDuration + duration
                print('%s%s (%s)' % ('\t' * 3, i, formatTime(duration)))
            except Exception as ex:
                print('Can not open file: %s\nStack Trace:\n%s' % (itemFullPath, ex))
                continue
    return totalDuration



def formatTime(seconds):
    sec = timedelta(seconds=int(seconds))
    d = datetime(1,1,1) + sec
    return ("%d days, %d hours, %d min, %d sec" % (d.day-1, d.hour, d.minute, d.second))

if __name__ == "__main__":
    folderPath = "/path/to/folder"
    traverseFolder(folderPath)
