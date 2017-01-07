:::loop
::python.exe C:\src\cntk\Examples\Other\Sourena\Data\rec.py
python.exe C:\src\cntk\Examples\Other\Sourena\Data\maintest.py
::PAUSE 
python.exe C:\src\cntk\Examples\Other\Sourena\Data\uci2ctf.py  --input_file all.txt --features_start 1 --features_dim 533 --labels_start 0 --labels_dim 1 --num_labels 5  --output_file test.txt
::PAUSE 

C:\src\cntk\x64\Release_CpuOnly\cntk.exe configfile=..\Config\simple.cntk

::PAUSE 


python.exe C:\src\cntk\Examples\Other\Sourena\Data\mode.py

::goto loop