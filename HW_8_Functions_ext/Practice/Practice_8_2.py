class SaySomething:
    def __init__(self):
        self.saved_word = ""

    def __str__(self):
        return "str={}".format(self.saved_word)

    def __call__(self, word=None):
        if word is None:
            return self.saved_word
        else:
            tmp_string = self.saved_word
            self.saved_word = word
            return tmp_string


f = SaySomething()
print(f("Hi"))
print(f())
print(f())
print(f("friend"))
print(f())
print(f())

