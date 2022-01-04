
class UpperNameDecorator:
    def __init__(self, f):
        self.f = f
    def __call__(self, s_name):
        file = open(s_name + ".txt", "w")
        file.write(self.f(s_name))
        file.close()


@UpperNameDecorator
def up_name(str_name):
    return str(str_name).upper()


s_name = 'hello!!!'
print(up_name(s_name))
