import urwid
import logging

logger = logging.getLogger(__name__)


def is_very_long(password):
    """Проверка, что символов минимум 12"""
    return len(password) >= 12


def has_digit(password):
    """True - в пароле есть цифры"""
    return any(symbol.isdigit() for symbol in password)


def has_letters(password):
    """True - в пароле есть хотя бы 1 буква"""
    return any(symbol.isalpha() for symbol in password)


def has_upper_letters(password):
    """True - в пароле есть заглавные буквы"""
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    """True - в пароле есть строчные буквы"""
    return any(symbol.islower() for symbol in password)


def has_symbols(password):
    return any(not symbol.isalpha() and not symbol.isdigit() for symbol in
               password)


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        filename='main.log',
        filemode='w',
        format='%(asctime)s %(levelname)s %(message)s'
    )
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
                logging.debug(f'Сработала проверка: {func.__name__}')
                logging.info(f'Получено + 2 балла')
        logging.debug(f'Итого: {score} балла')
        reply.set_text("Рейтинг этого пароля: %s" % score)

    password = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text(u"")
    menu = urwid.Pile([password, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(password, 'change', on_ask_change)
    urwid.MainLoop(menu).run()

if __name__ == "__main__":
    main()

