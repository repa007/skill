from nis import match
from flask import Flask, request, jsonify
from random import randint
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/privet', methods = ['POST'])
def main():
    content = request.json
    status = '200 OK'
    #output = b'Hello World!\n'

    com = content["request"]["command"]
    if (com.find("поздравлялка") != -1):
        def one():
            def sayHello():
                response = {}
                response["version"] = content["version"]
                response["session"] = content["session"]
                response["response"] = {"end_session" : False}

                response["response"]["text"] = "Выберите праздник. новый год или день рождения"
                response["response"]["tts"] = "Что празднуем?... ( скажите....... новый год...... или.... скажите день рождения)"

                response["response"]["buttons"] = [{"title": "Новый год"}, {"title": "День рождения"}]
                #response["response"]["Placeholder"] = {"title": "тайтл","button": { "action": {"type": "open_url", "url": "https://dev.vk.com/marusia/api"}}}
                response["response"]["end_session"] = False
                return response
            response = sayHello()
            return response
            #######################################################################
        response = one()
        return response
    elif (com == "новый год"):
        def new_year():
            def sayHello():
                response = {}
                response["version"] = content["version"]
                response["session"] = content["session"]
                response["response"] = {"end_session" : False}
                response["response"]["buttons"] = [{"title": "Новый год"}, {"title": "День рождения"}]
                response["response"]["text"] = generate_new_year(response)
                response["response"]["end_session"] = False
                return response
            response = sayHello()
            return response
            #######################################################################
        response = new_year()
        return response
    elif (com == "день рождения"):
        def birthday():
            def sayHello():
                response = {}
                response["version"] = content["version"]
                response["session"] = content["session"]
                response["response"] = {"end_session" : False}
                response["response"]["buttons"] = [{"title": "Новый год"}, {"title": "День рождения"}]
                response["response"]["text"] = generate_birthday(response)
                response["response"]["end_session"] = False
                return response
            response = sayHello()
            return response
            #######################################################################
        response = birthday()
        return response
    else:
        response = {}
        response["version"] = content["version"]
        response["session"] = content["session"]
        response["response"] = {"end_session" : False}
        response["response"]["text"] = "Выход из навыка"
        response["response"]["end_session"] = True
    return response

############----------------------###########
############-----FOR NEW YEAR-----###########
############----------------------###########
def generate_new_year(response):
    random_number = randint(1,10)
    if random_number == 1:
        congratulation = col_1()
    if random_number == 2:
        congratulation = col_2(response)
    if random_number == 3:
        congratulation = col_3()
    if random_number == 4:
        congratulation = col_4()
    if random_number == 5:
        congratulation = col_5()
    if random_number == 6:
        congratulation = col_6()
    if random_number == 7:
        congratulation = col_7()
    if random_number == 8:
        congratulation = col_8()
    if random_number == 9:
        congratulation = col_9()
    if random_number == 10:
        congratulation = col_10()

    return congratulation

def col_1():
    text = "Коллеги, в преддверие Нового года хочу пожелать вам сказочных зарплат, волшебных условий работы и начальников, которые всегда будут в чудесном расположении духа! Пусть ваш опыт и знания станут ценнее любых богатств. Но если кто-то задумает их приобрести — торгуйтесь до последнего!"

def col_2(response):
    text = "C НГ!"
    response["response"]["text"] = "С эн гэ!"
    return text

def col_3():
    text = "Дамы и господа, прошу вас провести новый год в середине промежутка от скуки до весёлой госпитализации!"
    return text

def col_4():
    text = "Здорового счастья и счастливого здоровья!"
    return text

def col_5():
    text = """Что общего между "новым годом" и "айтишником"? Строковый тип данных. А да, всё поздравление я закомментировала. Сори."""
    return text

def col_6():
    text = "Поздравление украла бабайка"
    return text

def col_7():
    text = "Я желаю в НОВЫЙ ГОД, Винно-Водочный Завод,\nМятых Баксов 2 вагона,\nНаших денег 3 Лимона!\nОтпуск месяцев на 10-за бугром покуралесить!\nЯхту, Лексус Новый Марки, Бриллиантов целый воз!"
    return text

def col_8():
    text = "Вы - самая лучшая команда по водному поло, с которой мне когда-либо довелось работать!"
    return text

def col_9():
    text = "Шоб вам в новый год было так же хорошо, как коту на ёлке!"
    return text

def col_10():
    text = "Неудержим времени ход. Так пусть он несёт в следующий год!"

    return text


###########----------------------###########
###########-----FOR BIRTHDAY-----###########
###########----------------------###########

def generate_birthday(com):
    random_number = randint(1,10)
    if random_number == 1:
        congratulation = ina_1()
    if random_number == 2:
        congratulation = ina_2()
    if random_number == 3:
        congratulation = ina_3()
    if random_number == 4:
        congratulation = ina_4()
    if random_number == 5:
        congratulation = ina_5()
    if random_number == 6:
        congratulation = ina_6()
    if random_number == 7:
        congratulation = ina_7()
    if random_number == 8:
        congratulation = ina_8()
    if random_number == 9:
        congratulation = ina_9()
    if random_number == 10:
        congratulation = ina_10()

    return congratulation

def ina_1():
    text = "С международным днём... тебя"
    return text
def ina_2():
    text = "Вот и старше стал на год,\nСтарость скоро подойдет.\nОчень скоро растолстеешь,\nПоседеешь, полысеешь.\nС днем рожденья поздравляю,\nВ жизни всё успеть желаю.\nПусть года хоть и идут,\nТебе счастье лишь несут!"
    return text
def ina_3():
    text = "Скайнет поздравляет вас с тем, что вы живы. Не волнуйтесь, мы работаем над этим."
    return text
def ina_4():
    text = "Поздравление украла бабайка."
    return text
def ina_5():
    text = "Achievement unlocked: Multiple Survivor"
    return text
def ina_6():
    text = "С праздничком! И пусть препятствия на твоём пути рухнут быстрее твоей сомооценки"
    return text
def ina_7():
    text = "В году примерно триста шесьдесят пять дней. Сегодня твой. Вот. Тебя это должно радовать. Меня радует."
    return text
def ina_8():
    text = "Вам посылочка. Поздравление. Получите и распишитесь."
    return text
def ina_9():
    text = "С ДР!"
    return text
def ina_10():
    text = "С днём варенья, ягодка моя!"
    return text





