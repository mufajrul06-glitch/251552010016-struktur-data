def cek_bracket (ekspresi) :
    stack = []
    
    pasangan = {')' : '(', '}' : '{', ']' : '['}

    for char in ekspresi : 
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            if stack[-1] != pasangan[char]:
                return False
            stack.pop()

    return len(stack) == 0

print(cek_bracket('(())')) 
print(cek_bracket('{[()]}')) 
print(cek_bracket('([)]'))
print(cek_bracket('{[}'))