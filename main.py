import urwid

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
    return any(char in ".,:;!_*-+()/#¤%&@[]{}#$%^^&*-_=)" for char in password)


def main():
    def on_ask_change(edit, password):
        score = 0
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
                score += 2
        score += 0
        reply.set_text("Рейтинг этого пароля: %s" % score)

    password = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text(u"")
    menu = urwid.Pile([password, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(password, 'change', on_ask_change)
    urwid.MainLoop(menu).run()


if __name__ == "__main__":
    """Отправная точка программы"""
    main()
