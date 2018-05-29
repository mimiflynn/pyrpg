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
        self.inventory = []

    def start(self):
        self.show_greeting()
        self.read_frame(self.current_frame)

    def read_frame(self, frame_name):
        self.prompt(self.frames[frame_name]['intro'])

    def get_frame(self):
        return self.frames[self.current_frame]

    def get_frame_action(self, action_name):
        frame = self.get_frame()
        return frame['actions'][action_name]

    def add_inventory(self, item):
        self.inventory.append(item)

    def get_movement_options(self):
        frame = self.get_frame()
        return [*frame['moves']] + [*frame['actions']]

    def show_hint(self):
        return 'These are your movement options: ' + str(self.get_movement_options())

    def parse_response(self, response):
        frame = self.get_frame()
        if response == 'hint':
            return self.prompt(self.show_hint())
        if response == 'help':
            return self.prompt(self.show_hint())
        if self.get_movement_options().count(response):
            if response in frame['moves']:
                self.current_frame = frame['moves'][response]
                return self.read_frame(self.current_frame)
            else:
                return self.do_action(response)

    def do_action(self, action_name):
        action = self.get_frame_action(action_name)
        if 'item' in action:
            self.add_inventory(action['item'])
            self.current_frame = action['frame']
            print(' ')
            print('You have added ' + action['item'] + ' to your inventory!')
            print(str(self.inventory))
            print(' ')
            print(action['result'])
        if 'required' in action:
            if self.inventory.count(action['required']):
                self.current_frame = action['frame']
                print(' ')
                print(action['result'])
            else:
                print(' ')
                print('You need the ' + action['required'] + ' to do this action!')
        else:
            print(' ')
            print(action['result'])
        self.read_frame(self.current_frame)

    def show_greeting(self):
        print('You are now playing ' + self.name)
        print(self.greeting)

    def prompt(self, question):
        print(' ')
        print(question)
        print(str(self.get_movement_options()))
        print(self.parse_response(str(input(''))))
