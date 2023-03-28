import PlotBodes as plot
from PyInquirer import prompt, print_json

questions = [
    {
        'type': 'input',
        'name': 'number_of_bodies',
        'message': '\nHow many planets would you like to simulate?',
        'validate': lambda answers: '3',
        'default': lambda val: (val.isnumeric() and int(val) > 1) or 'Please enter a valid integer larger than 1.'
        'filter': lambda val: int(val)
    },
    {
        'type': 'list',
        'name': 'initial_conditions_generator',
        'message': 'How would you like to generate the initial conditions?',
        'choices': ['Manual', 'Automatic'],
        'filter': lambda val: val.lower()
    }

]

answers1 = prompt.prompt(questions, style=custom_style_3)
if (answer.get('initial_conditions_generator') == 'manual'):
    for (answers.get('number_of_bodies')

