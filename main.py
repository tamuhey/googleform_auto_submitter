# -*- coding: utf-8 -*-
import requests
import json

cfg_fname = "cfg/cfg.json"
with open(cfg_fname, "r") as f:
    cfg = json.load(f)


def main():
    # set request params
    params = {"entry.{}".format(cfg["entry"][k]): cfg["output"][k] for k in cfg["entry"].keys()}

    # submit
    r = requests.get(cfg["form_url"] + "formResponse", params=params)

    # error check
    try:
        r.raise_for_status()
    except:
        print("Failure...")
    else:
        print("Success!!")


if __name__ == "__main__":
    main()
