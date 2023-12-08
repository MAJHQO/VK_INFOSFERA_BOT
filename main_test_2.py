import vk_api as vk_api
import botLib
import data
import random
import json
import time

from vk_api.bot_longpoll import VkBotEventType,VkBotLongPoll,VkBotMessageEvent,VkBotEvent
from vk_api.requests_pool import VkRequestsPool,RequestResult



#Функция сценария "О направлениях"
def directions(event:VkBotMessageEvent):


    if botLib.checkUserOnBan(event)==True:
        pass

    else:

        if event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='directions':
            print('LAUNCH SCENARY: ', directions.__name__.upper())
            botLib.session.method('messages.send',{
                    'user_id': event.object['user_id'],
                    'random_id': random.randint(20,1000)+time.localtime().tm_sec,
                    'keyboard':botLib.keyboard_directions.get_keyboard(),
                    'attachment': 'photo-221557455_457239032',
                    'message':data.direction_messages_start})
        

        if event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Подготовительная (1 класс)':
            botLib.session.method('messages.send',
                {
                'user_id': event.message['from_id'],
                'random_id': random.randint(21,1000)+time.localtime().tm_sec,
                'attachment': 'photo-221557455_457239037',
                'message': data.direction_messages['Подготовительная']
                }
            )


        elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Байтик (2 класс)': 
            botLib.session.method('messages.send',
                {
                'user_id': event.message['from_id'],
                'random_id': random.randint(22,1000)+time.localtime().tm_sec,
                'attachment': 'photo-221557455_457239036',
                'message': data.direction_messages['Байтик']
                }
            )
            

        elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Инфомиры (3-4 класс)':
            botLib.session.method('messages.send',
                {
                'user_id': event.message['from_id'],
                'random_id': random.randint(23,1000)+time.localtime().tm_sec,
                'attachment': 'photo-221557455_457239035',
                'message': data.direction_messages['Инфомиры']
                }
            )


        elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Инфостарт (5-7 класс)':
            botLib.session.method('messages.send',
                {
                'user_id': event.message['from_id'],
                'random_id': random.randint(24,1000)+time.localtime().tm_sec,
                'attachment': 'photo-221557455_457239034',
                'message': data.direction_messages['Инфостарт']
                }
            )
            


