# twitter_api
Server-hosted app for finding Twitter user friends' location and put them on a map.\
Visit my hosted website manually by searching: `damoklov.pythonanywhere.com`
My project is kindly hosted at __Pythonanywhere.com__ and I try to keep it running!\
https://goo.gl/oLY4G4

## Getting started
To work with my project you need to:\
1. Stick to the structure as shown below:\
![S1](/screenshots/pythonanywherelocale.png)
2. Download all the files or clone this repo and move files from _docs_ and _templates_ into root directory with python modules.
3. Create text file __KEYS.txt__ and put your Twitter's API keys into it, separating each of them with a newline.
4. Host your project at __Pythonanywhere__ or manually launch _flask_app.py_:\
* Windows:
```
set FLASK_APP=flask_app.py
python -m flask run
```
   * Unix:
```
export FLASK_APP=flask_app.py
python -m flask run
```
### Prerequisites
For python 3.x: `pip3 install -r requirements.txt`\
For python 2.x `pip install -r requirements.txt`

## Built With
* [Flask](http://flask.pocoo.org/)
* [Pythonanywhere](https://www.pythonanywhere.com)

## Warning
This app was built to be deployed on a __Pythonanywhere.com__ and some code parts may not be tested as for using manually on PC.\
In case of problems, write comments underneath this projects of send a message to me directly: `mishanya@protonmail.com`
