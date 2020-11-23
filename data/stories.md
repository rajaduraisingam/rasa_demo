## greet
* greet
 - utter_greet
 - utter_help

## happy path
* greet
  - utter_greet
  - utter_help
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
  - utter_help
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
  - utter_help
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
 
## check balance
* check_balance
  - balance_form
  - form{"name" : "balance_form"}
  - form("name" : null)
* affirm
  - utter_goodbye  
 
 ## transfer money
 * transfer_money
  - transfer_form
  - form{"name" : "transfer_form"}
  - form("name" : null)
* affirm
  - utter_goodbye
 

  
