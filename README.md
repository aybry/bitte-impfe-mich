# Bitte impfe mich! Please vaccinate me!
A Python bot that utilises the [impfstoff.link](https://impfstoff.link/) API to get you a vaccination appointment.

This script calls `https://api.impfstoff.link/?robot=1` once a second to see if any new appointments have been found by the API's backend. If a new appointment is found, the corresponding Doctolib link is opened automatically in a new tab.

Using this script might save you a couple of seconds compared to using the website manually. That could be the difference you need.

# Run the script
To set the script going, simply run:

```
python bitte_impfe_mich.py
```

The script should work on all Python 3 versions (written and tested on 3.8.5).

If you make adjustments, please respect the API's rate limit of _1 request per second_. Feel free to share your adjustments by opening a merge request.

# Please note...
So far during testing, not a single tab has actually shown available appointments (only "Keine Verfügbarkeiten"/"No availabilities"). Thousands of people are trying simultaneously to do exactly the same thing as you are; this script is no guarantee. 

# Acknowledgements
Thanks to the teams behind [impfstoff.link](https://impfstoff.link/) and the [Telegram bot](https://github.com/guicheffer/impfstoff.bot). 
