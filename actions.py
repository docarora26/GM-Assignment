from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import urllib.request, urllib.parse, urllib.error
import requests
from rasa_sdk.forms import FormValidationAction

class ValidateCountryForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_country_form"

    @staticmethod
    def country_db() -> List[Text]:
        """Database of supported cuisines."""

        url = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCountries"
        data = urllib.request.urlopen(url).read().decode()
        info = json.loads(data)
        countries = []
        for i in info['body']:
            countries.append(i.lower())
        return [countries]

    def validate_country(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate country value."""

        if value.lower() in self.cuisine_db():
            # validation succeeded, set the value of the "country" slot to value
            return {"country": value}
        else:
            dispatcher.utter_message(response="utter_wrong_country")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"country": None}

class ActionCountry(Action):
    """This action class allows to display buttons for each country."""

    def name(self) -> Text:

        return "action_country"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        url = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCountries"
        data = urllib.request.urlopen(url).read().decode()
        info = json.loads(data)
        countries = []
        for i in info['body']:
            countries.append(i)
        
        buttons = []
        for i in countries:
            payload = "/country{\"country\": \"" + countries[i] + "\"}"

            buttons.append(
                {"title": "{}".format(countries[i].title()),
                 "payload": payload})

        dispatcher.utter_button_template("utter_select", buttons, tracker)
        return []
class ActionCapital(Action):
    """This action class allows to display buttons for each country."""

    def name(self) -> Text:

        return "action_capital"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        country = str(tracker.get_slot('country'))
        
        response = requests.post('https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCapital', json={'country': country})
        info = response.json()
        capital = info['body']['capital']
        dispatcher.utter_message(response = "utter_capital", country=country, capital=capital)
        return []

class ActionPopulation(Action):
    """This action class allows to display buttons for each country."""

    def name(self) -> Text:

        return "action_population"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:
        country = str(tracker.get_slot('country'))
        response = requests.post('https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getPopulation', json={'country': country})
        info = response.json()
        population = info['body']['population']
        dispatcher.utter_message(response = "utter_population", country=country, population=population)
        return []