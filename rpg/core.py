class Rpg:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.greeting = kwargs['greeting']
        self.show_greeting()
        self.prompt('A stream is to your left and mountains are on the horizon. What direction do you want to go? ')

    def show_greeting(self):
        print(self.greeting)

    @staticmethod
    def parse_response(self, response):
        if response == 'hint':
            print('equals hint')
            return 'you seem to need help!'
        else:
            return 'you entered ' + response

    def prompt(self, question):
        user_input = str(input(question))
        response = self.parse_response(user_input)
        print(response)
