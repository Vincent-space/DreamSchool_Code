def Q1():
    while True:
        source = input()
        target = input()
        print(sequence(source,target))

def sequence(source, target):
    source_dict = {char: index for index, char in enumerate(source)}
    res = 0
    i = 0
    while i < len(target):
        cur_index = source_dict.get(target[i], -1)
        if cur_index == -1:
            return -1
        while cur_index < len(source):
            if i < len(target) and target[i] != source[cur_index]:
                i += 1
            cur_index += 1
        i += 1
        res += 1
    return res


if __name__ == '__main__':
   Q1()

