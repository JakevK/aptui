import text, window, readchar, re



window_dimensions = window.dimensions()
window_x = window_dimensions["x"]
window_y = window_dimensions["y"]



def multi_choice(title, options, width=0):

    margin_top = (window_y - len(options) - 1) // 2 - 1
    margin_bottom = window_y - len(options) - margin_top - 5

    width = max(max(map(len, options)), width)


    title_display = text.center(title, width)
    title_display = text.decorate(
        title_display, 
        bold=1, 
        color="blue", 
        underline=1
    )
    title_display = text.center(title_display)


    selected = 0

    while True:
        window.clear()


        options_display = [option.ljust(width) for option in options]
        options_display[selected] = text.decorate(
            options_display[selected], 
            reversed=1
        )
        options_display = [text.center(option) for option in options_display]


        print('\n' * margin_top)

        print(title_display + '\n')

        for option in options_display:
            print(option)

        print('\n' * margin_bottom)


        key_press = readchar.readkey()

        if key_press == readchar.key.DOWN:
            if selected < len(options) - 1:
                selected += 1
            else:
                selected = 0
        elif key_press == readchar.key.UP:
            if selected:
                selected -= 1
            else:
                selected = len(options) - 1

        elif key_press == readchar.key.ENTER:
            window.clear()
            return options[selected]



def type_input(message, min_length, max_length, validation_func=None):
    margin_top = (window_y - 3) // 2 - 1
    margin_bottom = window_y - margin_top - 6

    message_display = text.decorate(message, color="blue")
    message_display = text.center(message_display)


    chars = []
    cursor_pos = 0
    
    while True:
        window.clear()

        
        formatted_chars = [*chars, ' ']
        formatted_chars[cursor_pos] = text.decorate(
            formatted_chars[cursor_pos], 
            reversed=1
        )
        formatted_chars = ' ' + ''.join(formatted_chars)
        formatted_chars = text.center(
            formatted_chars, 
            max(
                len(chars), 
                max_length + 2
            )
        )
        formatted_chars = text.decorate(formatted_chars, underline=1)
        formatted_chars = text.center(formatted_chars)


        print('\n' * margin_top)
        print(message_display + '\n')
        print(formatted_chars)
        print('\n' * margin_bottom)


        key_press = readchar.readkey()

        if key_press == readchar.key.LEFT:
            if cursor_pos:
                cursor_pos -= 1
        elif key_press == readchar.key.RIGHT:
            if cursor_pos < len(chars):
                cursor_pos += 1

        elif key_press == readchar.key.BACKSPACE:
            if cursor_pos:
                chars.pop(cursor_pos - 1)
                cursor_pos -= 1

        elif key_press == readchar.key.ENTER:
            return ''.join(chars)

        elif len(repr(key_press)) == 3:
            if len(chars) < max_length and validation_func(chars, key_press):
                chars.insert(cursor_pos, key_press)
                cursor_pos += 1


def str_validation(chars, new_char):
    return True

def str_input(message, min_length, max_length):
    return type_input(min_length, max_length)


def int_input(message, min_value, max_value):
