#!/usr/bin/python
#print('')

import os
import re
lista = os.listdir()
print(lista)
for video in lista:
    if re.search('mp4',video) or re.search('flv',video) :
        video =  "\""+video+"\""
        wav = video+'.wav'
        mp3 = wav+".mp3"
        #print('ffmpeg {0}'.format(i))
        #print(i)
        os.system('ffmpeg -i {0} {1}'.format(video, wav))
        os.system('lame {0} {1}'.format(wav,mp3))
        os.system('rm {0} {1}'.format(wav,video))
