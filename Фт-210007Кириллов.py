import logging

def input_int(
    msg: str, 
    min: int = None, 
    max: int = None,
) -> int:
    '''
    Берет на ввод у пользователя число с дальнейшей проверкой.
    Параметры:
    msg - Сообщение подающееся на ввод пользователю.
    min - Минимальное значение на ввод.
    max - Максимальное значение на ввод.
    Возврат:
    Корректно введенное число.
    '''
    while True:
        try:
            logging.info(msg)
            num = int(input(msg))
            logging.info('Пользователь ввел: ' + str(num))
            if min != None and num < min or max != None and num > max:
                min_msg = '' if min == None else f' от {min}'
                max_msg = '' if max == None else f' до {max}'
                print(f'Ошибка: нужно ввести число{min_msg}{max_msg}!')
                logging.error(f'Ошибка: нужно ввести число{min_msg}{max_msg}!')
                continue
            logging.info('Корректное значение введенное пользователем: ' + str(num))
            return num
        except:
            logging.error('Ошибка: нужно ввести число!', exc_info=True)
            print('Ошибка: нужно ввести число!')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="logfile.log", filemode="a",
                            format="%(asctime)s %(levelname)s %(message)s")

    number = input_int("Введите сумму: ")

    cups = [64, 32, 16, 8, 4, 2, 1]
    
    #Пустой массив для счета кол-ва купюр
    count_cups = [0 for i in range (0,7)]
    
    #Вычитаем и считаем максимальное выгодное количество купюр
    while number:
        for i in range (0,7):
            if number - cups[i] >= 0: 
                number -= cups[i]
                count_cups[i] += 1
                break
    
    #Выводим кол-во купюр начиная с максимально затрачиваемых
    for i in range (0,7):
        if count_cups[i]:
            print(f"Купюр {cups[i]} для оплаты суммы:", count_cups[i])
            logging.info(f"Купюр {cups[i]} для оплаты суммы:" + str(count_cups[i]))