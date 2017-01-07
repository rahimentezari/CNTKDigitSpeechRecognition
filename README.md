# CNTKDigitSpeechRecognition
This is for Digit Recognition using Microsoft DeepLearning Platform :CNTK

Training:
- This was trained using TIDIGI*T*S
- all the files were played back and recorded again with microphone,saved in .wav format.
- features were extracted using "python_speech_features"(https://github.com/jameslyons/python_speech_features)
- features were trained using Microsoft CNTK
- for getting ready the data for train:
   - run loop.py- this file inputs the testwav.txt(line by line of training wav audios) and outputs all.txt  containing MFF features with labels at the beginning of each line.
  - run uci2ctf.py with this command: python uci2ctf.py --input_file train.txt --features_start 1 --features_dim 533 --labels_start 0 --labels_dim 1 --num_labels 5 --output_file train2.txt


Test:
Run text.bat on windows. This will execute:
1- rec.py to record a number
2- maintest.py to extract MFCC features(all.txt)
3- uci2ctf.py to change the type to "CNTKTextFormatReader"
4- cntk.exe configfile=..\Config\simple.cntk
5- mode.py to get the Mode of Predicted outputs.
6- print of the predicted digit to "output.txt"