def faq(event:VkBotMessageEvent):


    if botLib.checkUserOnBan(event)==True:
        pass

    else:
        print('LAUNCH SCENARY: ', faq.__name__.upper())
        if event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='faq':
            botLib.session.method('messages.send',{
                'user_id': event.object['user_id'],
                'random_id': random.randint(27,1000)+time.localtime().tm_sec,
                'keyboard': botLib.keyboard_faq.get_keyboard(),
                'message': 'Какой у вас вопрос? (1 страница)'
            })

        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='next':
             botLib.session.method('messages.sendMessageEventAnswer',
                {
                'event_id':event.object['event_id'],
                'user_id':event.object['user_id'],
                'peer_id':event.object['peer_id'],
                'event_data': json.dumps(
                                        botLib.session.method('messages.send',{
                                            'user_id': event.object['user_id'],
                                            'random_id': random.randint(28,1000)+time.localtime().tm_sec,
                                            'keyboard': botLib.keyboard_faq_2.get_keyboard(),
                                            'message': 'Какой у вас вопрос? (2 страница)'
                                        })
                )})


        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='back':
            botLib.session.method('messages.sendMessageEventAnswer',
                {
                'event_id':event.object['event_id'],
                'user_id':event.object['user_id'],
                'peer_id':event.object['peer_id'],
                'event_data': json.dumps(
                                        botLib.session.method('messages.send',{
                                            'user_id': event.object['user_id'],
                                            'random_id': random.randint(29,1000)+time.localtime().tm_sec,
                                            'keyboard': botLib.keyboard_faq.get_keyboard(),
                                            'message': 'Какой у вас вопрос? (1 страница)'
                                        })
                )})

        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='minAge':
            botLib.session.method('messages.sendMessageEventAnswer',
                {
                'event_id':event.object['event_id'],
                'user_id':event.object['user_id'],
                'peer_id':event.object['peer_id'],
                'event_data': json.dumps(botLib.session.method('messages.send',{
                                        'user_id': event.object['user_id'],
                                        'random_id': random.randint(30,1000)+time.localtime().tm_sec,
                                        'message': data.faq_message[0]
                                        })
                )})
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='itemForSc':
            botLib.session.method('messages.sendMessageEventAnswer',
                {
                'event_id':event.object['event_id'],
                'user_id':event.object['user_id'],
                'peer_id':event.object['peer_id'],
                'event_data': json.dumps(
                                        botLib.session.method('messages.send',{
                                            'user_id': event.object['user_id'],
                                            'random_id': random.randint(31,1000)+time.localtime().tm_sec,
                                            'message': data.faq_message[1]
                                        })
                )})
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='computer':
            botLib.session.method('messages.sendMessageEventAnswer',
                    {
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id'],
                    'event_data': json.dumps(
                                            botLib.session.method('messages.send',{
                                                'user_id': event.object['user_id'],
                                                'random_id': random.randint(32,1000)+time.localtime().tm_sec,
                                                'message': data.faq_message[2]
                                            })
                    )})
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='attendance':
            botLib.session.method('messages.sendMessageEventAnswer',
                    {
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id'],
                    'event_data': json.dumps(
                                            botLib.session.method('messages.send',{
                                                'user_id': event.object['user_id'],
                                                'random_id': random.randint(33,1000)+time.localtime().tm_sec,
                                                'message': data.faq_message[3]
                                            })
                    )})
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='schedule':
            botLib.session.method('messages.sendMessageEventAnswer',
                    {
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id'],
                    'event_data': json.dumps(
                                            botLib.session.method('messages.send',{
                                                'user_id': event.object['user_id'],
                                                'random_id': random.randint(34,1000)+time.localtime().tm_sec,
                                                'message': data.faq_message[4]
                                            })
                                        )})
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='secShift':
            botLib.session.method('messages.sendMessageEventAnswer',
                    {
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id'],
                    'event_data': json.dumps(
                                            botLib.session.method('messages.send',{
                                                'user_id': event.object['user_id'],
                                                'random_id': random.randint(35,1000)+time.localtime().tm_sec,
                                                'message': data.faq_message[5]
                                            })
                                        )})
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='testing':
            botLib.session.method('messages.sendMessageEventAnswer',
                    {
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id'],
                    'event_data': json.dumps(
                                            botLib.session.method('messages.send',{
                                                'user_id': event.object['user_id'],
                                                'random_id': random.randint(36,1000)+time.localtime().tm_sec,
                                                'message': data.faq_message[6]
                                            })
                                        )})
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='taxDeduction':
            botLib.session.method('messages.sendMessageEventAnswer',
                    {
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id'],
                    'event_data': json.dumps(
                                            botLib.session.method('messages.send',{
                                                'user_id': event.object['user_id'],
                                                'random_id': random.randint(37,1000)+time.localtime().tm_sec,
                                                'message': data.faq_message[7]
                                            })
                                        )})
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='anotherQuest':
            botLib.session.method('messages.sendMessageEventAnswer',
                    {
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id'],
                    'event_data': json.dumps(
                                            botLib.session.method('messages.send',{
                                                'user_id': event.object['user_id'],
                                                'random_id': random.randint(39,1000)+time.localtime().tm_sec,
                                                'message': data.faq_message[9]
                                            })
                                        )})
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='MotherCaptl':
            botLib.session.method('messages.sendMessageEventAnswer',
                    {
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id'],
                    'event_data': json.dumps(
                                            botLib.session.method('messages.send',{
                                                'user_id': event.object['user_id'],
                                                'random_id': random.randint(38,1000)+time.localtime().tm_sec,
                                                'message': data.faq_message[8]
                                            })
                                        )})



