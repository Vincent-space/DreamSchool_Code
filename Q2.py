def Q2():
    while True:
        string = input()
        print(string)
        print(bracket_match(string))


def bracket_match(string):
    st = []
    res = [' '] * len(string)
    for i, c in enumerate(string):
        if c not in ('(', ')'):
            continue
        if c == '(':
            st.append(i)
            res[i] = 'x'
        elif c == ')':
            if not st:
                res[i] = '?'
            else:
                res[st.pop()] = ' '
    return ''.join(res)

if __name__ == '__main__':
    Q2()
