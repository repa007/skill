import json

request = """{
"meta":{
"client_id":"MailRu-VC/1.0"
"locale":"ru_RU"
"timezone":"Europe/Moscow"
"interfaces":{}
"_city_ru":"Москва"
}
"request":{
"command":"ти"
"original_utterance":"ти"
"type":"SimpleUtterance"
"nlu":{
"tokens":[
0:"ти"
]
"entities":[]
}
}
"session":{
"session_id":"982839da-4c6c-4648-8d75-776f3e9111c2"
"user_id":"5a1c1db4dbf41e81c202ea7c5e589e57255aa1840c378125eddb7d48aec3c474"
"skill_id":"52401ef1-935a-49ef-bd57-1f3f83ac3447"
"new":true
"message_id":0
"application":{
"application_id":"5a1c1db4dbf41e81c202ea7c5e589e57255aa1840c378125eddb7d48aec3c474"
"application_type":"mail"
}
"auth_token":"636d5f7d6fb18e1aff48bb161ab82de12012fec213a0bf2e9a9efd8b7825c69c"
}
"state":{
"session":{}
"user":{}
}
"version":"1.0"
}"""

content = request.json
status = '200 OK'
#output = b'Hello World!\n'

def sayHello():
    response = {}
    response["version"] = content["version"]
    response["session"] = content["session"]
    response["response"] = {"end_session" : False}
        #response["response"]["text"] = "Что празднуем?"
        #response["response"]["tts"] = "По чём кипиш?"

    response["response"]["text"] = "Кого поздравляем?"
    response["response"]["tts"] = "В честь кого движ?"


    

    response["response"]["end_session"] = True
    print(pesponse)
    return response
sayHello()
response = sayHello()