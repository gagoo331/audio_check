import multiprocessing
from playsound import playsound

p = multiprocessing.Process(target=playsound, args=("C:\\Users\\gagoo\\Documents\\Sound\\file_example_WAV_2MG.wav",))
p.start()
input("press ENTER to stop playback")
p.terminate()