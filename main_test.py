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
def directions(events:VkBotMessageEvent):

    botLib.writeInFile('scenary.json','directions')

    user_id=events.object['user_id']

    botLib.session.method('messages.send',{
                    'user_id': user_id,
                    'random_id': random.randint(2,1000)+time.localtime().tm_sec,
                    'keyboard':botLib.keyboard_directions.get_keyboard(),
                    'attachment': 'photo-221557455_457239032',
                    'message':data.direction_messages_start})
    

    for event in botLib.bot_longpoll.listen():
        botLib.printLog(event)
        if event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Подготовительная (1 класс)':
            botLib.session.method('messages.send',
                {
                'user_id': user_id,
                'random_id': random.randint(3,1000)+time.localtime().tm_sec,
                'attachment': 'photo-221557455_457239037',
                'message': data.direction_messages['Подготовительная']
                }
            )


        elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Байтик (2 класс)': 
            botLib.session.method('messages.send',
                {
                'user_id': user_id,
                'random_id': random.randint(4,1000)+time.localtime().tm_sec,
                'attachment': 'photo-221557455_457239036',
                'message': data.direction_messages['Байтик']
                }
            )
             

        elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Инфомиры (3-4 класс)':
            botLib.session.method('messages.send',
                {
                'user_id': user_id,
                'random_id': random.randint(5,1000)+time.localtime().tm_sec,
                'attachment': 'photo-221557455_457239035',
                'message': data.direction_messages['Инфомиры']
                }
            )


        elif event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=='Инфостарт (5-7 класс)':
            botLib.session.method('messages.send',
                {
                'user_id': user_id,
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
            start()



def faq(events:VkBotMessageEvent):

    botLib.writeInFile('scenary.json','faq')

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
        botLib.printLog(event)
        if event.type==VkBotEventType.MESSAGE_REPLY:
            message_id=event.obj['conversation_message_id']
            for event2 in botLib.bot_longpoll.listen():
                if (i>data.faq_message.__len__() or i<0:)
                        botLib.session.method('messages.send',{
                            'user_id': event.object['user_id'],
                            'peer_id': event.object['user_id'],
                            'keyboard': botLib.keyboard_faq.get_keyboard(),
                            'random_id': random.randint(10,1000)+time.localtime().tm_sec,
                            'message': data.faq_message[0]
                            
                            })
                        break
                else:

                    if event2.type==VkBotEventType.MESSAGE_EVENT and event2.object['payload'][0]=='next':
                        i+=1

                        if (i>data.faq_message.__len__() or i<0):
                            botLib.session.method('messages.send', {
                                'user_id': event.object['user_id'],
                                'random_id': random.randint(12,1000)+time.localtime().tm_sec,
                                'message': data.start_messages
                            })

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
                        start()


#Функция старта для новых пользователей
def start():

    botLib.writeInFile('scenary.json','start')

    print('Launch scenary: ', start.__name__)

    for event in botLib.bot_longpoll.listen():
        # check=botLib.session.method('messages.getLongPollServer',{'need_pts':1,'group_id':event.group_id,'lp_version':3})
        # long=botLib.session.method('messages.getLongPollHistory',{'ts':check['ts'], 'group_id': event.group_id,'preview_length':0})
        botLib.printLog(event)
        # print(long)
        if event.type==VkBotEventType.MESSAGE_NEW and event.from_user and event.message['text']=="Начать":
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
                'peer_id':event.object['peer_id']
            })

            directions(event)
        

        elif event.type==VkBotEventType.MESSAGE_EVENT and event.object['payload'][0]=='faq':
            botLib.session.method('messages.sendMessageEventAnswer',{
                'event_id':event.object['event_id'],
                'user_id':event.object['user_id'],
                'peer_id':event.object['peer_id']
            })
            
            faq(event)

def main():
    print("BOT STARTED")
    print('Launch scenary: ', main.__name__)

    if 'start' == botLib.readFile('scenary.json'):
        start()
    elif 'directions' == botLib.readFile('scenary.json'):
        directions()
    elif 'faq' == botLib.readFile('scenary.json'):
        faq()
    else:
       botLib.writeInFile('scenary.json','start')
       start()


main()
