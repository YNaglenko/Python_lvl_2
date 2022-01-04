# def dec(f):
#     def get_name(n):
#         return "Hello" + str(f(n))
#
#     return get_name()
#
#
# @dec
# def up_name(str_name):
#     return str(str_name).capitalize()

def name_dec(f):
    def hello_name(name):
        return "Hello " + f(name)

    return hello_name


@name_dec
def up_name(str_name):
    return str(str_name).capitalize()


print(up_name('alex'))
