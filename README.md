ВАЖНО: лучше запускать потссылке через Chromе, тк через
яндекс он почему-то жалуется на item/1, а в хроме нет

1 фиксация (забыл добавить описание )):
27.08.24-28.08.2024

разработал модель, представление, скрипт на открытие платежа для item/1 поправить надо для любого item, также прописал urls'ы и проверил работу, вывод все четко, осталось подредачить и основная часть выполнена


2 фиксация:
28.08.2024 15:48

поправил html страницу, поправил вьюшку и теперь на каждый айтем идет свой айдишник сессии


3 фиксация:
28.08.2024 - 29.08.2024

полностью сделал основное задание, реализовал начальное окно, исправил ошибки которые возникали, также добавил контейнеры docker и настроил виртуальное окружение .env, добавил в models.py модели Order и OrderItem они нужны чтобы в модели Order была информация о заказе, а промежуточная модель OrderItem будет связывать конкретные item с заказом


4 фиксация:
30.08.2024:

добавлены новые модели Order, Discount, Tax, также добавлено поле валюты в модели item и реализован Stripe Payment Intent, из пробелм почему то не видит обращение к другим переменным из других классов, почему я не смог разобраться, супер много времени ушло, а результат один и тот же, в приципе думаю, что задание я сделал насколько смог, главное, что смог реализовать основные задачи и увидел как работать с платежной системой, полезный навык я считаю, надеюсь, что мои рассуждения и мысли понравятся и я смогу узнать как мне исправить свои моменты и стать лучше, чем сейчас, на самом деле очень интересное тестовое, оно явно отличается от всех тех, которые я проходил, верим в лучшее
