import text, window, readchar



window_dimensions = window.dimensions()
window_x = window_dimensions["x"]
window_y = window_dimensions["y"]



def multi_choice(title, options, width=0):
    selected = 0

    while True:
        window.clear()

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


def text_input(message, validation):
    pass