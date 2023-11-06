from os import environ

SESSION_CONFIGS = [
    {
        'name': 'mini_ultimatum_game',
        'app_sequence': ['mini_ultimatum_game', 'exit_survey'],
        'num_demo_participants': 3,
        'num_rounds': 1,  # Adjust the number of rounds as needed
    },
]

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

# Define any custom fields you want to collect from participants and sessions here
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# Language and currency settings
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'KES'
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 2
USE_POINTS = False

# Admin username and password
ADMIN_USERNAME = 'admin'
# It's best to set the admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# Introductory HTML content for the demo page
DEMO_PAGE_INTRO_HTML = """ """

# Secret key for security
SECRET_KEY = 'your_secret_key_here''1921889376756'

# List of installed apps
INSTALLED_APPS = ['otree', 'mini_ultimatum_game', 'exit_survey']
