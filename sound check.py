import glob  
import os
import json
import webbrowser

def check_sound_webdriver(dirname = os.path.dirname(__file__) ):
    results_dict = {}
    # below loop is needed to iterate through different audio type files
    for EXT in ['.wav','.mp3','ogg',".aac",".ac3",".wma"]:
        # loop for iterate through all files and find EXT type files
        for filename in glob.glob(dirname + "\\*" + EXT):
            webbrowser.open(filename)
            audio_name = filename.removeprefix(dirname + "\\") # remove path name from filename
            user_input = input("Enter your feedback, n or c: ")
            results_dict[audio_name] = user_input 
    
    j = json.dumps(results_dict, indent=4) 
    f = open('result.json', 'w')
    print(j, file=f)

# Either input folder path where files are stored or move files into executable py file folder
check_sound_webdriver()
# check_sound_webdriver("C:\\Users\\gagoo\\Desktop\\")

