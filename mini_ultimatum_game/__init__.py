from otree.api import *
import random

doc = """
The Mini Ultimatum Game

Explore decision-making and human behavior in this social science experiment. 

Roles:
- Player 1: Decide how much to send to Player 2.
- Player 2: Receive offers from Player 1.
- Player 3 (the Punisher): Determine if Player 1's offer is fair.

Challenge your decision-making and discover the impact of your choices. Will you cooperate or compete? Play now to uncover economic dynamics and fairness in a fun way.
"""


class C(BaseConstants):
    NAME_IN_URL = 'mini_ultimatum_game'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT = cu(200)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    offer = models.CurrencyField(
        min=0, max=C.ENDOWMENT,
        label="How much money will you send to Player 2?",
    )

    punish_decision = models.BooleanField(
	    label="Will you punish Player 1?",
	    choices=[
	        [True, 'Punish'],
	        [False, 'Not Punish']
	    ],
	    widget=widgets.RadioSelectHorizontal
	)

    def set_payoffs(self):
	    player1 = self.get_player_by_id(1)
	    player2 = self.get_player_by_id(2)
	    player3 = self.get_player_by_id(3)

	    if self.punish_decision:
	        player1.payoff = 0
	        player2.payoff = 0
	    else:
	        player1.payoff = 200 - self.offer
	        player2.payoff = self.offer
	        player3.payoff = 0


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'Player 1'
        elif self.id_in_group == 2:
            return 'Player 2'
        else:
            return 'Player 3 (Punisher)'


# PAGES
class Offer(Page):
    form_model = 'group'
    form_fields = ['offer']

    def is_displayed(self):
    	return self.id_in_group == 1

    def vars_for_template(self):
        player1 = self.group.get_player_by_id(1)

        return {
            'endowment': C.ENDOWMENT,
        }


class WaitForOffer(WaitPage):
    pass


class Decision(Page):
    form_model = 'group'
    form_fields = ['punish_decision']

    def is_displayed(self):
    	return self.id_in_group == 3

    def vars_for_template(self):
        player1 = self.group.get_player_by_id(1)

        return {
        	'endowment': C.ENDOWMENT, 
            'player1_offer': self.group.offer,
        }


class WaitForResults(WaitPage):
    def after_all_players_arrive(self):
    	self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        player1 = self.group.get_player_by_id(1)
        player2 = self.group.get_player_by_id(2)
        player3 = self.group.get_player_by_id(3)

        return {
            'player1_offer': self.group.offer,
            'player3_decision': self.group.punish_decision,
            'player1_payout': player1.payoff,
            'player2_offer': player1.group.offer,
            'player2_payout': player2.payoff,
        }
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
    	if player:
        	return "exit_survey"


page_sequence = [Offer, WaitForOffer, Decision, WaitForResults, Results]
