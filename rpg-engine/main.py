def parse_response(response):
    if response == 'hint':
        print('equals hint')
        return 'you seem to need help!'
    else:
        return 'you entered ' + response


def prompt(question):
    user_input = str(input(question))
    response = parse_response(user_input)
    print(response)


prompt('what is your name? ')
