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
You will need to open Firefox and navigate to the saved logins page. To get there, press the Alt key to make the top menu visible. Click on Tools -> Options. Then select the tab on the left for Privacy & Security. Scroll down to the section **Logins and Passwords**. Make sure "Use a master password" is unchecked. If you already had a master password, you will need to enter it now in order to disable it. Finally, click on the "Saved Logins" button along the right side. Leave this window open.

Launch a terminal. If you installed Python through Anaconda, this will be through the Anaconda prompt. If you installed Python natively on Windows, this will be cmd.exe. If it's on Mac/Linux it will be the Terminal program. In any case navigate to the directory which contains the script `firefox_password_exporter.py`. Launch the script by running:
```
python firefox_password_exporter.py
```
Move the terminal window to one side of the screen where you can still see the Firefox window, but the terminal window is selected (in focus).

The script will prompt you to enter some required information. A description is below, along with a screen shot for clarification:

1. Number of passwords: This is the number written on the left panel at the top, "N logins"
2. Number of visible items: This is the total number of items you can see on the left side of the screen. If one is partially visible, include that in the count. If all the items are visible, the number you enter will be the same  as the number of passwords in step 1.

For questions 3-8, you need to move your mouse to hover over the desired location, but don't click. Instead, press the enter key. The terminal needs to be in focus so that the program can capture when you press Enter and record the mouse's location. Once you hit "ENTER" the saved coordinates will be printed out in the terminal. If you record any of these incorrectly, you will  need to start again.
Make sure before you start, you are scrolled all the way to the top of the page.

3. First Item location: Hover the mouse over the first item. It shouldn't matter where in the box the mouse is, but I usually put it somewhere in the middle. Press the ENTER key.
4. Last Item location: Hover the mouse over the last visible item. If the last item is partially visible, put the mouse towards the top of the item so that it will still be selected if you were to press the mouse (but don't actually press the mouse now). Press the ENTER key.
5. Info location: Hover the mouse over the informational text on the right panel. I recommend placing it near the front of the string since it may have varying length. You know you're in the right place if the mouse cursor changes to to look like a capital letter I. Press the ENTER key.
6. Website location: Hover the mouse over the Website address url. You know you're in the right place if the mouse cursor changes to a little hand as if you are following a link. Press the ENTER key.
7. Username Copy Button: Hover the mouse over the "Copy" button to the right of the Username. Press the ENTER key.
8. Password Copy Button: Hover the mouse over the "Copy" button to the right of the Password. Press the ENTER key.

![Inputs](https://raw.githubusercontent.com/lherlant/firefox_password_exporter/master/password_screen.png)

Finally you will be given an ETA and asked if you want to continue or not. Press ENTER to continue. Once you start, you will not be able to use the computer until it's completed. You will see the mouse move back and forth on the screen, selecting and copying fields. The websites and usernames will print in the terminal window as it goes.

Do not touch the mouse or keyboard during this time or it will miss passwords and copy irrelevant data. It's also hard to stop once it has started since it has control over your mouse. On Windows, doing ctrl+alt+delete halts execution.

When it's done, `firefox_auto_export.csv` will be created in the same directory with the copied login information contained within.

I recommend testing with a small number of examples first (enter 5 for question 1 and 2 above), to be sure it's exporting the way you want before you run it on 100+ logins.


## Disclaimer
This script was handy for me, but I make no claims that it will work for you. You must do your own due diligence to confirm that you have the passwords you want exported and that the information is correct. If you are exporting a large number of passwords, I would particularly advise checking the last screen's worth of passwords for duplicates and missing entries. In my personal testing it was working fine, but the onus is on you to confirm before deleting original entries from your Firefox profile.
