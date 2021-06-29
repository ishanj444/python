## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## book_room
* book_room
  - utter_book_room
* count_room
  - utter_count_room

## check_in
* check_in
  - utter_check_in

## check_out
* check_out
  - utter_check_out

## cancel_reservation
* cancel_reservation
  - utter_cancel_reservation

## cancellation_policy
* cancellation_policy
  - utter_cancellation_policy

## restaurant
* restaurant
  - utter_restaurant

## breakfast_avail
* breakfast_avail
  - utter_breakfast_avail

## breakfast_time
* breakfast_time
  - utter_breakfast_time

## restaurant_time
* restaurant_time
  - utter_restaurant_time

## clean_room
* clean_room
  - utter_clean_room

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
