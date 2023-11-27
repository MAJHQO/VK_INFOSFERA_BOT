import vk_api as vk_api
from vk_api.bot_longpoll import VkBotEventType,VkBotLongPoll,VkBotMessageEvent,VkBotEvent
from vk_api.keyboard import VkKeyboard,VkKeyboardButton,VkKeyboardColor
from vk_api.upload import VkUpload
from vk_api.requests_pool import VkRequestsPool,RequestResult
import datetime
import json
from multipledispatch import dispatch

group_id='221557455'

userInfo_val={
    'group_id':group_id,
    'user_id':[

    ]
    }
@dispatch(str,object)
def writeInFile(state:str,events:VkBotMessageEvent):
    """
    pathFile: полный путь до файла или его название, если он находится в каталоге проекта
    state: название сценария, в котором вы находитесь
    """
    
    # check=session.method('messages.getLongPollServer',{'need_pts':1,'group_id':events.group_id,'lp_version':3})
    # long=session.method('messages.getLongPollHistory',{'ts':check['ts'], 'group_id': events.group_id,'preview_length':0})

    if events.type==VkBotEventType.MESSAGE_NEW:
        user_id=events.message['from_id']
    else:
        user_id=events.object['user_id']
        
    with open('userInfo.json','w+') as file:
        dataUser = json.load(file)


        for user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][user]['user_id']==user_id):
                dataUser['user_id'][user]['state']=state
        file.write(json.dumps(dataUser['user_id']))
    # with open('userInfo.json','w+') as file:
    #     dataUser = json.load(file)
    #     dataUser['user_id'][0]['state']='OLOLO'
    #     file.write=json.load(dataUser)

@dispatch (int,int,str)
def writeInFile(user_id,peer_id,permission):
    """
    permission: права доступа к боту
    """
    
    userInfo_val['user_id'].append({
        'user_id':user_id,
        'peer_id':peer_id,
        'state':'start',
        'permission':permission
        })
    with open('userInfo.json','w+') as file:
        file.write(json.dumps(userInfo_val))


def readFile(pathFile:str,events:VkBotMessageEvent):
    """
    pathFile: полный путь до файла или его название, если он находится в каталоге проекта
    """
    
    check=session.method('messages.getLongPollServer',{'need_pts':1,'group_id':events.group_id,'lp_version':3})
    long=session.method('messages.getLongPollHistory',{'ts':check['ts'], 'group_id': events.group_id,'preview_length':0})

    if long('messages')('count')>0:
        user_id=long('messages')('items')[0]('from_id')
        with open(pathFile, 'r') as file:
            dataLog = json.load(userInfo_val['user_id'])
            for user in range(len (dataLog)):
                    if (dataLog[user]['user_id']==user_id):
                        first_key = dataLog[user]['user_id']['state']
                    
    return first_key

# def sPrintLog(event:VkBotMessageEvent, save:bool,pathFile:str):
#     """
#     message: проверка на событие прихода сообщения
#     obj: проверка на события нажатия кнопки и т.д
#     pathFile: полный путь до файла или его название (для сохранения), если он находится в каталоге проекта
#     save: (True) - выводит в консоли и сохраняет логи в файл, (False) - выводит логи в консоль
#     """

#     # if event.type==VkBotEventType.MESSAGE_NEW:
#     #     print(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.message["from_id"]} | Scenary: {userInfo_val["state"]} | Event: {event.type} | Text: {event.message["text"]}')
#     # elif event.type==VkBotEventType.MESSAGE_EVENT:
#     #     print(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.object["user_id"]} | Scenary: {userInfo_val["state"]} | Event: {event.type} | Payload: {event.object["payload"]}')
#     # elif event.type==VkBotEventType.MESSAGE_REPLY:
#     #     print(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.message["from_id"]} | Scenary: {state_scenary["state"]} | Event: {event.type}')

#     if (save):
#         with open(pathFile,'a',encoding='utf-8') as file:
#             if event.type==VkBotEventType.MESSAGE_NEW:
#                 file.writelines(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.message["from_id"]} | Scenary: {userInfo_val["state"]} | Event: {event.type} | Text: {event.message["text"]}\n')
#             elif event.type==VkBotEventType.MESSAGE_EVENT:
#                 file.writelines(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.object["user_id"]} | Scenary: {userInfo_val["state"]} | Event: {event.type} | Payload: {event.object["payload"]}\n')
#             # elif event.type==VkBotEventType.MESSAGE_REPLY:
#             #     file.writelines(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.object["user_id"]} | Scenary: {state_scenary["state"]} | Event: {event.type}')



#Инициализация сессии бота при помощи токена
session=vk_api.VkApi(token='vk1.a.HeKyjLADslNJB6qFgDRwKmWPJqbgRAYgH6U0-mvObCHOBmdl392qrE8QdC2e0zAkN_tlJc-CM2Skq5jMckEnaoXeTIfyUa1qAWF7dzU4dH44gaj6CKTbj4Zc251F7i5h805K93Uc3Ti1odVdaZ3uRtodtDV-BSTRoG5kMrdXMzJkJ3OJPQZGSpkC3Qi62jxmV3SNJ6O-nV6PcbqI9dHbvg')
#Создание объекта, для обработки событий от сервера
bot_longpoll=VkBotLongPoll(session,'221557455',25)
#Объект клавиатуры, сценария "Старт"
keyboard_start=VkKeyboard() #Callback_button - для перехода между сценариями; usual_button - для взаимодействия внутри данного сценария
#Объект для составления и обработки запросов
request_pool_api=VkRequestsPool(session)
#Объект, характеризующий результат запроса
pool_result=RequestResult()
#Объект для загрузки различных данных
upload=VkUpload(session)



keyboard_start.add_callback_button('О направлениях',VkKeyboardColor.PRIMARY,['directions'])
keyboard_start.add_line()
keyboard_start.add_openlink_button('Записаться','https://nn.isphera.ru/#form')
keyboard_start.add_line()
keyboard_start.add_callback_button ("Часто задаваемые вопросы",VkKeyboardColor.SECONDARY,['faq'])


keyboard_directions=VkKeyboard()

keyboard_directions.add_button("Подготовительная (1 класс)",VkKeyboardColor.PRIMARY,['Preparatory'])
keyboard_directions.add_line()
keyboard_directions.add_button("Байтик (2 класс)",VkKeyboardColor.PRIMARY,['Baytick'])
keyboard_directions.add_button("Инфомиры (3-4 класс)",VkKeyboardColor.PRIMARY,['IfoWorlds'])
keyboard_directions.add_line()
keyboard_directions.add_button("Инфостарт (5-7 класс)",VkKeyboardColor.PRIMARY,['InfoStart'])
keyboard_directions.add_line()
keyboard_directions.add_callback_button("Вернуться",VkKeyboardColor.NEGATIVE,['start'])

keyboard_faq=VkKeyboard()

keyboard_faq.add_callback_button('Вперед',VkKeyboardColor.PRIMARY,['next'])
keyboard_faq.add_callback_button('Назад',VkKeyboardColor.SECONDARY,['back'])
keyboard_faq.add_line()
keyboard_faq.add_callback_button('Вернуться',VkKeyboardColor.NEGATIVE,['start'])