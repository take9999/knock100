#a simple game test

def print_test():
    verb1 = verb_dict["say"]
    print(verb1("TEST"))

def say(noun):
    return "You said '{}'".format(noun)
#
# def say2(noun):
#     return "You said2 '{}'".format(noun)

#verb_dict={"say":say,"say2":say2}
verb_dict={"say":say}
print("hello")
print_test()
