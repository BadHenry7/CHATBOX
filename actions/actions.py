# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import aiohttp

# class ActionHelloWorld(Action):
    

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []
    

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
        if not user_cedula:
            dispatcher.utter_message(response="utter_dar_cedula")  
            return []  # Indica que el slot sigue vacío

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


class Diagnosticos(Action):

    def name(self) -> Text:
        return "action_diagnosticos_chatbox"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_cedula = tracker.get_slot("cedula")
        print("--------------", user_cedula)
        
        payload = {
            "cedula": user_cedula 
        }

        if not user_cedula:
            dispatcher.utter_message(response="utter_dar_cedula")  
            return []  # Indica que el slot sigue vacío

        async with aiohttp.ClientSession() as session:
            async with session.post("http://127.0.0.1:8000/get_diagnosticos_chatbox", json=payload) as response:
                rasa_response = await response.json()
                print(rasa_response)
                v_resultado = rasa_response["resultado"]
                v_descripcion = rasa_response["descripcion"]

                dispatcher.utter_message(
                response="utter_diagnosticos_chatbox",
                resultado=v_resultado,
                descripcion=v_descripcion
        )
        return []
    

class Recomendaciones(Action):

    def name(self) -> Text:
        return "action_recomendaciones_chatbox"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_cedula = tracker.get_slot("cedula")
        print("--------------", user_cedula)
        
        payload = {
            "cedula": user_cedula 
        }
        if not user_cedula:
            dispatcher.utter_message(response="utter_dar_cedula")  
            return []  # 
        
        async with aiohttp.ClientSession() as session:
            async with session.post("http://127.0.0.1:8000/get_recomendaciones_chatbox", json=payload) as response:
                rasa_response = await response.json()
                print(rasa_response)
                v_observacion = rasa_response["observacion"]
              

                dispatcher.utter_message(
                response="utter_recomendaciones_chatbox",
                observacion=v_observacion,
            
        )
        return []
    
class Sintomas(Action):

    def name(self) -> Text:
        return "action_sintomas_chatbox"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_cedula = tracker.get_slot("cedula")
        print("--------------", user_cedula)
        
        payload = {
            "cedula": user_cedula 
        }
        if not user_cedula:
            dispatcher.utter_message(response="utter_dar_cedula")  
            return []  
        async with aiohttp.ClientSession() as session:
            async with session.post("http://127.0.0.1:8000/get_sintomas_chatbox", json=payload) as response:
                rasa_response = await response.json()
                print(rasa_response)
                v_nombre = rasa_response["nombre"]
                v_descripcion = rasa_response["descripcion"]

                dispatcher.utter_message(
                response="utter_sintomas_chatbox",
                nombre=v_nombre,
                descripcion=v_descripcion
        )
        return []
    
class Ubicacion(Action):

    def name(self) -> Text:
        return "action_ubicacion_chatbox"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_cedula = tracker.get_slot("cedula")
        print("--------------", user_cedula)
        
        payload = {
            "cedula": user_cedula 
        }
        if not user_cedula:
            dispatcher.utter_message(response="utter_dar_cedula")  
            return [] 
        async with aiohttp.ClientSession() as session:
            async with session.post("http://127.0.0.1:8000/get_ubicacion_chatbox", json=payload) as response:
                rasa_response = await response.json()
                print(rasa_response)
                v_ubicacion = rasa_response["ubicacion"]
                v_salas = rasa_response["salas"]

                dispatcher.utter_message(
                response="utter_ubicacion_chatbox",
                ubicacion=v_ubicacion,
                salas=v_salas
        )
        return []