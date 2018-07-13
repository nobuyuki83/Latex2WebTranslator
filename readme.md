# Latex2Translator

If you want to translate your LaTex using an automatric online service like GoogleTranslate, you need to remove all the LaTex commands, otherwise the translator will breake the commands. This program will detect the latex command and change it into keywords such that the translator wouldn't change the keywords. After the online translation, another program substite the keywords back to the latex commands.


## How to Use

chagne the LaTex file "main_ja.tex" into text file "toGoogleTrans.txt" and keyword file "keyMap.txt"

'''
python to_google.py
'''

Chagne the text file from translator "fromGoogleTrans.txt" and "keyMap.txt" into LaTex file "main_en.tex"

'''
python to_latex.py
'''



