import window, re, json



window_x = window.dimensions()["x"]



def strip_ansi(text):
    # used this because I'm not very good at regex
    # https://stackoverflow.com/questions/14693701/how-can-i-remove-the-ansi-escape-sequences-from-a-string-in-python
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    
    return ansi_escape.sub('', text)


def center(text, width=None):
    if width == None:
        width = window_x

    text_len = len(strip_ansi(text))

    margin_left = (width - text_len) // 2
    margin_right = width - text_len - margin_left

    return ' ' * margin_left + text + ' ' * margin_right
    

def decorate(text, **args):
    ansi_codes = json.load(open("ansi_codes.json"))
    
    prefixes = []
    for key, value in args.items():
        if isinstance(subsection := ansi_codes[key], str) and value:
            prefixes.append(subsection)
        else:
            prefixes.append(subsection[value])
    
    clean = ansi_codes["none"]
    return (clean + ''.join(prefixes)).join((clean + text).split(clean)) + clean
