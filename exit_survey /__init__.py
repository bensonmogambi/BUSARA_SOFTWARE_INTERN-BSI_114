from otree.api import *

doc = """

The Exit Survey

This app is designed to collect additional info and feedback from participants after completing the  Game.
	
The survey includes questions about the capital cities of Kenya, a mathemathical problem, and the population of Kenya.

Thanks for Your Participation.

"""

class C(BaseConstants):
    NAME_IN_URL = 'ExitSurvey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    capital_city = models.IntegerField(
        label="What is the capital city of Kenya?",
        choices=[
            [1, 'Kisumu'],
            [2, 'Nairobi'],
            [3, 'Mombasa'],
        ],
        widget=widgets.RadioSelect,
    )

    math_problem = models.IntegerField(
        label="What is 14 + 15?",
    )

    kenya_population = models.IntegerField(
        label="What is the population of Kenya?",
    )

    def correct_math_problem_answer(self):
    	return self.math_problem == 29


# PAGES
class CapitalCity(Page):
    form_model = 'player'
    form_fields = ['capital_city']


class MathProblem(Page):
    form_model = 'player'
    form_fields = ['math_problem']

    def error_message(self, values):
        if values['math_problem'] != 29:
            return 'Your answer to the math problem is incorrect. Please provide the correct answer.'


class PopulationPage(Page):
    form_model = 'player'
    form_fields = ['kenya_population']


class ThankYou(Page):
    pass

page_sequence = [CapitalCity, MathProblem, PopulationPage, ThankYou]
