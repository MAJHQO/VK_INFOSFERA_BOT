import vk_api as vk_api
from vk_api.bot_longpoll import VkBotEventType,VkBotLongPoll,VkBotMessageEvent,VkBotEvent
from vk_api.keyboard import VkKeyboard,VkKeyboardButton,VkKeyboardColor
from vk_api.upload import VkUpload
from vk_api.requests_pool import VkRequestsPool,RequestResult
import datetime
import json
from multipledispatch import dispatch


# state_scenary['state']=state
#     with open(pathFile,'w+') as file:
#         file.write(json.dumps(state_scenary))


# check=session.method('messages.getLongPollServer',{'need_pts':1,'group_id':events.group_id,'lp_version':3})
# long=session.method('messages.getLongPollHistory',{'ts':check['ts'], 'group_id': events.group_id,'preview_length':0})


group_id='221557455'

state_scenary={'state':''}


user={'user_id':' ',
        'peer_id':' ',
        'state':' ',
        'permission':' '
        }


userInfo_val={
    'group_id':group_id,
    'user_id':[]
    }


def getUserId(userID:int):
    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                return file_user


def writeInFile(state:str,userID:int):
    """
    pathFile: полный путь до файла или его название, если он находится в каталоге проекта
    state: название сценария, в котором вы находитесь
    """

    # if events.type==VkBotEventType.MESSAGE_NEW:
    #     user_id=events.message['from_id']
    # else:
    #     user_id=events.object['user_id']

    with open('userInfo.json','r') as file:
        dataUser = json.load(file)
        
    user['user_id']=userID
    user['peer_id']=userID
    user['state']=state
    user['permission']='user'

    with open('userInfo.json','w') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                dataUser['user_id'][file_user]=user
                break
            else:
                continue
        file.write(json.dumps(dataUser))



def writeInFile_start(user_id,peer_id,permission):
    """
    permission: права доступа к боту
    """

    user['user_id']=user_id
    user['peer_id']=peer_id
    user['state']='start'
    user['permission']=permission
    
    userInfo_val['user_id'].append(user)
    with open('userInfo.json','w+') as file:
        file.write(json.dumps(userInfo_val))




def sPrintLog(event:VkBotMessageEvent, save:bool, pathFile:str):
    """
    message: проверка на событие прихода сообщения
    obj: проверка на события нажатия кнопки и т.д
    pathFile: полный путь до файла или его название (для сохранения), если он находится в каталоге проекта
    save: (True) - выводит в консоли и сохраняет логи в файл, (False) - выводит логи в консоль
    """

    with open('userInfo.json','r') as file:
        dataUser_r = json.load(file)


    if event.type==VkBotEventType.MESSAGE_TYPING_STATE:
        userIndex=getUserId(event.object["from_id"])
    elif event.type== VkBotEventType.MESSAGE_NEW:
        userIndex=getUserId(event.message["from_id"])
    elif event.type==VkBotEventType.MESSAGE_REPLY:
        userIndex=getUserId(event.object["peer_id"])
    elif event.type==VkBotEventType.MESSAGE_EVENT:
        userIndex=getUserId(event.object["user_id"])

    if event.type==VkBotEventType.MESSAGE_NEW:
        print(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.message["from_id"]} | Scenary: {dataUser_r["user_id"][userIndex]["state"]} | Event: {event.type} | Text: {event.message["text"]}')
    elif event.type==VkBotEventType.MESSAGE_EVENT:
        print(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.object["user_id"]} | Scenary: {dataUser_r["user_id"][userIndex]["state"]} | Event: {event.type} | Payload: {event.object["payload"]}')

    if (save):
        with open(pathFile,'a',encoding='utf-8') as file:
            if event.type==VkBotEventType.MESSAGE_NEW:
                file.writelines(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.message["from_id"]} | Scenary: {dataUser_r["user_id"][userIndex]["state"]} | Event: {event.type} | Text: {event.message["text"]}\n')
            elif event.type==VkBotEventType.MESSAGE_EVENT:
                file.writelines(f'[LOG] [{datetime.datetime.now()}]: UserID: {event.object["user_id"]} | Scenary: {dataUser_r["user_id"][userIndex]["state"]} | Event: {event.type} | Payload: {event.object["payload"]}\n')



#Инициализация сессии бота при помощи токена
session=vk_api.VkApi(token='vk1.a.HeKyjLADslNJB6qFgDRwKmWPJqbgRAYgH6U0-mvObCHOBmdl392qrE8QdC2e0zAkN_tlJc'
                           '-CM2Skq5jMckEnaoXeTIfyUa1qAWF7dzU4dH44gaj6CKTbj4Zc251F7i5h805K93Uc3Ti1odVdaZ3uRtodtDV'
                           '-BSTRoG5kMrdXMzJkJ3OJPQZGSpkC3Qi62jxmV3SNJ6O-nV6PcbqI9dHbvg')
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


payload_arrStart=['directions','faq']
payload_arrDirection=['Preparatory','Baytick','IfoWorlds','InfoStart','start']
payload_arrFaq=['next','back']


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

keyboard_continue=VkKeyboard()
keyboard_continue.add_button('Продолжить',VkKeyboardColor.SECONDARY,['continue'])