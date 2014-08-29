#!/bin/bash

echo Starting reader...
/emf-meter/emf-meter-reader.py epmX /dev/ttyUSB0 /emf-meter/epmX.csv >> /emf-meter/reader.log 2>&1 &
