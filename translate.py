import os
import re
from googletrans import Translator


DIR = "D:\\Downloads\\"
catalog = input("Введите название папки: ")

dirs = os.listdir(path=DIR + catalog+"\\")


catalogs = []
for dir in dirs:
    if os.path.splitext(DIR+catalog+dir)[1] == ".srt":
        catalogs.append(dir)


translator = Translator()

# def getText(lines:list)->list:
#     for line in lines:        
#         if bool(re.match("[a-zA-Z]", line)) == False:
#             # translations = translator.translate(line, src="en", dest='ru')
#     return lines

for i in catalogs:
    with open(DIR+catalog+"\\"+i, 'r+') as f:
        lines = f.readlines()
        for line in lines:  
            if bool(re.match("[a-zA-Z]", line)):
                translation = translator.translate(line, src="en", dest='ru')
                lines[lines.index(line)] = translation.text + "\n"

    with open(DIR+catalog+"\\"+"2"+i, 'w+', encoding='utf-8') as f:
        for line in lines:
            f.write(line)