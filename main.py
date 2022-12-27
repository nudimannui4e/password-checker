import urwid


def test_pass():
    """Всякие проверки функций ниже"""
    print(has_digit("rnfUinginr"))  # False
    print(has_digit("rnvnreiv83282"))  # True
    print(is_very_long("onrv"))  # False
    print(is_very_long("ogvorneorenvoernb"))  # True
    print(has_upper_letters("rnfUinginr"))  # True
    print(has_letters("ewrewrw"))  # True
    print(has_letters("ewr321ewrw"))  # True
    print(has_letters("12341"))  # False
    print(has_upper_letters("GnoiIGIrg129"))  # True
    print(has_upper_letters("12971eorin29"))  # False
    print(has_symbols("onregn04"))  # False
    print(has_symbols("OVN#O2049)@$"))  # True
    print(has_symbols("sdaw43W@RR3}}"))


def is_very_long(password):
    """Проверка, что символов минимум 12"""
    return len(password) >= 12


def has_digit(password):
    """True - в пароле есть цифры"""
    found_digit = 0
    for symbol in password:
        if symbol.isdigit():
            found_digit += 1
    return found_digit > 0


def has_letters(password):
    """True - в пароле есть хотя бы 1 буква"""
    found_letter = 0
    for symbol in password:
        if symbol.isalpha():
            found_letter += 1
    return found_letter > 0


def has_upper_letters(password):
    """True - в пароле есть заглавные буквы"""
    found_upper = 0
    for symbol in password:
        if symbol.isupper():
            found_upper += 1
    return found_upper > 0


def has_lower_letters(password):
    """True - в пароле есть строчные буквы"""
    found_lower = 0
    for symbol in password:
        if symbol.islower():
            found_lower += 1
    return found_lower > 0


def has_symbols(password):
    symbols = '!@#$%^&*()_+=-ºª•¶§∞¢£™¡§±|"[]{}'
    found_symbols = 0
    for symbol in password:
        if symbol in symbols:
            found_symbols += 1
    return found_symbols > 0


def main():
    global score
    score = 0

    def on_ask_change(password, score):
        functions = [
            is_very_long,
            has_digit,
            has_letters,
            has_lower_letters,
            has_upper_letters,
            has_symbols,
        ]
        for func in functions:
            if func(password):
                print('1')
        reply.set_text("Оценка пароля: %s" % score)

    password = urwid.Edit('Password: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([password, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(password, 'change', on_ask_change)
    urwid.MainLoop(menu).run()


if __name__ == "__main__":
    """Отправная точка программы"""
    main()
