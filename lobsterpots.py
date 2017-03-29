import random,time
import math as maths
def init(days,diff):
    print('Initialising...')
    days_to_play=days
    difficulty=diff
    diff_calc=6-diff
    pots_done=diff_calc
    money_done=10*diff_calc
    global days_to_play,difficulty,pots_done,money_done
def startup():
    print('Welcome to LobsterPotsInfinity - UltimateEdition(v0.0(pre prod.))')
    days=int(input('Please enter the number of game days you wish to play LPIUE for(please enter a number 7-28:'))
    if days<7 or days>28:
             days=int(input('Please enter a valid number:'))
    diff=int(input('Plese enter a difficulty level between 1 and 5:'))
    if diff<1 or diff>5:
        diff=int(input('Please enter a valid number:'))
    init(days,diff)
def main():
    startup()
    print('Preparing to load...')
    global days_to_play,difficulty,pots_done,money_done
    days_played=0
    print('Loading...')
    while days_played<days_to_play:
        play_day(days_played,pots_done,money_done)
        global pots_done,money_done,days_to_play
        days_played=days_played+1
    finish(pots_done,money_done,difficulty)
def play_day(days_played,pots,money):
    days_to_show=days_played+1
    print('Day ',days_to_show,':')
    lobster_bulletin_price=0.4*difficulty
    diff_calc_two=16-difficulty
    lobster_base_price=random.randint(1,diff_calc_two)
    clip=lobster_base_price
    clop=clip*2
    llip=clop*5
    llop=llip*2
    print('Lobster prices today at Lob$t@M@rt:')
    print('Common inshore lobsters fetch £',clip,' whilst common offshores, £',clop)
    print('Inshore and offshore lobbable lobster fetch £',llip,' and £',llop,' respectively')
    newspaper_statement=str('Enter y to buy a newspaper with weather and lobster abundance information for £')+str(lobster_bulletin_price)+str(' or any other key to cancel:')
    newspaper_brought=input(newspaper_statement)
    bad_weather_max=20*difficulty
    divider_li=50*difficulty
    divider_lo=10*difficulty
    if difficulty==1:
        divider_c=difficulty
    else:
        divider_c=0.5*difficulty
    bad_weather_odds=random.randint(1,bad_weather_max)
    lobbable_lobster_chance_i=random.randint(1,100)
    lobbable_lobster_chance_o=random.randint(1,100)
    lobbable_lobster_chance_i_percent=lobbable_lobster_chance_i/divider_li
    lobbable_lobster_chance_o_percent=lobbable_lobster_chance_o/divider_lo
    common_lobster_chance_i=random.randint(10,99)
    common_lobster_chance_o=random.randint(15,95)
    common_lobster_chance_i_percent=common_lobster_chance_i/divider_c
    common_lobster_chance_o_percent=common_lobster_chance_o/divider_c
    if newspaper_brought=='y':
        if money>lobster_bulletin_price:
            newspaper_line_5=str('  lobbable lobster is '+str(lobbable_lobster_chance_i_percent)+'%. The   ')
            newspaper_line_7=str('are '+str(lobbable_lobster_chance_o_percent)+'%. The chances of catching a ')
            newspaper_line_8=str(' common lobster are '+str(common_lobster_chance_i_percent)+'% inshore and ')
            newspaper_line_9=str(str(common_lobster_chance_o_percent)+'% offshore.[Bill The Reporter]')
            newspaper_line_11=str('There is a '+str(bad_weather_odds)+'% chance of bad weather')
            print('************************************')
            print('--------The Lobster Bulletin--------')
            print('^^^^^^^^^^^^^^HEADLINES^^^^^^^^^^^^^')
            print('  The chance of catching an inshore ')
            print(newspaper_line_5)
            print(' chance of catching an offshore one ')
            print(newspaper_line_7)
            print(newspaper_line_8)
            print(newspaper_line_9)
            print('<<<<<<<<<<<<<<<WEATHER>>>>>>>>>>>>>>')
            print(newspaper_line_11)
            money=money-lobster_bulletin_price
        else:
            print("You can't afford a newspaper")
    print('You have ',pots,' pots.')
    pots_placed_offshore=int(input('Enter the number of pots placed offshore. If you enter a number higher than the number of pots you own; you will not place any pots offshore:'))
    if pots_placed_offshore>pots:
        print('Invalid Input')
        pots_placed_offshore_final=0
    else:
        pots_placed_offshore_final=pots_placed_offshore
    pots_placed_inshore=pots-pots_placed_offshore_final
    pots_done=pots
    money_done=money
    if difficulty>2:
        c_l_o=common_lobster_chance_o_percent*pots_placed_offshore_final
        c_l_o_f=c_l_o/100
        clof=maths.floor(c_l_o_f)
        pots_placed_offshore_final_new=pots_placed_offshore_final-c_l_o_f
        c_l_i=common_lobster_chance_i_percent*pots_placed_inshore
        c_l_i_f=c_l_i/100
        clif=maths.floor(c_l_i_f)
        pots_placed_inshore_final=pots_placed_inshore-c_l_i_f
        l_l_o=lobbable_lobster_chance_o_percent*pots_placed_offshore_final_new
        l_l_o_f=l_l_o/100
        llof=maths.floor(l_l_o_f)
        pots_placed_offshore_final_new=pots_placed_offshore_final_new-l_l_o_f
        l_l_i=lobbable_lobster_chance_i_percent*pots_placed_inshore
        l_l_i_f=l_l_i/100
        llif=maths.floor(l_l_i_f)
        pots_placed_inshore_final=pots_placed_inshore_final-l_l_i_f
    else:
        l_l_o=lobbable_lobster_chance_o_percent*pots_placed_offshore_final
        l_l_o_f=l_l_o/100
        llof=maths.floor(l_l_o_f)
        pots_placed_offshore_final_new=pots_placed_offshore_final-l_l_o_f
        l_l_i=lobbable_lobster_chance_i_percent*pots_placed_inshore
        l_l_i_f=l_l_i/100
        llif=maths.floor(l_l_i_f)
        pots_placed_inshore_final=pots_placed_inshore-l_l_i_f
        c_l_o=common_lobster_chance_o_percent*pots_placed_offshore_final_new
        c_l_o_f=c_l_o/100
        clof=maths.floor(c_l_o_f)
        pots_placed_offshore_final_new=pots_placed_offshore_final_new-c_l_o_f
        c_l_i=common_lobster_chance_i_percent*pots_placed_inshore
        c_l_i_f=c_l_i/100
        clif=maths.floor(c_l_i_f)
        pots_placed_inshore_final=pots_placed_inshore_final-c_l_i_f
    bad_w_computational_odds=bad_weather_odds/100
    multiplier=random.random()
    if bad_w_computational_odds>multiplier:
        weather='BAD'
        pots=pots-pots_placed_offshore_final
    else:
        weather='good'
        money_earnt=clof*clop
        money=money+money_earnt
        money_earnt=llof*llop
        money=money+money_earnt
    money_earnt=clif*clip
    money=money+money_earnt
    money_earnt=llif*llip
    money=money+money_earnt 
    print('The weather is:')
    print(weather)
    print('You caught:')
    if weather=='good':
        print('Common lobsters offshore*',clof)
        print('Lobbable lobsters offshore*',llof)
    else:
        print('Common lobsters offshore*0')
        print('Lobbable lobsters offshore*0')
    print('Common lobsters inshore*',clif)
    print('Lobbable lobsters inshore*',llif)
    multiplier=random.random()
    multiplier=multiplier*difficulty
    multiplier=multiplier*5
    pot_price=maths.ceil(multiplier)
    money_pennies=money*100
    money_pennies=maths.ceil(money_pennies)
    money=money_pennies/100
    print('You have ',pots,' pots and £',money)
    print('The price of pots is £',pot_price)   
    pots_bought=int(input('How many pots do you wish to buy:'))
    money_spent=pots_bought*pot_price
    if money_spent<=money:
        pots_done=pots+pots_bought
        money_done=money-money_spent
    else:
        print("You can't afford that!")
    global pots_done,money_done
    print('Day complete')
