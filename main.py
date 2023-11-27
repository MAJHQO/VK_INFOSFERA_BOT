import vk_api as vk_api
import botLib
import data
import random
import json
import datetime
import time

from vk_api.bot_longpoll import VkBotEventType,VkBotLongPoll,VkBotMessageEvent,VkBotEvent
from vk_api.requests_pool import VkRequestsPool,RequestResult

#Для каждого пользователя свой файл с id, peer_id и state сценария - ВАЖНО

#Функция сценария "О направлениях"
def directions(events:VkBotMessageEvent,restart:bool):

    print('LAUNCH SCENARY: ', directions.__name__.upper(), restart)

    if (restart):
        botLib.sPrintLog(events,True,'BotLog.txt')
        if events.type==VkBotEventType.MESSAGE_NEW and events.from_user and events.message['text']=='Подготовительная (1 класс)':
            botLib.session.method('messages.send',
                {
                'user_id': events.message['from_id'],
                'random_id': random.randint(3,1000)+time.localtime().tm_sec,
                'attachment': 'photo-221557455_457239037',
                'message': data.direction_messages['Подготовительная']
                }
            )


        elif events.type==VkBotEventType.MESSAGE_NEW and events.from_user and events.message['text']=='Байтик (2 класс)': 
            botLib.session.method('messages.send',
                {
                'user_id': events.message['from_id'],
                'random_id': random.randint(4,1000)+time.localtime().tm_sec,
                'attachment': 'photo-221557455_457239036',
                'message': data.direction_messages['Байтик']
                }
            )
             

        elif events.type==VkBotEventType.MESSAGE_NEW and events.from_user and events.message['text']=='Инфомиры (3-4 класс)':
            botLib.session.method('messages.send',
                {
                'user_id': events.message['from_id'],
                'random_id': random.randint(5,1000)+time.localtime().tm_sec,
                'attachment': 'photo-221557455_457239035',
                'message': data.direction_messages['Инфомиры']
                }
            )


        elif events.type==VkBotEventType.MESSAGE_NEW and events.from_user and events.message['text']=='Инфостарт (5-7 класс)':
            botLib.session.method('messages.send',
                {
                'user_id': events.message['from_id'],
                'random_id': random.randint(6,1000)+time.localtime().tm_sec,
                'attachment': 'photo-221557455_457239034',
                'message': data.direction_messages['Инфостарт']
                }
            )
        

        elif events.type==VkBotEventType.MESSAGE_EVENT and events.object['payload'][0]=='start':
            botLib.session.method('messages.sendMessageEventAnswer',
                    {
                    'event_id':events.object['event_id'],
                    'user_id':events.object['user_id'],
                    'peer_id':events.object['peer_id'],
                    'event_data': json.dumps(botLib.session.method('messages.send',{
                                    'user_id': events.object['user_id'],
                                    'random_id':random.randint(7,1000)+time.localtime().tm_sec,
                                    'keyboard':botLib.keyboard_start.get_keyboard(),
                                    'attachment': 'photo-221557455_457239033',
                                    'message':data.start_messages
                                }
                            ))
                    }
                )
            botLib.writeInFile(start.__name__,events.object['user_id'])
            start(events,False)

    else:
            botLib.session.method('messages.send',{
                    'user_id': events.object['user_id'],
                    'random_id': random.randint(2,1000)+time.localtime().tm_sec,
                    'keyboard':botLib.keyboard_directions.get_keyboard(),
                    'attachment': 'photo-221557455_457239032',
                    'message':data.direction_messages_start})


            for event in botLib.bot_longpoll.listen():
                botLib.sPrintLog(event,True,'BotLog.txt')
                if event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Подготовительная (1 класс)':
                    botLib.session.method('messages.send',
                        {
                        'user_id': event.message['from_id'],
                        'random_id': random.randint(3,1000)+time.localtime().tm_sec,
                        'attachment': 'photo-221557455_457239037',
                        'message': data.direction_messages['Подготовительная']
                        }
                    )


                elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Байтик (2 класс)': 
                    botLib.session.method('messages.send',
                        {
                        'user_id': event.message['from_id'],
                        'random_id': random.randint(4,1000)+time.localtime().tm_sec,
                        'attachment': 'photo-221557455_457239036',
                        'message': data.direction_messages['Байтик']
                        }
                    )
                    

                elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Инфомиры (3-4 класс)':
                    botLib.session.method('messages.send',
                        {
                        'user_id': event.message['from_id'],
                        'random_id': random.randint(5,1000)+time.localtime().tm_sec,
                        'attachment': 'photo-221557455_457239035',
                        'message': data.direction_messages['Инфомиры']
                        }
                    )


                elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Инфостарт (5-7 класс)':
                    botLib.session.method('messages.send',
                        {
                        'user_id': event.message['from_id'],
                        'random_id': random.randint(6,1000)+time.localtime().tm_sec,
                        'attachment': 'photo-221557455_457239034',
                        'message': data.direction_messages['Инфостарт']
                        }
                    )
                

                elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='start':
                    botLib.session.method('messages.sendMessageEventAnswer',
                            {
                            'event_id':event.object['event_id'],
                            'user_id':event.object['user_id'],
                            'peer_id':event.object['peer_id'],
                            'event_data': json.dumps(botLib.session.method('messages.send',{
                                            'user_id': event.object['user_id'],
                                            'random_id':random.randint(7,1000)+time.localtime().tm_sec,
                                            'keyboard':botLib.keyboard_start.get_keyboard(),
                                            'attachment': 'photo-221557455_457239033',
                                            'message':data.start_messages
                                        }
                                    ))
                            }
                        )
                    botLib.writeInFile(start.__name__,event.object['user_id'])
                    start(event,False)
            


