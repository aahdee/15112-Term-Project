GeoHell - created by Aren Davey


GeoHell is a small bullet hell game created in Python with the module Pygame. This game was created for the term project for my 15-112 class at Carnegie Mellon University.


To play this game, open the run.py file and run it. 


To run this game, you need:
* Python 3
* Pygame
To install Pygame, use the following instructions that was provided by the 15-112 TA Lukas Peraza:


Windows Directions:

Download the correct Pygame .whl file from:
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame

pygame-1.9.2a0-cpXX-none-win32.whl

With XX replaced with
   - "34" if using Python 3.4
   - "35" if using Python 3.5

Note the path to the downloaded file (e.g. C:\Users\Me\Downloads\pygame-1.9.2a0-cp35-none-win32.whl)

Open a Command Prompt (Start Menu -> type "cmd" in search -> Enter)

Navigate to the folder of your Python installation using the "cd" command
(You can find the location of the folder by looking in Pyzo -> Shell -> Edit shell configurations,
and looking in the "exe" text box)

For example, if Python is installed in C:\Python35, type

   cd Python35

Use pip to install Pygame

   python3 -m pip install C:\Users\Me\Downloads\pygame-1.9.2a0-cp35-none-win32.whl

Verify it worked

   python3 -c "import pygame; print('yay')"


OSX Directions:

Open a Terminal window

Type the command

   brew -v

If you get an error (brew: not found), then install homebrew by using the command

   ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install all the Pygame dependencies:

   brew install mercurial git
   brew install sdl sdl_image sdl_mixer sdl_ttf smpeg portmidi

Use pip to install Pygame from source:

   pip3 install hg+http://bitbucket.org/pygame/pygame

Verify it worked

   python3 -c "import pygame; print('yay')"