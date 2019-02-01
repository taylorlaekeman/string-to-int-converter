class StringToIntConverter():
    def __init__(self, string_to_convert):
        self.string_to_convert = string_to_convert

    def convert(self):
        converted_int = 0
        while not self.string_is_empty():
            char, self.string_to_convert = pop_first_char(self.string_to_convert)
            converted_int *= 10
            converted_int += cast_char_to_int(char)
        return converted_int

    def string_is_empty(self):
        empty_string_formats = ["", None]
        return self.string_to_convert in empty_string_formats

def pop_first_char(word):
    char = word[0]
    shortened_word = word[1:]
    return char, shortened_word

def cast_char_to_int(char):
    if char == '1':
        return 1
    elif char == '2':
        return 2
    elif char == '3':
        return 3
    elif char == '4':
        return 4
    elif char == '5':
        return 5
    elif char == '6':
        return 6
    elif char == '7':
        return 7
    elif char == '8':
        return 8
    elif char == '9':
        return 9
    else:
        return 0
