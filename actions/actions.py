# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import aiohttp

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
    

class BuscarCitas(Action):

    def name(self) -> Text:
        return "action_ultima_cita"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_cedula = tracker.get_slot("cedula")
        print("--------------", user_cedula)
        
        payload = {
            "cedula": user_cedula 
        }
        async with aiohttp.ClientSession() as session:
            async with session.post("http://127.0.0.1:8000/get_ultima_cita", json=payload) as response:
                rasa_response = await response.json()
                print(rasa_response)
                v_fecha = rasa_response["fecha"]
                v_doctor = rasa_response["doctor"]

                dispatcher.utter_message(
                response="utter_ultima_cita",
                fecha=v_fecha,
                doctor=v_doctor
        )
        return []


class Buscar(Action):
    def name(self) -> Text:
        return "action_"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_cedula = tracker.get_slot("cedula")
        print("--------------", user_cedula)
        
        payload = {
            "cedula": user_cedula 
        }
        async with aiohttp.ClientSession() as session:
            async with session.post("http://127.0.0.1:8000/get_ultima_cita", json=payload) as response:
                rasa_response = await response.json()
                print(rasa_response)
                v_fecha = rasa_response["fecha"]
                v_doctor = rasa_response["doctor"]
     

                dispatcher.utter_message(
                response="utter_ultima_cita",
                fecha=v_fecha,
                doctor=v_doctor
        )
        return []
