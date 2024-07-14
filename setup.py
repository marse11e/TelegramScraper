import os
import configparser


def install_requirements():
    print("Требования к установке ...")
    os.system('python3 -m pip install telethon')
    os.system('pip3 install telethon')


def setup_config():
    cpass = configparser.RawConfigParser()
    cpass.add_section('account')

    xid = input("Введите идентификатор API: ")
    cpass.set('account', 'id', xid)

    xhash = input("Введите хэш API: ")
    cpass.set('account', 'hash', xhash)

    xphone = input("Введите номер телефона: ")
    cpass.set('account', 'phone', xphone)

    with open('config.ini', 'w') as setup_file:
        cpass.write(setup_file)

    print("Настройка завершена!")


def main():
    # Установка необходимых зависимостей.
    install_requirements()
    # Настройка конфигурационного файла.
    setup_config()


if __name__ == "__main__":
    main()
