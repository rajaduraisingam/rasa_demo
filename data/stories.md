## greet_path
* greet
  - utter_greet
  - utter_help

## say goodbye_path
* goodbye
  - utter_goodbye

## help_path
* help
    - utter_help
    
## transfer money
* transfer_money
    - transfer_form
    - form{"name": "transfer_form"}
    - form{"name": null}
    
## check_balance_path
* greet
    - utter_greet
    - utter_help
* check_balance
    - balance_form
    - form{"name": "balance_form"}
    - form("name":null)
* affirm
    - utter_goodbye
* goodbye
    - utter_goodbye
    
 ## out_of_scope_path
* greet
    - utter_greet
    - utter_help
* out_of_scope
    - action_default_ask_rephrase
* goodbye
    - utter_goodbye

