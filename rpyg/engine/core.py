from rpyg.cli import output, ui


class Rpyg:
    """
    Game engine encapsulated
    """
    def __init__(self, output=output, ui=ui, **kwargs):
        """
        Construct the new game

        :param output:
            function - optional - will output text - defaults to Cli package
        :param kwargs:
            name - string - name of game
            greeting - string - game greeting - defaults to nothing
            entry - string - keyname for the starting game frame - defaults to 'entry'
            frames - string - game frames
        :return: None
        """
        self.name = kwargs['name']
        self.greeting = kwargs.get('greeting', '')
        self.entry_frame = kwargs.get('entry', 'entry')
        self.frames = kwargs['frames']
        self.ui = ui
        self.output = output

        self.current_frame = self.entry_frame
        self.inventory = []

    def start(self):
        """
        Kick off game play

        :return: None
        """
        self.show_greeting()
        self.read_frame()

    def read_frame(self):
        """
        Read the current frame

        :return: None
        """
        frame = self.get_frame()
        if 'end' in frame:
            self.output(frame.get('intro', ''))
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
        """

        :param response:
        :return:
        """
        frame = self.get_frame()
        if response == 'exit' or response == 'quit':
            exit()
        if response == 'hint' or response == 'help':
            return self.prompt(self.show_hint())
        if self.get_movement_options().count(response):
            if response in frame['moves']:
                self.current_frame = frame['moves'][response]
                return self.read_frame()
            else:
                return self.do_action(response)
        else:
            self.output(' ')
            self.output('Dunno what you mean by "' + response + '", do you need help?')
            return self.prompt(self.show_hint())

    def do_action(self, action_name):
        action = self.get_frame_action(action_name)
        if 'item' in action:
            self.add_inventory(action['item'])
            self.current_frame = action['frame']
            self.output(' ')
            self.output('You have added [' + action['item'] + '] to your inventory!')
            self.output(str(self.inventory))
        if 'required' in action:
            if self.inventory.count(action['required']):
                self.current_frame = action['frame']
                self.output(' ')
                self.output(action['result'])
            else:
                self.output(' ')
                self.output('------------------------ ')
                self.output('Oh no! You are unable to ' + action_name + '.')
                self.output(' ')
                self.output('You need the [' + action['required'] + '] to ' + action_name + '!')
                self.output(' ')
                self.output('Find the [' + action['required'] + ']!')
                self.output('------------------------ ')
        else:
            if 'frame' in action:
                self.current_frame = action['frame']
            self.output(' ')
            self.output(action['result'])
        self.read_frame()

    def show_greeting(self):
        self.output(' ------------------------ ')
        self.output('You are now playing ' + self.name)
        self.output(self.greeting)
        self.output(' ------------------------ ')

    def prompt(self, question):
        self.output(' ')
        self.output(question)
        self.output(self.parse_response(str(self.ui())))
