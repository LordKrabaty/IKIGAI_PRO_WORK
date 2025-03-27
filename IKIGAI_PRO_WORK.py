"""Main module"""

# IMPORTS
from src import ikidef, ikidraw

# USER DATA -----------------------------------------------------------------------------------

draw_iki = False  # Whether to provide a visualization of the final results
ask_name = 'What is your name?'

# Get the user's name with proper length constraints
user_name = ikidef.input_limit(ask_name, 2, 30)
# Extract the first name from the full name (if applicable)
first_name = ikidef.first_word(user_name, ' ')
# Record the current date
test_date = ikidef.current_date()

###################### QUESTIONNAIRE #######################################

# FIRST SET OF QUESTIONS ---------------------------------------------------
# (Assigned to true/false variables based on the answers)
# (Always asked)

# Value limits
value_minTrue = 5  # Threshold for a "true" evaluation
value_max = 10  # Maximum possible value
value_min = 0  # Minimum possible value

# First set of questions
ask_love = 'How much do you love your job?'
ask_world = 'How much does your work help make the world a better place?'
ask_money = 'How satisfied are you with your earnings?'
ask_good = 'How good are you at it?'

# Get numerical input for each question and evaluate if it meets the threshold
value_love = ikidef.ask_for_number(ask_love, value_min, value_max)
ok_love = ikidef.true_or_not(value_love, value_minTrue)

value_world = ikidef.ask_for_number(ask_world, value_min, value_max)
ok_world = ikidef.true_or_not(value_world, value_minTrue)

value_money = ikidef.ask_for_number(ask_money, value_min, value_max)
ok_money = ikidef.true_or_not(value_money, value_minTrue)

value_good = ikidef.ask_for_number(ask_good, value_min, value_max)
ok_good = ikidef.true_or_not(value_good, value_minTrue)

# COUNTING FOR EVALUATION --------------------------------------------------

from statistics import mean

# LWMG (Love, World, Money, Good) values
LWMG = (value_love, value_world, value_good, value_money)
score_LWMG_sum = sum(LWMG)
score_LWMG_avr = mean(LWMG)
score_LWMG_min = min(LWMG)

# Calculate PMVP (Passion, Mission, Vocation, Profession) values based on averages of LWMG
passion = (value_good, value_love)
value_passion = mean(passion)
ok_passion = ikidef.true_or_not(value_passion, value_minTrue)

mission = (value_world, value_love)
value_mission = mean(mission)
ok_mission = ikidef.true_or_not(value_mission, value_minTrue)

vocation = (value_world, value_money)
value_vocation = mean(vocation)
ok_vocation = ikidef.true_or_not(value_vocation, value_minTrue)

profession = (value_good, value_money)
value_profession = mean(profession)
ok_profession = ikidef.true_or_not(value_profession, value_minTrue)

PMVP = (value_passion, value_mission, value_vocation, value_profession)
score_PWMP_min = min(PMVP)
score_PWMP_sum = sum(PMVP)
score_PWMP_avr = mean(PMVP)

# RESULTS AND ADDITIONAL QUESTIONS ----------------------------------------

msg_results = f'\n{first_name}, your average rating is {score_LWMG_avr}. Your lowest grade awarded is {score_LWMG_min}. '

msg_congrat = "Congratulations! Keep doing what you're doing."
msg_under_limit = "You have some values under the limit. You need to work on improving them."
msg_improve = 'Still, you can make some improvements based on your lowest grade(s).'

positive = 'yes'
negative = 'no'

yn_instructions = f'Answer {positive}/{negative}'
msg_error = f'{yn_instructions} as instructed. Write in lowercase!'

ask_yn_love = ask_yn_world = ask_yn_money = ask_yn_good = False  # Flags for yes/no follow-up questions

text_conclusion = '-'  # Conclusion text for `ikidraw`, to be updated based on results
text_advice = '-'

make_love = make_world = make_money = make_good = False  # Flags for additional advice (yes/no questions)

