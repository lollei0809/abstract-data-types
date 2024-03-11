from stack2 import Stack
def validate(plist):
    stack3 = Stack()
    for item in plist:
        if item == "(":
            stack3.Push(item)
        elif item == ")":
            if stack3.isEmpty():
                valid = False
            else:
                stack3.Pop()
    if stack3.isEmpty():
        valid = True
    return valid

string = input("string: ")
strlist = list(string)
print(validate(strlist))

