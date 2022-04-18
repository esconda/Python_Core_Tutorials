# Author: Burak Dogancay
from setuptools import setup

def setupSettings():
  APP=['test.py']
  DATA_FILES = ['myInsertedImage.jpg']
  OPTIONS = {'argv_emulation': True,'iconfile': 'myCoolIcon.icns'}
  
  setup (
        app=APP,
        data_files=DATA_FILES,
        options={'py2app': OPTIONS},
        setup_requires=['py2app'],
        )
  
def main():
  setupSettings()

if __name__ == '__main__':
    main()