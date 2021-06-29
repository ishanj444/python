#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## happy path 1
* greet: hello there!
  - utter_greet
* mood_great: amazing
  - utter_happy

## happy path 2
* greet: hello there!
  - utter_greet
* mood_great: amazing
  - utter_happy
* goodbye: bye-bye!
  - utter_goodbye

## sad path 1
* greet: hello
  - utter_greet
* mood_unhappy: not good
  - utter_cheer_up
  - utter_did_that_help
* affirm: yes
  - utter_happy

## sad path 2
* greet: hello
  - utter_greet
* mood_unhappy: not good
  - utter_cheer_up
  - utter_did_that_help
* deny: not really
  - utter_goodbye

## sad path 3
* greet: hi
  - utter_greet
* mood_unhappy: very terrible
  - utter_cheer_up
  - utter_did_that_help
* deny: no
  - utter_goodbye

## book_room
* book_room: I want to book a room
  - utter_book_room
* count_room: 2
  - utter_count_room

## check_in
* check_in: What are your check in timings ?
  - utter_check_in

## check_out
* check_out: What are your check out timings ?
  - utter_check_out

## cancel_reservation
* cancel_reservation: How do I cancel a reservation ?
  - utter_cancel_reservation

## cancellation_policy
* cancellation_policy: What is your cancellation policy ?
  - utter_cancellation_policy

## restaurant
* restaurant: Does the hotel have a restaurant ?
  - utter_restaurant

## breakfast_avail
* breakfast_avail: Does the hotel offer breakfast ?
  - utter_breakfast_avail

## breakfast_time
* breakfast_time: What are the breakfast timings ?
  - utter_breakfast_time

## restaurant_time
* restaurant_time: What are the restaurant timings ?
  - utter_restaurant_time

## clean_room
* clean_room: Could you send someone to clean my room ?
  - utter_clean_room

## say goodbye
* goodbye: bye-bye!
  - utter_goodbye

## bot challenge
* bot_challenge: are you a bot?
  - utter_iamabot
