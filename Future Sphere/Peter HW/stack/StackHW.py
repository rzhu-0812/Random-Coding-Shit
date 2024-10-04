class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.empty():
            return self.items[-1]
        else:
            print("No items in stack")
    
    def push(self, a):
        self.items.append(a)
    
    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            print("No items in stack")

def question_1(string):
    stack = Stack()
    temp_str = []

    for char in string:
        stack.push(char)
    
    for _ in range(len(string)):
        temp_str.append(stack.pop())
    
    return "".join(temp_str)

def question_2(exp):
    temp = Stack()

    bracket_pairs = {"(": ")", "{": "}", "[": "]"}

    for char in exp:
        if char in bracket_pairs.keys():
            temp.push(char)
        elif char in bracket_pairs.values():
            if temp.empty() or bracket_pairs[temp.pop()] != char:
                return "Not Balanced"

    return "Balanced"

print(question_1("GeeksQuiz"))
print(question_1("abc"))

print(question_2("[()]{}{[()()]()}"))
print(question_2("[(])"))
        

