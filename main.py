from flask import Flask, send_file
import random
import os
import requests 
app = Flask(__name__)

facts_list = [
    "Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
    "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
    "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.",
    "Согласно исследованию 2019 года, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после окончания рабочего дня.",
    "Один из способов борьбы с технологической зависимостью — поиск занятий, которые приносят удовольствие и улучшают настроение.",
    "Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, заставляя тратить как можно больше времени на просмотр контента.",
    "Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть осознаннее в их использовании."
]



@app.route("/")
def hello_world():
    return '<h1>Главная страница.Самый крутой сайт!</h1>' \
    '<a href="/random_fact">Посмотреть случайный факт!</a> <a href="/gen_pass/15">Сгенерировать пароль</a> <a href="/flip_coin">Поиграть в орел и решка</a> <a href="/random_mem">Рандомный мем</a>'

    
@app.route('/random_fact')
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'


@app.route("/gen_pass/<int:pass_length>")
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return f'<p>Сгенерированный пароль: {password}</p>'

@app.route("/flip_coin")
def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"



@app.route("/random_mem")
def mem():
    images = os.listdir('images')
    random_image = random.choice(images)
    image_path = os.path.join('images', random_image)
    return send_file(image_path, mimetype='image/jpeg')



app.run(debug=True)
