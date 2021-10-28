import cv2
import moviepy.editor as mve

# склеивание видео
clip1 = mve.VideoFileClip("video1.mp4")
clip2 = mve.VideoFileClip("video2.mp4")

final_clip = mve.concatenate_videoclips([clip1,clip2])
final_clip.write_videofile("concat.mp4")


# извлечеие песни из ролика

audio = mve.AudioFileClip("/")
audio.write_audiofile("/", #fps)

# удаление отрезков в видео
# добавление текста

vcodec =   "libx264"

videoquality = "24"

# slow, ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
compression = "slow"

title = "test"

savevideo = title + '.mp4'

# modify these start and end times for your subclips
cuts = [('00:00:02.949', '00:00:04.152'),
        ('00:00:06.328', '00:00:13.077')]


def edit_video(savevideo, cuts):
    # load file
    video = mve.VideoFileClip(loadtitle)

    # cut file
    clips = []
    for cut in cuts:
        clip = video.subclip(cut[0], cut[1])
        clips.append(clip)

    final_clip = mve.concatenate_videoclips(clips)

    # add text
    txt = mve.TextClip('Please Subscribe!', font='Courier',
                       fontsize=120, color='white', bg_color='gray35')
    txt = txt.set_position(('center', 0.6), relative=True)
    txt = txt.set_start((0, 3)) # (min, s)
    txt = txt.set_duration(4)
    txt = txt.crossfadein(0.5)
    txt = txt.crossfadeout(0.5)

    final_clip = mve.CompositeVideoClip([final_clip, txt])

    # save file
    final_clip.write_videofile(savetitle, threads=4, fps=24,
                               codec=vcodec,
                               preset=compression,
                               ffmpeg_params=["-crf",videoquality])

    video.close()


if __name__ == '__main__':
    edit_video(savevideo, cuts)