def admin_panel(events:VkBotMessageEvent):

    botLib.writeInFile(admin_panel.__name__, events.message['from_id'])

    print('●!ban user_id - бан пользователя\n●!unban user_id - разблокировка пользователя\n●!setadmin user_id permission - поставить пользователю статус admin\n●!help - описание всех команд')

    command=str(input())

    while (command!='!exit'):
        if '!ban' in command:
            userid=int(command[command.find(' ')+1:])
            botLib.banUser(userid)
        elif '!unban' in command:
            userid=int(command[command.find(' ')+1:])
            botLib.unBanUser(userid)
        elif '!setpermission' in command:
            userid=int(command[command.find(' ')+1:command.rfind(' ')])
            permission=command[command.rfind(' ')+1:]
            botLib.setUserPermission(userid,permission)
        elif '!exit' in command:
            start(events,False)
        elif '!help' in command:
            print('●!ban user_id - бан пользователя\n●!unban user_id - разблокировка пользователя\n●!setadmin user_id permission - поставить пользователю статус admin\n●!help - описание всех команд')
        
        command=str(input())
          


#Функция старта для новых пользователей
def start(event:VkBotMessageEvent):

    print('LAUNCH SCENARY: ', start.__name__.upper())

    if botLib.checkUserOnBan(event)==True:
        pass

    else:

        if event.type==VkBotEventType.MESSAGE_NEW and event.from_user:
            if event.message['text']=='Начать' or event.message['text']=='Старт':
                botLib.session.method('messages.send',
                            {
                            'user_id': event.message['from_id'],
                            'keyboard': botLib.keyboard_start.get_keyboard(),
                            'random_id': 0,
                            'attachment': 'photo-221557455_457239033',
                            'message': data.start_messages
                            }
                        )

        if event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=="!admin":
                permission=botLib.getUserPermission(event.message['from_id'])
                if permission=='admin':
                    admin_panel(event)
                else:
                    botLib.session.method('messages.send',
                        {
                        'user_id': event.message['from_id'],
                        'random_id': random.randint(15,1000)+time.localtime().tm_sec,
                        'message': 'Я вас не понимаю. Извините :('
                        }
                    )


        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='directions':
                botLib.session.method('messages.sendMessageEventAnswer',{
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id'],
                })

                botLib.writeInFile(directions.__name__,event.object['user_id'])
                directions(event)


        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='faq':
                botLib.session.method('messages.sendMessageEventAnswer',{
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id']
                })

                botLib.writeInFile(faq.__name__,event.object['user_id'])
                faq(event)



def main():
    print("BOT STARTED")

    print('Launch scenary: ', main.__name__)
    for event in botLib.bot_longpoll.listen():

        if event.type != VkBotEventType.MESSAGE_TYPING_STATE:
            botLib.sPrintLog(event,True,'BotLog.txt')

        if event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=="Начать":
            botLib.writeInFile_start(event.message['from_id'],event.message['from_id'],'user')
            start(event)

        elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=="Старт":
            botLib.writeInFile(start.__name__,event.message['from_id'])
            start(event)

        if event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0] in botLib.payload_arrStart:
            botLib.writeInFile(start.__name__,event.object['user_id'])
            start(event)

        elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=="!admin":
            botLib.writeInFile(start.__name__,event.message['from_id'])
            start(event)

        elif event.type==VkBotEventType.MESSAGE_NEW and event.message['text'] in botLib.payload_arrDirection:
            botLib.writeInFile(directions.__name__,event.message['from_id'])
            directions(event)

        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0] in botLib.payload_arrFaq:
            botLib.writeInFile(faq.__name__,event.object['user_id'])
            faq(event)

        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0] == 'start':
            botLib.session.method('messages.sendMessageEventAnswer',
                        {
                        'event_id':event.object['event_id'],
                        'user_id':event.object['user_id'],
                        'peer_id':event.object['peer_id'],
                        'event_data': json.dumps(botLib.session.method('messages.send',{
                                        'user_id': event.object['user_id'],
                                        'random_id':random.randint(21,1000)+time.localtime().tm_sec,
                                        'keyboard':botLib.keyboard_start.get_keyboard(),
                                        'attachment': 'photo-221557455_457239033',
                                        'message':data.start_messages
                                    }
                                ))
                        }
                    )
            botLib.writeInFile(start.__name__,event.object['user_id'])
            start(event)



main()
