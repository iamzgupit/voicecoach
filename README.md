# VoiceCoach
A web app that helps you tune your voice and practice your scales, no need for a piano or a teacher.

# Demo
Visit https://voicecoachdemo.herokuapp.com to see the app in action.

# Technologies
* Web Audio API
* Sound Manager 2 API
* PitchDetect by [cwilso](https://github.com/cwilso/pitchdetect)
* Pushtape Player by by [zirafa](https://github.com/zirafa/pushtape-player.js/blob/master/README.md)
* Python
* Javascript
* JQuery
* SQLite	
* SQLAlchemy
* Jinja
* Flask
  
# Features
- pitch detector & matcher
- check if you're on pitch; see how closely you match a sample audio track or Mariah Carey
- routine builder
- create and save different routines for different practice situations (e.g. you're tired and your voice is sore, so you choose a shorter routine)
- player
- play your audio routine, jumping around within a scale and from scale to scale with ease.

# Installation
Clone the voicecoach repo:

```sh
$ git clone https://github.com/blakegilmore/voicecoach.git
```
# Running it
Jump into your voicecoach directory:

```sh
$ cd voicecoach
```
Set up your environment and install dependencies.
```sh
$ cd voicecoach
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
Run the server with python.
```sh
$ python server.py
```
