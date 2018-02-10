# Smart Blender
A Smart Blender built at SpartaHack IV [Won awards:  Best IoT Hack Using A Qualcomm Device, First-Time Hacker Prize]

# Getting Started
To use this project you need:
* Navigate to https://mysmartblender.com/
* Download the python scripts on a rasberry pi and connect a relay to a blender on GPIO port 17
* Put food in blender and give command

# Built With
* JavaScript
* Python
* HTML/CSS
* Rasberry Pi

# Front End
The front end utilizes the p5.js speech recognition library to take user input via speech. The transcribed string is then pushed to a firebase database to be processed by the backend. When a text response is sent back from the database, the front end listens for a change in value and speaks the result. We used html/css for the styling but ideally we want to move it over to React after this.

# Back End
The backend consists of a rasberry pi with a continuos python script that listens for changes in the firebase database to process user input commands. We utilize a word bank of key words that are relevant for blender commands to actuate a text response and a blender command. 

We use the GPIO output in the rasberry pi to control a single channel relay that opens and closes the blender's circuit to turn it on and off. We allow variable blending times and we would want to add a pulse feature as a next step.

# Authors
Greg Margosian, Chris Bell, Ritwik Biswas
