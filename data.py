
start_messages=""" 
Привет, это компьютерная школа "Инфосфера"!)\n
В нашей школе дети осваивают компьютерные технологии на профессиональном уровне. Обучение в школе поможет воспитать у детей информационную культуру, развить системное мышление и научиться решать задачи творчески.\n
Компьютерная школа «Инфосфера» была образована 17 декабря 2009 года. С 2022 года открыт филиал в г. Нижний Новгород\n
Сейчас успешно обучаются более 600 детей от 7 до 16 лет по следующим направлениям:\n\n
    ● Информатика
    ● Информационные технологии
    ● Робототехника
    ● Программирование
    ● Компьютерная графика\n\n
Квалифицированные педагоги-практики помогут ребятам реализовать творческий потенциал и воплотить в жизнь свои уникальные идеи и замыслы!
                """

direction_messages_start="""
Какую траекторию вы хотите изучить:
    ● Подготовительная
    ● Байтик
    ● Инфомиры
    ● Инфостарт
                """

faq_message_last="""
Если у вас остались еще вопросы, мы можете связаться с нами через:
    ● Телефон: +79040567288
    ● Электронная почта: infosferann@mail.ru
    ● @nn.isphera(Группа)
    """


direction_messages={
    'Подготовительная':"""
●Развитие логического и образного мышления\n
Творчество в мультимедийных адаптированных программах (Музыкальный конструктор MAGIX MUSIC MAKER, Audacity, Фантазеры), знакомство с компьютером, работа с микрофоном и устройствами ввода текстовой информации, конструирование
                        """,
    'Байтик':""" 
●Знакомство с компьютером и робототехникой.\n
Робототехника, создание мультфильмов с озвучкой в команде, изучение приемов форматирования текста в простых текстовых редакторах, работа в графическом редакторе Paint.
            """,
    'Инфомиры': """ 
●Длится ступень 3 года. ИМ1, ИМ2, ИМ3\n\n
Продвинутые навыки работы в Microsoft Office, основы программирования и робототехники.\n
Изучение устройств компьютера и организации файлового пространства, освоение основных алгоритмических конструкций, программирования и конструирования роботов, создание профессиональных презентаций и текстовых документов.

                """,
    'Инфостарт': """ 
●«Инфостарт-0»: 5 класс – поступают ребята, которые до этого у нас не учились\n\n
На этом курсе дети познакомятся с работой в графическом редакторе Figma, попробуют сверстать сайты, научатся конструировать роботов и программировать их. Модульный интегрированный курс «Инфостарт 0» поможет тем, кто только что познакомился с Инфосферой, определится с интересами в IT-области и направлением дальнейшего обучения.\n\n\n                     
●Третья ступень «Инфостарт» (6,7 класс)\n\n
Первое знакомство с профессиональными средами в компьютерном дизайне, программировании и системном администрировании.\n
На этой ступени дети знакомятся с векторной и растровой графикой в программах СorelDraw и Photoshop, изучают робототехнику на конструкторах, Arduino, верстают сайты на HTML. Инфостарт поможет тем, кто только что познакомился с Инфосферой и хочет продвинуться в области IT.\n\n\n                     
Третья ступень «Инфопро» и «Инфостарт» (6, 7 класс)\n\n
●В Инфостарт мы приглашаем всех желающих. В Инфопро поступают дети, успешно закончившие Инфомиры.
                            """}

faq_message={
    0: 
    """
    Принимаете ли в школу 6-леток (детей, которые ходят в садик)?

    ● Обучение начинается с 7 летнего возраста. Мы ждем детей, которые идут в сентябре в первый класс. Это связано с умением организовывать свою учебную деятельность. Чаще всего ребенок остается учится у нас с 1 по 7 класс. Для освоения курса робототехники и программирования на последующих возрастных ступенях (Байтик, Инфомиры) требуются математические знания и общеучебные умения и навыки уровня 2-3 класса начальной школы. Наша программа основывается на базовом школьном курсе математики.
    """,
    1: 
    """
    Что необходимо для учебы в школе?

    ● Ручка, карандаш, ластик, папка-скоросшиватель, флэш - карта. И желание учиться!)
    """,
    2: 
    """
    Нужен ли дома компьютер для выполнения домашних заданий?

    ● Для выполнения домашних заданий компьютер будет необходим на ступени обучения «Инфомиры». Если дома компьютер отсутствует либо сломался, то ребенок может приходить в компьютерную школу «Инфосфера» и заниматься за свободным компьютером.
    """,
    3:
    """
    Сколько раз в неделю занимаются дети? Какова длительность занятий?
    
    ● Расписание компьютерной школы составлено таким образом, что дети приходят в Инфосферу 2-3 раза в неделю в зависимости от возраста и ступени обучения. Длительность занятий – 45 минут. 10 минут перемена.

    """,
    4:
    """
    Подойдет ли нам расписание? Мой ребенок ходит еще на другие занятия, в другие кружки.

    ● При составлении расписания мы стараемся учитывать Ваши пожелания. Мы предложим заполнить анкету, где Вы укажете удобные дни и время. В нашей школе есть несколько групп и есть варианты разных дней для посещения занятий.
    """,
    5:
    """
    Если ребенок учится в общеобразовательной школе во вторую смену, то может ли он обучаться в компьютерной школе?

    ● Да, занятия в компьютерной школе «Инфосфера» проводятся и в первую, и во вторую смену.
    """,
    6:
    """
    Что включает тестирование в школу? В какой форме оно проходит?

    ● Мы предлагаем тест, распечатанный на бумаге, который включает в себя задание на логику, мышление и сообразительность. Все задания разработаны с учетом возраста ребенка.
    """,
    7:
    """
    Можно ли получить налоговый вычет по вашему договору?

    ● Да, у школы есть лицензия на образовательную деятельность и Вы можете оформить налоговый вычет. Мы можем отправить Вам скан-копию договора на адрес электронной почты, указанный 
    """,
    8:
    """
    Можно ли оплачивать дополнительное обучение за счет материнского капитала?

    ● Средства материнского капитала можно использовать для оплаты детского сада, частной школы или продленки, дополнительного образования, репетитора или курсов, учебы в вузе, а также жилья на время учебы. Направить средства сертификата на образование любого из детей можно, когда ребенку исполнится три года.
    """
}