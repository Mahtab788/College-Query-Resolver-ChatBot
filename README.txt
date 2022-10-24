
======================
 Library Requirements 
======================
This Chat-Bot requires some python libraries installed in system which were installed in an virtual enviornment on Anaconda3, which can be installed by visiting "https://pytorch.org/".
The code was specificly created for CUDA 11.3 Compute Platform which is for NVIDIA GPUs. To run the code without a GPU compute platform then install pytorch for CPU.
List of other libraries that need to be installed:
1.pyttsx3 (pip install pyttsx3)
2.NLTK (https://www.nltk.org/install.html)
3.numpy (pip install numpy)

=========================
 How To Run The Chat-Bot
=========================
To run the Chat-bot run a file named app.py. If any changes are made in intents.json 
file then  firstly user should run train.py to train the Chat-Bot for new responese
and after doing that user can run app.py