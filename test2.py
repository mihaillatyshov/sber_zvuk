import moviepy.editor as mp
from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_nonsilent
import speech_recognition as sr

MyVideo = mp.VideoFileClip("./videos/blabla.mp4")
#MyVideo
MyAudio = MyVideo.audio
#MyVideo.audio.write_audiofile("./videos/test_a.wav")
MyAudio.write_audiofile("./videos/blabla_a.wav")
#MyVideo.write_videofile("./videos/blabla_v.mp4")


r = sr.Recognizer()
audio = "./videos/blabla_a.wav"
with sr.AudioFile(audio) as source:
    #r.adjust_for_ambient_noise(source)
    audio = r.record(source)
text = r.recognize_google(audio, language = "ru-RU")
print(text)



#print("Start")
#sound = AudioSegment.from_file("./videos/blabla_a.mp3", format="mp3")
#timestamp_list = detect_nonsilent(sound, 500, sound.dBFS * 1.3, 1)
# 
#for i in range(len(timestamp_list)):
#    d = timestamp_list[i][1] - timestamp_list[i][0]
#    print("Section is :", timestamp_list[i], "duration is:", d)
#print('dBFS: {0}, max_dBFS: {1}, duration: {2}, split: {3}'.format(round(sound.dBFS,2),round(sound.max_dBFS,2),sound.duration_seconds,len(timestamp_list)))