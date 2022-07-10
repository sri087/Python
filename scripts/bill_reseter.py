import configparser
import datetime
import requests
import json

import monthdelta


class Requestor:
    def http_get(self, url, params):
        response = requests.request("GET", url=url, params=params)
        """return (json.dumps(json.loads(response.text), 
                        sort_keys=True, 
                        indent=4, 
                        separators=(",", ": ")))
        """
        return json.loads(response.text)

    def http_put(self, url, params):
        response = requests.request("PUT", url=url, params=params)
        """return (json.dumps(json.loads(response.text), 
                        sort_keys=True, 
                        indent=4, 
                        separators=(",", ": ")))
        """
        return json.loads(response.text)


class BillReseter:
    def __init__(self):
        self.read_config("trello.ini")
        self.auth = {
            "key": self.config["trello"]["app_key"],
            "token": self.config["trello"]["token"],
        }
        self.params = {
            "dueComplete": "false",  # reset the completed checkbox
            "idList": self.config["trello"][
                "to_pay"
            ],  # send the card back to 'To Pay' list
        }
        self.paid_bills_list = []
        self.requestor = Requestor()

    def read_config(self, config_file_name: str):
        self.config = configparser.ConfigParser()
        self.config.read(config_file_name)

    def reset_bill(self, bill):
        ddate = bill["due"][:10]
        freq = ""
        for label in bill["labels"]:
            freq = label.get("name")
            if freq[:6] == "Repeat":
                [year, month, day] = ddate[:10].split("-")

                olddue = datetime.date(int(year), int(month), int(day))
                newdue = None

                if freq == "Repeat Monthly":
                    newdue = olddue + monthdelta.MonthDelta(1)
                elif freq == "Repeat 6 Monthly":
                    newdue = olddue + monthdelta.MonthDelta(6)
                elif freq == "Repeat Yearly":
                    newdue = olddue + monthdelta.MonthDelta(12)

                print(bill["name"], olddue, newdue, freq)
                # create a full parameter dict with auth and params, add due date as new parameter
                put_params = {**self.auth, **self.params}
                put_params["due"] = newdue

                url = (
                    self.config["trello"]["base_url"]
                    + self.config["trello"]["reset_card_url"]
                    + bill["id"]
                )
                self.requestor.http_put(url, put_params)

    def get_paid_bills(self):
        url = (
            self.config["trello"]["base_url"] + self.config["trello"]["paid_bills_url"]
        )
        self.paid_bills_list = self.requestor.http_get(url, self.auth)

    def reset_bills(self):
        self.get_paid_bills()
        print("Bill Name", "Old Due", "New Due", "Frequency")
        for bill in self.paid_bills_list:
            self.reset_bill(bill)


def main():
    bill_reseter = BillReseter()
    bill_reseter.reset_bills()


if __name__ == "__main__":
    main()
