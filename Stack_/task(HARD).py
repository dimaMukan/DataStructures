def balance_check(s):
    if len(s) % 2 != 0:
        return False

    opening = set('([{')
    matches = set([
        ('(',')'),
        ('[',']'),
        ('{','}')
    ])

    stack = []

    for parent in s:
        if parent in opening:
            stack.append(parent)

        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open,parent) not in matches:
                return False

    return len(stack) == 0






print(balance_check('[]'))
print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){[}]'))

