import requests
import time
import logging
import webbrowser
import os


##### Start user options #####

# The latest possible date for your first appointment.
# If an availability is found but the date is later than `LATEST_DATE`,
# the availability will be ignored and the tab won't be opened.
LATEST_DATE = "2023-01-01"  # e.g. "2021-06-19"

# The following vaccination centres will be ignored (if e.g. you explicitly
# need a non-vector vaccine or cannot travel far).
IGNORE = (
    # "arena"
    # "messe"
    # "erika"
    # "tempelhof"
    # "velodrom"
    # "tegel"
)

##### End user options #####


logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s - %(asctime)s - %(message)s")


API_URL = "https://www.doctolib.de/institut/berlin/ciz-berlin-berlin?pid=practice-{iz_id}"


ZENTREN = {
    "arena": {
        "last_opened": 0,
        "id": "158431",
    },
    "messe": {
        "last_opened": 0,
        "id": "158434",
    },
    "erika": {
        "last_opened": 0,
        "id": "158437",
    },
    "tempelhof": {
        "last_opened": 0,
        "id": "158433",
    },
    "velodrom": {
        "last_opened": 0,
        "id": "158435",
    },
    "tegel": {
        "last_opened": 0,
        "id": "158436",
    },
}


DATA = {}
COUNTER = 0


def get_me_geimpft():
    r = requests.get("https://api.impfstoff.link/?robot=1",
                     timeout=3).json()["stats"]

    logging.debug("fetched")

    for api_iz_dict in r:
        check_impfzentrum(api_iz_dict)
    logging.debug("Done")
    time.sleep(1.1)


def check_impfzentrum(api_iz_dict):
    iz = api_iz_dict["id"]

    for date in api_iz_dict["stats"]:
        identifier = "_".join((iz, date))
        if not DATA.get(identifier):
            DATA[identifier] = api_iz_dict["stats"][date]["last"]
        elif api_iz_dict["stats"][date]["last"] > DATA[identifier]:
            DATA[identifier] = api_iz_dict["stats"][date]["last"]
            if (time.time() - ZENTREN[iz]["last_opened"] > 20):
                if date <= LATEST_DATE:
                    logging.info(f"Date {date} is good!")
                    logging.info(f"{iz} has new appointments on {date}...")
                    if iz in IGNORE:
                        logging.info(f"Ignoring {iz}.")
                    else:
                        logging.info(f"Opening {API_URL.format(iz_id=ZENTREN[iz]['id'])}")
                        webbrowser.open(API_URL.format(iz_id=ZENTREN[iz]["id"]))
                        for _ in range(1):
                            print("\007")
                            time.sleep(0.15)
                        ZENTREN[iz]["last_opened"] = time.time()
                        return
                else:
                    logging.info(f"Date {date} is too late")
            else:
                logging.info(f"{iz} is already open")


while True:
    try:
        if COUNTER % 50 == 0:
            logging.info(f"Fetched {COUNTER} times")
        get_me_geimpft()
        COUNTER += 1
    except Exception as e:
        logging.info(e)