def finish(pots_done,money_done,difficulty):
    global days_to_play
    print('Proccessing you score...')
    if difficulty==1:
        pots_value=20*pots_done
    elif difficulty==2:
        pots_value=15*pots_done
    elif difficulty==3 or difficulty==4:
        pots_value=10*pots_done
    else:
        pots_value=5*pots_done
    final_takings=money_done+pots_value
    diff_calc=6-difficulty
    money_start=diff_calc*10
    final_profit=final_takings-money_start
    score_average=0
    if difficulty==1:
        score_average=2000*days_to_play
    elif difficulty==2:
        score_average=200*days_to_play
    elif difficulty==3:
        score_average=150*days_to_play
    elif difficulty==4:
        score_average=20*days_to_play
    elif difficulty==5:
        score_average=2*days_to_play
    score_average_min=score_average*0.9
    score_average_max=score_average*1.1
    score_poor_min=score_average*0.5
    score_good_max=score_average*2
    if final_profit<score_poor_min:
        rating='very poor!'
    elif final_profit<score_average_min:
        rating='poor.'
    elif final_profit<score_average_max:
        rating='average.'
    elif final_profit<score_good_max:
        rating='good.'
    else:
        rating='very good!'
    print('Your final score (profit) of ',final_profit,' pounds gives you a rating of ',rating)
    print('Done')
    time.sleep(30)
main()