# RESULTS IF EVERYTHING MAX → RANDOM

give_random = False  # Initially set to False for random advice
ask_random = f'There is probably nothing to improve. {yn_instructions}: Do you want random advice to just check it?'
ask_random_again = f'{yn_instructions}: Do you want another random message?'

if score_LWMG_avr == value_max:
    print(msg_results, msg_congrat, sep='', end='')
    text_conclusion = msg_congrat
    give_random = ikidef.ask_for_yn(ask_random, positive, negative, msg_error)

    if not give_random:  # If no random advice is requested, end here
        draw_iki = True

# OTHER SCENARIOS ----------------------------------------------------------

elif ok_passion and ok_mission and ok_vocation and ok_profession and score_PWMP_avr < value_max:
    print(msg_results, msg_congrat, msg_improve, '\n', sep='')

    if score_PWMP_min == value_passion:
        ask_yn_love = ask_yn_good = True
    if score_PWMP_min == value_mission:
        ask_yn_love = ask_yn_world = True
    if score_PWMP_min == value_vocation:
        ask_yn_world = ask_yn_money = True
    if score_PWMP_min == value_profession:
        ask_yn_money = ask_yn_good = True

elif not ok_passion or not ok_mission or not ok_vocation or not ok_profession:
    print(msg_results, msg_under_limit, '\n', sep='')

    if not ok_passion:
        ask_yn_love = ask_yn_good = True
    if not ok_mission:
        ask_yn_love = ask_yn_world = True
    if not ok_vocation:
        ask_yn_world = ask_yn_money = True
    if not ok_profession:
        ask_yn_money = ask_yn_good = True

else:
    msg_unexpected = 'Unexpected result. Please contact the developer!'
    print(msg_unexpected)

# ADDITIONAL QUESTIONS -----------------------------------------------------

ask_love2 = f'{yn_instructions}: Can the environment you work in be improved (e.g., music, people, good tea during tasks)?'
ask_world2 = f'{yn_instructions}: Is there a small part of your work that helps/makes someone happy, and could you do more of it?'
ask_money2 = f'{yn_instructions}: Can you ask for more money?'
ask_good2 = f'{yn_instructions}: Is there anything you could learn to improve your skills?'

if ask_yn_love:
    make_love = ikidef.ask_for_yn(ask_love2, positive, negative, msg_error)
if ask_yn_world:
    make_world = ikidef.ask_for_yn(ask_world2, positive, negative, msg_error)
if ask_yn_money:
    make_money = ikidef.ask_for_yn(ask_money2, positive, negative, msg_error)
if ask_yn_good:
    make_good = ikidef.ask_for_yn(ask_good2, positive, negative, msg_error)

# RESULTS FROM ADDITIONAL QUESTIONS ----------------------------------------

msg_try_love = 'You can try to improve your work environment.'
msg_try_world = 'You can try to magnify the parts of your work that make someone happy.'
msg_try_money = 'You can try to negotiate for more money.'
msg_try_good = 'You can try to learn skills to improve your performance.'

msg_try = f'Try applying the advice given and retake this test. {first_name}, I know you can do it!'

msg_miss = '\nYou are missing in your current job:'

name_passion = 'Passion'
name_mission = 'Mission'
name_vocation = 'Vocation'
name_profession = 'Profession'

msg_under = "You cannot improve your essential grade(s) under the limit!"
msg_change_job = "You might need to consider changing jobs!"
msg_sorry = f"I'm sorry, {first_name}! {msg_under} {msg_change_job}"

msg_gaps = 'You have critical gaps in some areas, but you can address them!'
msg_space = 'Your score is fine. Still, there is room for improvement if you wish.'
msg_still_ok = "You cannot improve your lowest grade, but your score is fine."

try_love = try_good = try_money = try_world = False  # Flags for showing specific advice in final results

temp_advice = '{adv}\n   - {plus}'  # Template for displaying each piece of advice on a new line

# RANDOM ADVICE LOOP -------------------------------------------------------

