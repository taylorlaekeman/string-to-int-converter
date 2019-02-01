class StringToIntConverter():
    def __init__(self, string_to_convert):
        self.string_wrapper = StringWrapper(string_to_convert)
        self.converted_int = 0

    def convert(self):
        while not self.string_wrapper.is_empty():
            char = self.string_wrapper.pop()
            self.add_digit(char)
        return self.converted_int

    def add_digit(self, char):
        self.converted_int *= 10
        self.converted_int += cast_char_to_int(char)

class StringWrapper():
    def __init__(self, string):
        self.string = string

    def pop(self):
        char = self.string[0]
        self.string = self.string[1:]
        return char

    def is_empty(self):
        return self.string == "" or self.string == None

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