def faq(events:VkBotMessageEvent,restart:bool):

    print('LAUNCH SCENARY: ', faq.__name__.upper(),restart)

    botLib.session.method('messages.send',
                    {
                    'user_id': events.object['user_id'],
                    'peer_id': events.object['user_id'],
                    'keyboard': botLib.keyboard_faq.get_keyboard(),
                    'random_id': random.randint(9,1000)+time.localtime().tm_sec,
                    'message': data.faq_message[0]
                    }
    )
    i=0

    for event in botLib.bot_longpoll.listen():
        botLib.sPrintLog(event,True,'BotLog.txt')
        if event.type==VkBotEventType.MESSAGE_REPLY:

            message_id=event.obj['conversation_message_id']
            for event2 in botLib.bot_longpoll.listen():

                if event2.type==VkBotEventType.MESSAGE_EVENT and event2.object['payload'][0]=='next':
                    i+=1
                    if (i==data.faq_message.__len__()):
                        i=data.faq_message.__len__()
                        botLib.session.method('messages.sendMessageEventAnswer',
                        {
                        'event_id':event2.object['event_id'],
                        'user_id':event2.object['user_id'],
                        'peer_id':event2.object['peer_id'],
                        'event_data':
                            json.dumps (botLib.session.method('messages.edit',
                                        {
                                        'peer_id':event.object['peer_id'],
                                        'group_id':event.raw['group_id'],
                                        'conversation_message_id':message_id,
                                        'message':data.faq_message_last
                                        }
                        ))
                        })
                    elif(i>data.faq_message.__len__()):
                        i=data.faq_message.__len__()
                        botLib.session.method('messages.sendMessageEventAnswer',
                        {
                        'event_id':event2.object['event_id'],
                        'user_id':event2.object['user_id'],
                        'peer_id':event2.object['peer_id']
                        })

                    else:
                        botLib.session.method('messages.sendMessageEventAnswer',
                        {
                        'event_id':event2.object['event_id'],
                        'user_id':event2.object['user_id'],
                        'peer_id':event2.object['peer_id'],
                        'event_data':
                            json.dumps (botLib.session.method('messages.edit',
                                        {
                                        'peer_id':event.object['peer_id'],
                                        'group_id':event.raw['group_id'],
                                        'conversation_message_id':message_id,
                                        'message':data.faq_message[i]
                                        }
                        ))
                        })



                elif event2.type==VkBotEventType.MESSAGE_EVENT and event2.object['payload'][0]=='back':
                    i-=1

                    if (i==-1):
                        i=-1
                        botLib.session.method('messages.sendMessageEventAnswer',
                        {
                        'event_id':event2.object['event_id'],
                        'user_id':event2.object['user_id'],
                        'peer_id':event2.object['peer_id'],
                        'event_data':
                            json.dumps (botLib.session.method('messages.edit',
                                        {
                                        'peer_id':event.object['peer_id'],
                                        'group_id':event.raw['group_id'],
                                        'conversation_message_id':message_id,
                                        'message':data.faq_message_last
                                        }
                        ))
                        })

                    elif(i<-1):
                        i=-1
                        botLib.session.method('messages.sendMessageEventAnswer',
                        {
                        'event_id':event2.object['event_id'],
                        'user_id':event2.object['user_id'],
                        'peer_id':event2.object['peer_id']
                        })

                    else:
                        botLib.session.method('messages.sendMessageEventAnswer',
                        {
                        'event_id':event2.object['event_id'],
                        'user_id':event2.object['user_id'],
                        'peer_id':event2.object['peer_id'],
                        'event_data':
                            json.dumps(botLib.session.method('messages.edit',
                                            {
                                            'peer_id':event.object['peer_id'],
                                            'group_id':event.raw['group_id'],
                                            'conversation_message_id':message_id,
                                            'message':data.faq_message[i]
                                            }
                            ))
                        })
                    

                elif event2.type==VkBotEventType.MESSAGE_EVENT and event2.object['payload'][0]=='start':
                    botLib.session.method('messages.sendMessageEventAnswer',
                            {
                            'event_id':event2.object['event_id'],
                            'user_id':event2.object['user_id'],
                            'peer_id':event2.object['peer_id'],
                            'event_data': json.dumps(botLib.session.method('messages.send',{
                                'user_id': event2.object['user_id'],
                                'random_id':random.randint(11,1000)+time.localtime().tm_sec,
                                'keyboard':botLib.keyboard_start.get_keyboard(),
                                'attachment': 'photo-221557455_457239033',
                                'message':data.start_messages
                            }
                        ))})
                    if event2.type != VkBotEventType.MESSAGE_REPLY:
                        botLib.writeInFile(start.__name__,event.object['peer_id'])
                        start(event,False)



