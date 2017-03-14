# trex-game-agent
Designed course project for Scratch and Python @ NCTU

Reading screenshot and controling keyboard to play trex game.  
Here are some place to play this time-killing game:
- [T-Rex Runner](http://www.trex-game.skipser.com/)
- [Running T-Rex](http://apps.thecodepost.org/trex/trex.html)
- [T-Rex Game](https://scratch.mit.edu/projects/98506770/) on Scratch

This agent can only play well on [T-Rex Runner](http://www.trex-game.skipser.com/) version. To play other version, paramter should be tuned manually again.  
This agent can play forever, barring accidents.  

## Installation
Run `pip3 install -r requirements.txt` to install the dependencies.  
Some extra effort may be needed in order to install [PIL](http://www.pythonware.com/products/pil/) and [pyautogui](https://pyautogui.readthedocs.io/en/latest/install.html) package.  

## Let's Play
1. Open the game, make sure that the entire playground is visible.
2. Fire `python3 play.py`

After lossing the game, you should manually close the running `play.py` and restart it for next round if you want.  
