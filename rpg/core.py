class Rpg:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.greeting = kwargs['greeting']
        self.frames = kwargs['frames']
        self.current_frame = 'entry'

    def start(self):
        self.show_greeting()
        self.read_frame(self.current_frame)

    def read_frame(self, frame_name):
        self.prompt(self.frames[frame_name]['intro'])

    def show_hint(self):
        return 'These are your options: ' + str([*self.frames[self.current_frame]['moves']])

    def parse_response(self, response):
        if response == 'hint':
            return self.prompt(self.show_hint())
        if response == 'help':
            return self.prompt(self.show_hint())
        else:
            self.current_frame = self.frames[self.current_frame]['moves'][response]
            return self.read_frame(self.current_frame)

    def show_greeting(self):
        print('You are now playing ' + self.name)
        print(self.greeting)

    def prompt(self, question):
        print(self.parse_response(str(input(question))))
