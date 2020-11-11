from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

import asyncio

class TransferForm(FormAction):

    def name(self):
        return "transfer_form"
        
    @staticmethod
    def required_slots(tracker):
    
        if tracker.get_slot("PERSON") == True:
            return("amount_of_money")
        else:
           return("PERSON", "amount_of_money")
            
    def submit(
       self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        #domain: Dict[Text, Any],
   ) -> List[Dict]:
         return []
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
        "PERSON": [
                self.from_entity(entity = "PERSON"),
                self.from_intent(intent = "deny", value = None)
            ],
            "amount_of_money": [
                self.from_entity(entity = "amount_of_money"),
                self.from_intent(intent = "deny", value = None)
          ]
        }

class BalanceForm(FormAction):

    def name(self):
        return "balance_form"
        
    @staticmethod
    def required_slots(tracker):
    
        if tracker.get_slot("credit_card") == True:
            return()
        else:
            return("credit_card")
            
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
         return []
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
        "credit_card": [
                self.from_entity(entity = "credit_card"),
                self.from_intent(intent = "deny", value = None)
            ]
        }
        
#import json
    

#class FetchData(Action):
        #def name(self) -> Text:
            #return "fetch data"

        #def run(self, dispatcher: CollectingDispatcher,
                #tracker: Tracker,
                #domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
     #Get Input from user
            #limit = tracker.latest_message['text']
    
            #with open('data.json', 'r') as file:
               #reader = list(csv.reader(file))
        
            #for row in reader[:limit]:
                #print("In Row")
                #dispatcher.utter_message(text=row[1])
                #return []
