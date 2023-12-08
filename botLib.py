import vk_api as vk_api
from vk_api.bot_longpoll import VkBotEventType,VkBotLongPoll,VkBotMessageEvent,VkBotEvent
from vk_api.keyboard import VkKeyboard,VkKeyboardButton,VkKeyboardColor
from vk_api.upload import VkUpload
from vk_api.requests_pool import VkRequestsPool,RequestResult
import datetime
import json
from multipledispatch import dispatch


# 'vk1.a.HeKyjLADslNJB6qFgDRwKmWPJqbgRAYgH6U0-mvObCHOBmdl392qrE8QdC2e0zAkN_tlJc'
#                            '-CM2Skq5jMckEnaoXeTIfyUa1qAWF7dzU4dH44gaj6CKTbj4Zc251F7i5h805K93Uc3Ti1odVdaZ3uRtodtDV'
#                            '-BSTRoG5kMrdXMzJkJ3OJPQZGSpkC3Qi62jxmV3SNJ6O-nV6PcbqI9dHbvg'


#Инициализация сессии бота при помощи токена
session=vk_api.VkApi(token='vk1.a.UaXHv3-PnEII6XPvDq6QUS-2J1Kn_iiCFkPHHztbtFH_QUkfzo3cnhiDbZwNqOZrrDkcx44LxzWNzIP8yhcFPv4xCqZfUJpt7BELAZrZMJRupyoMUC0ffiT0L6mPzpdd9eZsNoPBNxVIYuvGJNiiNBkHdiAMX0hqg2k7WMdMa1BCilhbV7IjaoFG9UIzflwBQk0gG5VRc2h587tnc3sqtw')
#Создание объекта, для обработки событий от сервера
bot_longpoll=VkBotLongPoll(session,'221557455',25)



# state_scenary['state']=state
#     with open(pathFile,'w+') as file:
#         file.write(json.dumps(state_scenary))


# check=session.method('messages.getLongPollServer',{'need_pts':1,'group_id':events.group_id,'lp_version':3})
# long=session.method('messages.getLongPollHistory',{'ts':check['ts'], 'group_id': events.group_id,'preview_length':0})


group_id='221557455'

state_scenary={'state':''}


