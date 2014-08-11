#!/bin/bash
echo Creating virtualenv...
mkvirtualenv emf-meter

echo Adding cd `pwd` to postactivate...
echo "cd `pwd`\n" >> $WORKON_HOME/test/bin/postactivate

echo Switching to virtualenv...
workon emf-meter

echo Installing requirements...
pip install -r requirements.txt

echo Changing executable flags on scripts..
chmod +x emf-meter-reader.py
