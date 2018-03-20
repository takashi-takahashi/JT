import requests
from datetime import datetime

WEB_HOOK_URL = ""


def main():
    decision = datetime(year=2018, month=3, day=20)
    now = datetime.now()
    diff = now - decision
    diff_week = int(diff.days / 7)
    print(diff_week)
    # requests.post(WEB_HOOK_URL, json={"text": "############"})
    # requests.post(WEB_HOOK_URL, json={"text": "{0}週間が経過しました。".format(diff_week)})
    # requests.post(WEB_HOOK_URL, json={"text": "############"})


if __name__ == "__main__":
    main()
