# Firefox Password Exporter

My father was looking for a way to export firefox passwords, having saved more than a hundred in his profile. You might want to do this if you are switching to a specialized password manager or simply want to keep an encrypted backup of passwords to sites you don't use often. The only problem is that there doesn't seem to be a way to do it! We tried several opensource projects on github claiming to export the login credentials directly from the key4.db and logins.json files, but unfortunately none of them worked for us (they rely on using parts of Firefox's code for the decryption or reverse engineer the parts of the key4.db file which seems to have changed since their implementation). 

This password exporter works differently by using the mouse and clipboard to copy and save the logins and passwords from the settings gui within firefox. Perhaps less elegant, but it gets the job done and exported over 300 passwords in about 5 minutes.

I've extended the original code to make it a little more configurable instead of hardcoding the mouse positions and posted it here in hopes it will help anyone else facing the same task.


## Installation
This code has been tested under Python 3.7, but should likely work for Python 3.x given the dependencies work. The packages `pyautogui` and `clipboard` are required.
These can be installed via:
```
pip install pyautogui clipboard
```
If pip did not get installed or added to your path when you installed Python, you can do the following instead:
```
python -m pip install pyautogui clipboard
```
## Usage