while give_random:
    random_ask = True
    if random_ask:
        import random
        give_random = True
        text_advice = '   Just a random check:'
        random_advice = random.choice([msg_try_good, msg_try_love, msg_try_money, msg_try_world])
        print(random_advice, end=" ")
        text_advice = temp_advice.format(adv=text_advice, plus=random_advice)
        random_ask = ikidef.ask_for_yn(ask_random_again, positive, negative, msg_error)

    if not random_ask:
        give_random = False
        draw_iki = True
        break

# WHAT PMVP VALUES ARE MISSING ---------------------------------------------

if not ok_passion or not ok_mission or not ok_vocation or not ok_profession:
    print(msg_miss)
    if not ok_passion:
        print('\t -', name_passion)
    if not ok_mission:
        print('\t -', name_mission)
    if not ok_vocation:
        print('\t -', name_vocation)
    if not ok_profession:
        print('\t -', name_profession)

    if (not ok_passion and (not make_good and not make_love)) or \
       (not ok_mission and (not make_world and not make_love)) or \
       (not ok_vocation and (not make_world and not make_money)) or \
       (not ok_profession and (not make_good and not make_money)):
        print('\n', msg_sorry, sep='', end=" ")
        text_conclusion = msg_under
        text_advice = msg_change_job
        draw_iki = True

elif (not ok_passion and (make_good or make_love)) or \
     (not ok_mission and (make_world or make_love)) or \
     (not ok_vocation and (make_world or make_money)) or \
     (not ok_profession and (make_good or make_money)):
    print('\n', msg_gaps, sep='', end=" ")
    text_conclusion = msg_gaps

    if not ok_passion and make_love:
        try_love = True
    if not ok_passion and make_good:
        try_good = True
    if not ok_mission and make_love:
        try_love = True
    if not ok_mission and make_world:
        try_world = True
    if not ok_vocation and make_money:
        try_money = True
    if not ok_vocation and make_world:
        try_world = True
    if not ok_profession and make_money:
        try_money = True
    if not ok_profession and make_good:
        try_good = True

    text_advice = '   You really need to focus on improving:'

    if try_love:
        print(msg_try_love, end=" ")
        text_advice = temp_advice.format(adv=text_advice, plus=msg_try_love)
    if try_good:
        print(msg_try_good, end=" ")
        text_advice = temp_advice.format(adv=text_advice, plus=msg_try_good)
    if try_world:
        print(msg_try_world, end=" ")
        text_advice = temp_advice.format(adv=text_advice, plus=msg_try_world)
    if try_money:
        print(msg_try_money, end=" ")
        text_advice = temp_advice.format(adv=text_advice, plus=msg_try_money)

    print(msg_try, end=" ")
    draw_iki = True

elif (ok_passion and ok_mission and ok_vocation and ok_profession) and score_LWMG_avr < value_max:
    text_conclusion = msg_space

    if make_love:
        try_love = True
    if make_good:
        try_good = True
    if make_money:
        try_money = True
    if make_world:
        try_world = True

    text_advice = '   Optional space for improvement:'

    if try_love:
        print(msg_try_love, end=" ")
        text_advice = temp_advice.format(adv=text_advice, plus=msg_try_love)
    if try_good:
        print(msg_try_good, end=" ")
        text_advice = temp_advice.format(adv=text_advice, plus=msg_try_good)
    if try_world:
        print(msg_try_world, end=" ")
        text_advice = temp_advice.format(adv=text_advice, plus=msg_try_world)
    if try_money:
        print(msg_try_money, end=" ")
        text_advice = temp_advice.format(adv=text_advice, plus=msg_try_money)

    if not make_love and not make_world and not make_money and not make_good:
        print(msg_still_ok, end='')
        text_conclusion = msg_still_ok
        text_advice = ''

    draw_iki = True

###################### DRAW #######################################

if draw_iki:
    ikidraw.ikigai_draw(value_love, value_good, value_money, value_world, value_max, value_minTrue, 
                        text_conclusion, text_advice, user_name, test_date)

