from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("Hello World!")

         return []

class BalanceForm(Action):

    def name(self) -> Text:
        return "balance_form"
    
    @staticmethod
    def required_slots(tracker) -> List[Text]:
    
        return["card_number"]
    
    def run(self,
        dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any],
             ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("It's working!!!")
        
        return []
                    

   
         

    
    
        

                    

                   
        
    
    

    
    

                   
        
    
    

    
    

                    

                   
        
    
    



                   
        
    
    

    
    

                   
        
    
    

    
    
                    

                   
        
    
    

    
    

                   
        
    
    

    
    
