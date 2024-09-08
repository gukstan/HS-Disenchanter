# HS-Disenchanter

A script which disenchants all of your cards from a specific Hearthstone expansion.

This is a personal project from a man who only plays Standard. Disenchanting all Wild-only cards used to be so exhausting before I made this. Now I can leave it running while I go have some coffee

## Disclaimer

- This has only been tested in **Windows 10**.
  
- In order for the script to work out of the box, you need to **set your primary monitor and your Hearthstone to the 1920x1080 resolution.**
  
- This script is rough around the edges. I didn't have that many cards to test it with (they all got deleted pretty quickly :P ), so feel free to fiddle with it.
  

## Instructions

1. Make sure you have Python 3.11 installed on your machine.
  
  Note: When run, the script will automatically *pip install* the follwing dependencies in case you don't already have them: pyautogui, keyboard, pygetwindow
  
2. Close any other programs that interact with Hearthstone, such as deck trackers. Otherwise the script may not work.
  
3. Open Hearthstone and go into your collection. Then, select the expansion that you want to disenchant. Proceed with caution, as the script will disenchant ALL the cards within that expansion.
  
![2024-09-08-11-19-21-image](https://github.com/user-attachments/assets/2f83a67b-2b1c-4adf-affe-1c13974dd329)
  
4. Click on "Crafting". On the right side of the screen, leave only the "Owned" options checked.
  
![image](https://github.com/user-attachments/assets/318e275b-50de-45f6-9e12-0d5788b33130)

  
5. Run Disenchant.py
  

The script will then disenchant all cards within the selected expansion. If you need it to stop, press the "insert" key on your keyboard. If you don't have "insert", you can edit Disenchant.py and replace it with whatever key you prefer. It's really simple!

Note: the script will continue to run even after it deleted all cards within the expansion! When this happens, you need to stop it from running. If you have another expansion you wish to disenchant, just repeat the process.

6. Enjoy your Arcane Dust!
