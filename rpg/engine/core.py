from rpg.cli import Cli

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
        self.output = kwargs.get('output', Cli)

        self.current_frame = 'entry'
        self.inventory = []

    def start(self):
        self.show_greeting()
        self.read_frame()

    def read_frame(self):
        frame = self.get_frame()
        if 'end' in frame:
            self.output('Game Over')
            exit()
        else:
            self.prompt(self.get_frame()['intro'])

    def get_frame(self):
        return self.frames[self.current_frame]

    def get_frame_action(self, action_name):
        frame = self.get_frame()
        return frame['actions'][action_name]

    def add_inventory(self, item):
        self.inventory.append(item)

    def get_movement_options(self):
        frame = self.get_frame()
        return [*frame.get('moves', {})] + [*frame.get('actions', {})]

    def show_hint(self):
        return 'These are your movement options: ' + str(self.get_movement_options())

    def parse_response(self, response):
        frame = self.get_frame()
        if response == 'hint' or response == 'help':
            return self.prompt(self.show_hint())
        if self.get_movement_options().count(response):
            if response in frame['moves']:
                self.current_frame = frame['moves'][response]
                return self.read_frame()
            else:
                return self.do_action(response)

    def do_action(self, action_name):
        action = self.get_frame_action(action_name)
        if 'item' in action:
            self.add_inventory(action['item'])
            self.current_frame = action['frame']
            self.output(' ')
            self.output('You have added ' + action['item'] + ' to your inventory!')
            self.output(str(self.inventory))
        if 'required' in action:
            if self.inventory.count(action['required']):
                self.current_frame = action['frame']
                self.output(' ')
                self.output(action['result'])
            else:
                self.output(' ')
                self.output('You need the ' + action['required'] + ' to do this action!')
        else:
            if 'frame' in action:
                self.current_frame = action['frame']
            self.output(' ')
            self.output(action['result'])
        self.read_frame()

    def show_greeting(self):
        self.output('You are now playing ' + self.name)
        self.output(self.greeting)

    def prompt(self, question):
        self.output(' ')
        self.output(question)
        self.output(str(self.get_movement_options()))
        self.output(self.parse_response(str(input(''))))