#Функция старта для новых пользователей
def start(events:VkBotMessageEvent,restart:bool):

    print('LAUNCH SCENARY: ', start.__name__.upper(),restart)

    if events.type==VkBotEventType.MESSAGE_NEW and events.from_user:
        if events.message['text']=='Начать' or events.message['text']=='Старт':
            botLib.session.method('messages.send',
                        {
                        'user_id': events.message['from_id'],
                        'keyboard': botLib.keyboard_start.get_keyboard(),
                        'random_id': 0,
                        'attachment': 'photo-221557455_457239033',
                        'message': data.start_messages
                        }
                    )
    if (restart):
        botLib.sPrintLog(events, True, 'BotLog.txt')

        if events.type == VkBotEventType.MESSAGE_EVENT and events.object['payload'][0] == 'directions':
            botLib.session.method('messages.sendMessageEventAnswer', {
                'event_id': events.object['event_id'],
                'user_id': events.object['user_id'],
                'peer_id': events.object['peer_id'],
            })

            botLib.writeInFile(directions.__name__, events.object['user_id'])
            directions(events,False)


        elif events.type == VkBotEventType.MESSAGE_EVENT and events.object['payload'][0] == 'faq':
            botLib.session.method('messages.sendMessageEventAnswer', {
                    'event_id': events.object['event_id'],
                    'user_id': events.object['user_id'],
                    'peer_id': events.object['peer_id']})

            botLib.writeInFile(faq.__name__, events.object['user_id'])
            faq(events,False)

    else:
        for event in botLib.bot_longpoll.listen():

            botLib.sPrintLog(event,True,'BotLog.txt')
            if event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=="Старт":
                botLib.session.method('messages.send',
                        {
                        'user_id': event.message['from_id'],
                        'keyboard': botLib.keyboard_start.get_keyboard(),
                        'random_id': 0,
                        'attachment': 'photo-221557455_457239033',
                        'message': data.start_messages
                        }
                    )


            elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='directions':
                botLib.session.method('messages.sendMessageEventAnswer',{
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id'],
                })

                botLib.writeInFile(directions.__name__,event.object['user_id'])
                directions(event,False)


            elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='faq':
                botLib.session.method('messages.sendMessageEventAnswer',{
                    'event_id':event.object['event_id'],
                    'user_id':event.object['user_id'],
                    'peer_id':event.object['peer_id']
                })

                botLib.writeInFile(faq.__name__,event.object['user_id'])
                faq(event,False)

def main():
    print("BOT STARTED")
    print('Launch scenary: ', main.__name__)
    for event in botLib.bot_longpoll.listen():
        if event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=="Начать":
            botLib.writeInFile_start(event.message['from_id'],event.message['from_id'],'user')
            start(event,False)
        elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=="Старт":
            botLib.writeInFile(start.__name__,event.message['from_id'])
            start(event,False)

        if event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0] in botLib.payload_arrStart:
            start(event,True)
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0] in botLib.payload_arrDirection:
            directions(event,True)
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0] in botLib.payload_arrFaq:
            faq(event,True)
        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'] == 'start':
            start(event,True)
        
        if event.type != VkBotEventType.MESSAGE_TYPING_STATE:
            botLib.sPrintLog(event,True,'BotLog.txt')


main()
