import requests
import time
import logging
import webbrowser


logging.basicConfig(level=logging.INFO)


ZENTREN = {
    "arena": {
        "link": "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158431",
        "last_opened": 0
    },
    "messe": {
        "link": "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158434",
        "last_opened": 0
    },
    "erika": {
        "link": "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158437",
        "last_opened": 0
    },
    "tempelhof": {
        "link": "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158433",
        "last_opened": 0
    },
    "velodrom": {
        "link": "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158435",
        "last_opened": 0
    },
    "tegel": {
        "link": "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-158436",
        "last_opened": 0
    },
}


DATA = {}
COUNTER = 0


def get_me_geimpft():
    r = requests.get("https://api.impfstoff.link/?robot=1").json()["stats"]

    logging.debug("fetched")

    for iz_dict in r:
        iz = iz_dict["id"]

        for date in iz_dict["stats"]:
            identifier = "_".join((iz, date))
            if not DATA.get(identifier):
                DATA[identifier] = iz_dict["stats"][date]["count"]
            elif iz_dict["stats"][date]["count"] > DATA[identifier]:
                DATA[identifier] = iz_dict["stats"][date]["count"]
                if time.time() - ZENTREN[iz]["last_opened"] > 10:
                    logging.info(f"Opening {iz}")
                    webbrowser.open_new_tab(ZENTREN[iz]["link"])
                    ZENTREN[iz]["last_opened"] = time.time()
                else:
                    logging.info(f"{iz} is already open")

    logging.debug("Done")
    time.sleep(1)


while True:
    try:
        if COUNTER % 10 == 0:
            logging.info(f"Fetched {COUNTER} times")
        get_me_geimpft()
        COUNTER += 1
    except Exception as e:
        logging.info(e)

