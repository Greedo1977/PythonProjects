def get_formatted_name(first, last, middle = None):

    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'

    return full_name.title()

def get_name_reverse(first, last):
    reverse_formatted = f'{last} {first}'
    return reverse_formatted
