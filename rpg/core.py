class Rpg:
    def __init__(self, **kwargs):
        """
        :param kwargs:
            name
            greeting
            frames
        """
        self.name = kwargs['name']
        self.greeting = kwargs['greeting']
        self.frames = kwargs['frames']

        self.current_frame = 'house'
        self.inventory = {}

    def start(self):
        self.show_greeting()
        self.read_frame(self.current_frame)

    def read_frame(self, frame_name):
        self.prompt(self.frames[frame_name]['intro'])

    def do_action(self, action_name):
        print(self.frames[self.current_frame]['actions'][action_name]['result'])
        self.read_frame(self.current_frame)

    def add_inventory(self):
        self.inventory = {}

    def get_movement_options(self):
        return [*self.frames[self.current_frame]['moves']] + [*self.frames[self.current_frame]['actions']]

    def show_hint(self):
        return 'These are your movement options: ' + str(self.get_movement_options())

    def parse_response(self, response):
        if response == 'hint':
            return self.prompt(self.show_hint())
        if response == 'help':
            return self.prompt(self.show_hint())
        if self.get_movement_options().count(response):
            if response in self.frames[self.current_frame]['moves']:
                self.current_frame = self.frames[self.current_frame]['moves'][response]
                return self.read_frame(self.current_frame)
            else:
                return self.do_action(response)

    def show_greeting(self):
        print('You are now playing ' + self.name)
        print(self.greeting)

    def prompt(self, question):
        print(' ')
        print(question)
        print(str(self.get_movement_options()))
        print(self.parse_response(str(input(''))))