user={'user_id':'',
        'peer_id':'',
        'state':'',
        'ban':'',
        'permission':''
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
            


def banUser(userID:int):
    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                dataUser['user_id'][file_user]['ban']=True
    
    with open ('userInfo.json','w') as file:
        file.write(json.dumps(dataUser))
        print(f'[LOG] [{datetime.datetime.now()}] User: {userID} was ban')



def unBanUser(userID:int):
    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                dataUser['user_id'][file_user]['ban']=False
    
    with open ('userInfo.json','w') as file:
        file.write(json.dumps(dataUser))
        print(f'[LOG] [{datetime.datetime.now()}] User: {userID} was unban')

                   

def checkUserOnBan(userID:int):
    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                if dataUser['user_id'][file_user]['ban']==True:
                    return True
                else:
                    return False
            


def getUserPermission(userID:int):
    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                return dataUser['user_id'][file_user]['permission']
            


def getUserState(userID:int):
    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                return dataUser['user_id'][file_user]['state']



def setUserPermission(userID:int,permission:str):
    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    with open('userInfo.json','r') as file:
        for file_user in range(0,len (dataUser['user_id'])):
            if (dataUser['user_id'][file_user]['user_id']==userID):
                dataUser['user_id'][file_user]['permission']=permission
    
    with open ('userInfo.json','w') as file:
        file.write(json.dumps(dataUser))
        print(f'[LOG] [{datetime.datetime.now()}] User: {userID} was change permission on [{permission}]')



def writeInFile(state:str,userID:int):
    """
    userID: id пользователя
    state: название сценария, в котором вы находитесь
    """

    with open('userInfo.json','r') as file:
        dataUser = json.load(file)
        
    if userID==170852963:
        user['user_id']=userID
        user['peer_id']=userID
        user['state']='start'
        user['ban']=False
        user['permission']='admin'
    
    else:
        user['user_id']=userID
        user['peer_id']=userID
        user['state']='start'
        user['ban']=False
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

    with open('userInfo.json','r') as file:
        dataUser = json.load(file)

    if user_id==170852963:
        user['user_id']=user_id
        user['peer_id']=peer_id
        user['state']='start'
        user['ban']=False
        user['permission']='admin'
    
    else:
        user['user_id']=user_id
        user['peer_id']=peer_id
        user['state']='start'
        user['ban']=False
        user['permission']=permission
    
    dataUser['user_id'].append(user)
    with open('userInfo.json','w+') as file:
        file.write(json.dumps(dataUser))



def sPrintLog(event:VkBotMessageEvent, save:bool, pathFile:str):
    """
    message: проверка на событие прихода сообщения\n
    obj: проверка на события нажатия кнопки и т.д\n
    pathFile: полный путь до файла или его название (для сохранения), если он находится в каталоге проекта\n
    save: (True) - выводит в консоли и сохраняет логи в файл, (False) - выводит логи в консоль
    """

    check=session.method('messages.getLongPollServer',{'need_pts':1,'group_id':event.group_id,'lp_version':3})
    long=session.method('messages.getLongPollHistory',{'ts':check['ts'], 'group_id': event.group_id,'preview_length':0})

    if (long['messages']['count']>0):
        pass

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



#Объект клавиатуры, сценария "Старт"
keyboard_start=VkKeyboard() #Callback_button - для перехода между сценариями; usual_button - для взаимодействия внутри данного сценария
#Объект для составления и обработки запросов
request_pool_api=VkRequestsPool(session)
#Объект, характеризующий результат запроса
pool_result=RequestResult()
#Объект для загрузки различных данных
upload=VkUpload(session)


payload_arrStart=['directions','faq']
payload_arrDirection=['Подготовительная (1 класс)','Байтик (2 класс)','Инфомиры (3-4 класс)','Инфостарт (5-7 класс)']
payload_arrFaq=['next','back','minAge','itemForSc','computer','attendance','schedule','secShift','testing','testing','taxDeduction','MotherCaptl','anotherQuest']


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
keyboard_faq_2=VkKeyboard()


keyboard_faq.add_callback_button('Минимальный возраст',VkKeyboardColor.SECONDARY,['minAge'])
keyboard_faq.add_callback_button('Что необходимо для учебы?',VkKeyboardColor.SECONDARY,['itemForSc'])
keyboard_faq.add_line()
keyboard_faq.add_callback_button('Нужен ли дома компьютер?',VkKeyboardColor.SECONDARY,['computer'])
keyboard_faq.add_callback_button('Сколько занятий в неделю?',VkKeyboardColor.SECONDARY,['attendance'])
keyboard_faq.add_line()
keyboard_faq.add_callback_button('Подойдет ли нам расписание?',VkKeyboardColor.SECONDARY,['schedule'])
keyboard_faq.add_callback_button('Ребенок учиться во вторую смену',VkKeyboardColor.SECONDARY,['secShift'])
keyboard_faq.add_line()
keyboard_faq.add_callback_button('Главная',VkKeyboardColor.PRIMARY,['start'])
keyboard_faq.add_callback_button('Следующие',VkKeyboardColor.NEGATIVE,['next'])

keyboard_faq_2.add_callback_button('Что такое тестирование?',VkKeyboardColor.SECONDARY,['testing'])
keyboard_faq_2.add_callback_button('Налоговый вычет по нашему договору',VkKeyboardColor.SECONDARY,['taxDeduction'])
keyboard_faq_2.add_line()
keyboard_faq_2.add_callback_button('Оплата обучения за счет мат.капитала',VkKeyboardColor.SECONDARY,['MotherCaptl'])
keyboard_faq_2.add_callback_button('Другой вопрос',VkKeyboardColor.SECONDARY,['anotherQuest'])
keyboard_faq_2.add_line()
keyboard_faq_2.add_callback_button('Предыдущие',VkKeyboardColor.NEGATIVE,['back'])
