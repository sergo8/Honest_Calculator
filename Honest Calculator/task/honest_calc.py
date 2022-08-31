# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
memory = float(0)
continue_calc = True


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6

    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_7

    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_8

    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    if v.is_integer():
        if 10 > v > -10:
            return True
    else:
        return False


while continue_calc:
    result = 0

    print(msg_0)
    calc = tuple(input().split())
    x, oper, y = calc

    try:
        if x == 'M':
            if y == 'M':
                x = memory
                y = memory
            else:
                x = memory
        elif y == 'M':
            y = memory

        if oper in ['+', '-', '*', '/']:
            x_ = float(x)
            y_ = float(y)
            check(x_, y_, oper)
            if oper == '+':
                result = x_ + y_
            elif oper == '-':
                result = x_ - y_
            elif oper == '*':
                result = x_ * y_
            elif oper == '/':
                if y_ != 0:
                    result = x_ / y_
                else:
                    print(msg_3)
                    continue
            print(result)
        else:
            print(msg_2)
            continue

        while True:
            print(msg_4)
            store_result = input()
            if store_result == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(f'{msg_[msg_index]}')
                        one_digit = input()
                        if one_digit == 'y':
                            if msg_index < 12:
                                msg_index = msg_index + 1
                                continue
                            else:
                                memory = result
                                break
                        elif one_digit == 'n':
                            break
                        else:
                            continue
                    break
                else:
                    memory = result
                    break
            elif store_result == 'n':
                break
            else:
                continue
    except ValueError:
        print(msg_1)
    else:
        while True:
            print(msg_5)
            continue_ = input()
            if continue_ == 'y':
                break
            elif continue_ == 'n':
                continue_calc = False
                break
