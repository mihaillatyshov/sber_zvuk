import speech_recognition as sr
import subprocess
from os import path


STARTING_SEGMENT = '<s>'
ENDING_SEGMENT = '</s>'
SYLLABLE_SEGMENT = '<sil>'
NON_TEXT_SEGMENTS= [ STARTING_SEGMENT, ENDING_SEGMENT,SYLLABLE_SEGMENT ]

def get_audio_file_name(file):
    AUDIO_FILE = f"./videos/{file}"
	#path.join(path.realpath("C:\examples"), file)
    return AUDIO_FILE
    
def audio_extraction():
    command = "ffmpeg -i C:/examples/input.mkv -ss 00:01:00 -t 00:00:30 -vn C:/examples/output.wav"
    subprocess.call(command, shell=True)

def get_audio_Data(audio_file_name):
    r = sr.Recognizer()
    duration = None
    with sr.AudioFile(audio_file_name) as source:
        audioData = r.record(source) 
    return audioData

        
def get_text_from_audio(audioData):
    r = sr.Recognizer()
    text = ''
    try:
        text = r.recognize_sphinx(audioData)
        print("Sphinx extracted the following text\n" + text )
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    return text

def    get_text_segments_from_audio(audioData):
    r = sr.Recognizer()
    decoder = None
    segments = {}
    try:
        decoder = r.recognize_sphinx(audioData, show_all=True)
        for seg in decoder.seg():
            print( "Checking segment [{}] begins at {} & ends at {} seconds".format(seg.word , seg.start_frame/100, seg.end_frame/100, ) )
            if seg.word not in NON_TEXT_SEGMENTS:
                time_frame = ( seg.start_frame/100, seg.end_frame/100 )
                if seg.word in segments:
                    segments[seg.word].append( time_frame)
                else:
                    segments[seg.word] = [time_frame]
            else:
        
                print("Skipping segment - {} ".format(seg.word))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        
    return segments

    
if __name__ == '__main__':
    audio_extraction()
    audio_file_name = get_audio_file_name("output.wav")
    print(audio_file_name)
    audioData = get_audio_Data(audio_file_name)
    print("done audio data")
    entire_text = get_text_from_audio(audioData)
    print("done text extraction")
    segments = get_text_segments_from_audio(audioData)
    print("enter text to see the occurrence : ", )
    key = input()
    if key in segments:
        frames = segments[key]
        num_times = len(frames)
        if num_times> 1:
            print(" the text [{}] repeated {} times in the audio file as shown below".format(key, num_times))
            for frame in frames:
                print("starts at {} and ends at {} ".format(frame[0], frame[1]))
        else:
            print(" the text [{}] occurred once starting at {} and ends at {}".format(key,
            frames[0][0], frames[0][1]))
    else:
        print ("the text [{}] not found in the given audio file , Please check the input".format(key))
    print("done")