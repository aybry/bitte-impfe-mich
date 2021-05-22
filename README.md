# Bitte impfe mich! Please vaccinate me!
This is a Python script that utilises the [impfstoff.link](https://impfstoff.link/) API to get you a vaccination appointment.

This script calls `https://api.impfstoff.link/?robot=1` once every second (or so) to see if any new appointments have been found by the API's backend. If a new appointment is found, the corresponding Doctolib link is opened automatically in a new tab.

Using this script might save you a couple of seconds compared to using the website manually. That could be the difference you need.

## Run the script
To set the script going, simply open up a terminal in the repo's directory, and run:

```
python bitte_impfe_mich.py
```

You might have to install the (third-party) package `requests` first:

```
python -m pip install requests
```

The script should work on all versions of Python 3.6+ (written and tested on 3.8.5).

If you make adjustments, please respect the API's rate limit of _1 request per second_. Feel free to share your improvements by opening a merge request.

## Please note...
Thousands of people are trying simultaneously to do exactly the same thing as you are; this script gives you no guarantee of securing a slot. During testing, the majority of freshly opened tabs have already shown "Keine Verfügbarkeiten"/"No availabilities". For the rest that aren't already booked before you have a chance, you still have to click the buttons as quickly as possible. 

## Acknowledgements
Thanks to the teams behind [impfstoff.link](https://impfstoff.link/) and the [Telegram bot](https://github.com/guicheffer/impfstoff.bot). 
