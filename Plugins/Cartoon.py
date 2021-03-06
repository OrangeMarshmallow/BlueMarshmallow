from Plugins.Base import BasePlugin as base
import random


class CartoonPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Мультик'
        self.description = 'Отправляет случайный мультик для просмотра'
        self.words = ["мультик", "cartoon"]

    def func(self):
        try:
            m = [
                "101 далматинец",
                "101 далматинец 2: Приключения Патча в Лондоне",
                "7 гномов (мультсериал)",
                "Pixar - коллекция короткометражекАватар: Легенда об Аанге и Корре",
                "Аисты",
                "Алиса в стране чудес",
                "Алладин (мультсериал)",
                "Алладин",
                "Алладин 2: Возвращение Джафара",
                "Алладин 3: Король разбойников",
                "Альфа и Омега (1-8 части)",
                "Американский дракон: Джейк Лонг",
                "Анастасия",
                "Артур и минипуты (1-3 части)",
                "Астробой",
                "Атлантида 2: Возвращение Майло",
                "Атлантида: Затерянный мирБалерина",
                "Балто (1-2-3 части)",
                "Барби (все серии)",
                "Барби: Академия принцесс",
                "Барби: Балерина в розовых пуантах",
                "Барби: Виртуальный мир",
                "Барби: Жизнь в доме мечты",
                "Барби: Принцесса и поп-звезда",
                "Барбоскины",
                "Белоснежка и семь гномов",
                "Би Муви: Медовый заговор",
                "Большое путешествие",
                "Большой собачий побег",
                "Большой фильм про поросенка",
                "Босс-молокосос",
                "Братец медвежонок",
                "Братец медвежонок 2: Лоси в бегах",
                "Буба (Домовёнок)",
                "Бунт ушастых",
                "Бэмби",
                "Бэмби 2В гости к Робинсонам",
                "В поисках Немо (+ В поисках Дори)",
                "ВАЛЛИ",
                "Вверх",
                "Великий мышиный сыщик",
                "Весёлые паровозики из Чаггингтона (Чагинтона)",
                "Винкс",
                "Винкс на концерте: музыка, песни, клипы",
                "Винкс: Волшебное приключение",
                "Винкс: Тайна затерянного королевства",
                "Винкс: Тайна морской бездны",
                "Винни Пух (Дисней)",
                "Винни и Слонотоп",
                "Винни Пух и Слонотоп Хэллоуин",
                "Винни Пух: Весенние денёчки с малышом Ру",
                "Винни Пух: Время делать подарки",
                "Винни Пух: Рождественский Пух",
                "Вольт",
                "Время Приключений (Фин и Джейк)",
                "Вспыш и Чудо-МашинкиГадкий Я",
                "Гадкий Я 2",
                "Гадкий Я 3",
                "Гадкий Я: Миньоны (Мини-фильмы)",
                "Геркулес",
                "Геркулес (мультсериал)",
                "Герои в масках",
                "Герои Энвелла",
                "Гнездо дракона (1-2 части)",
                "Гномео и Джульетта",
                "Головоломка",
                "Горбун из Нотр Дама",
                "Горбун из Нотр Дама 2",
                "Город героев",
                "Город тачек",
                "Гравити Фолз",
                "Губка Боб (Спанч Боб)",
                "Гуфи и его команда",
                "Гуфи: экстремальный спортДамбо",
                "Дар ночной фурии",
                "Девять",
                "Делай ноги",
                "Делай ноги 2",
                "Дети дождя",
                "Джок",
                "Динозавр",
                "Доктор Плюшева",
                "Дом (Контакт неизбежен)",
                "Дом-монстр",
                "Дональд Дак",
                "Дорога на Эльдорадо",
                "Драконы и Всадники Олуха (мультсериал)",
                "Драконы: Гонки бесстрашных - Начало",
                "Друзья ангелов (мультсериал)",
                "Друзья ангелов: Между мечтой и реальностью",
                "ЕгиптусЗачарованная",
                "Зверопой",
                "Зверополис",
                "Звёздная Принцесса (Стар против Сил Зла)",
                "Звёздные войны: Войны Клонов",
                "Звёздные войны: Повстанцы",
                "Золушка",
                "Золушка 2: Мечты сбываются",
                "Золушка 3: Злые чарыИгорь",
                "Иосиф - царь сновидений",
                "История игрушек",
                "История игрушек 2",
                "История игрушек 3: Большой побегКак приручить дракона",
                "Как приручить дракона 2",
                "Каникулы Гуфи",
                "Кид vs Кэт (Кит виси Кет)",
                "Ким пять с плюсом",
                "Клуб Винкс: Школа волшебниц",
                "Клуб Микки Мауса",
                "Книга джунглей",
                "Книга джунглей 2",
                "Книга драконов",
                "Книга жизни",
                "Команда Умизуми",
                "Коралина в стране кошмаров",
                "Король Лев",
                "Король Лев 2: Гордость Симбы",
                "Король Лев 3: Хакуна матата",
                "Корпорация монстров",
                "Кот в сапогах",
                "Кот в сапогах: Три Чертёнка",
                "Кот Гром и заколдованный дом",
                "Коты-аристократы",
                "Кошмар перед Рождеством",
                "Красавица и Чудовище",
                "Красавица и Чудовище 2: Заколдованное Рождество",
                "Красавица и Чудовище 3: Волшебный мир Бель",
                "Кряк-Бряк",
                "Кубо - Легенда о самурае",
                "Кунг-фу Панда",
                "Кунг-фу Панда 2",
                "Кунг-фу Панда 3",
                "Кунг-Фу Панда: Загадки свитка",
                "Кунг-фу Панда: Праздничный выпуск",
                "Кунг-Фу Панда: Секреты мастеров",
                "Кунг-фу Панда: Секреты неистовой пятерки",
                "Кунг-фу Панда: Удивительные легенды (мультсериал)Легенда о Костяном Драконе",
                "Легенды ночных стражей",
                "Лего (Фильм)",
                "Лего Бэтмен",
                "Лего Звёздные войны",
                "Лего Ниндзяго (Фильм)",
                "Лего Ниндзяго: Мастера Кружитцу",
                "Леди Баг и Супер-Кот",
                "Леди и Бродяга",
                "Леди и Бродяга 2: Приключения Шалуна",
                "Ледниковый период (все серии)",
                "Лео и Тиг",
                "Лерой и Стич",
                "Лесная братва",
                "Лило и Стич (мультсериал)",
                "Лило и Стич",
                "Лило и Стич 2: Большая проблема Стича",
                "Лис и Пёс",
                "Лис и Пёс 2",
                "Лоракс",
                "ЛунтикМадагаскар",
                "Мадагаскар 2",
                "Мадагаскар 3",
                "Мадагаскар: Любовная лихорадка",
                "Мадагаскар: Рождество",
                "Маленькие Эйнштейны",
                "Маленький принц (2015)",
                "Малефисента",
                "Маша и Медведь (все серии) + Сказки и Страшилки",
                "Мегамозг",
                "Мегамозг: Кнопка гибели",
                "Медвежонок Винни и его друзья",
                "Меч в камне",
                "Микки Маус: Волшебное Рождество у Микки",
                "Микки Маус: Злодеи в доме Микки",
                "Микки: И снова под Рождество",
                "Микки: Однажды под Рождество",
                "Миньоны",
                "Миссия Дарвина",
                "Мишки Гамми",
                "Моана",
                "Мой шумный дом",
                "Монстер Хай (Школа Монстров)",
                "Монстр в Париже",
                "Монстры на каникулах (1-2 части)",
                "Монстры против пришельцев (все серии)",
                "Морская бригада",
                "Мулан",
                "Мулан 2",
                "Муравей АнтцНа замену",
                "Не бей копытом",
                "Новая школа императора",
                "Новые приключения Винни Пуха (мультсериал)",
                "Новые приключения Стича",
                "Норм и НесокрушимыеОбратный отсчет к Рождеству",
                "Огнедышащий",
                "Оливер и компания",
                "Отважный маленький тостер",
                "Охотники на троллейПаранорман или Как приручить зомби",
                "Песнь моря",
                "Пингвины из Мадагаскара (мультсериал)",
                "Пиноккио",
                "Пираты - Банда неудачников",
                "Питер Пен",
                "Питер Пен 2: Возвращение в Неверленд",
                "Планета 51",
                "Планета сокровищ",
                "Побег из курятника",
                "Подводная братва",
                "Покахонтас",
                "Покахонтас 2",
                "Полярный экспресс",
                "ПопПикси",
                "Похождения императора",
                "Похождения императора 2: Приключения Кронка",
                "Приключения Винни Пуха",
                "Приключения Икабода и мистера Тоада",
                "Приключения мистера Пибоди и Шермана",
                "Приключения Тигрули",
                "Приключения Тинтина: Тайна Единорога",
                "Приключения флика",
                "Принц Египта",
                "Принцесса и лягушка",
                "Принцесса Лебедь (1-6 части)Ральф",
                "Ранго",
                "Рапунцель (все серии)",
                "Рататуй",
                "Реальная белка (1-2 части)",
                "Рио",
                "Рио 2",
                "Робин Гуд",
                "Робинзон Крузо: Очень обитаемый остров",
                "Робокар Поли",
                "Рождественская история (2009)",
                "Рождественская история Микки",
                "Ромео с Обочины",
                "Ронал-варвар",
                "Русалочка (мультсериал)",
                "Русалочка",
                "Русалочка 2: Возвращение в море",
                "Русалочка 3: Начало истории Ариэль",
                "РыбологияСамолёты (1-2 части)",
                "Сезон охоты (1-4 части)",
                "Семейка Крудс (все серии)",
                "Синдбад: Легенда семи морей",
                "Сказочный патруль",
                "Скрудж МакДак и деньги",
                "Смешарики",
                "Смешарики - Азбука",
                "Смешарики - Начало",
                "Смешарики - Новые приключения",
                "Смешарики - Пин-Код",
                "Смурфики (1-5 части)",
                "Смывайся",
                "Снежная королева (1-3 части)",
                "Снежная королева (1957, СССР)",
                "Снежная королева (1995-1996, Великобритания)",
                "Сорвиголова Кик Бутовски",
                "София Прекрасная",
                "Союз зверей",
                "Спанч Боб (Губка Боб)",
                "Спасатели",
                "Спасатели в Австралии",
                "Спецагент ОСО",
                "Спирит: Душа прерий",
                "Спящая красавица",
                "Стар против Сил Зла (Звёздная Принцесса)",
                "Стальной гигант",
                "Странные чары",
                "СуперсемейкаТайна Коко",
                "Тайна красной планеты",
                "Тайная жизнь домашних животных",
                "Тарзан",
                "Тарзан 2",
                "Тарзан и Джейн",
                "Тачки (1-3 части)",
                "Тачки / Молния Маквин (все серии)",
                "Тачки Мультачки: Байки Мэтра",
                "Тимон и Пумба",
                "Тотали Спайс",
                "Трактор Том",
                "Трансформеры (1986)",
                "Трансформеры (фильмы / 1-5 части)",
                "Трансформеры G1: Первое поколение",
                "Трансформеры: Анимейтед",
                "Трансформеры: Боты Спасатели",
                "Трансформеры: Прайм",
                "Трансформеры: Роботы под прикрытием",
                "Три мушкетера. Микки, Дональд, Гуфи",
                "Тролли",
                "Труп невесты",
                "Турбо",
                "Турнир Долины ФейУмелец Мэнни",
                "Университет монстров",
                "Утиные истории (мультсериал)",
                "Утиные истории: Заветная лампаФантазия",
                "Фантазия 2000",
                "Феи",
                "Феи 2: Потерянное сокровище",
                "Феи 3: Большое волшебное спасение",
                "Феи: Загадка пиратского острова",
                "Феи: Легенда о чудовище",
                "Феи: Тайна зимнего леса",
                "Феи: Торт и Спорт",
                "Фердинанд",
                "Фиксики",
                "Финес и Ферб (мультсериал)",
                "Финес и Ферб: Через второе измерение",
                "Финли - маленькая пожарная машина",
                "ФранкенвиниХолодное торжество (1-4 части)",
                "Хороший динозавр",
                "Хортон",
                "Храбрая сердцем",
                "Хранители снов",
                "Хранитель Лев (мультсериал)",
                "Хранитель ЛуныЦыплёнок ЦыпаЧародейки",
                "Черепашки навсегда (2009)",
                "Черепашки-ниндзя (2007)",
                "Черепашки-ниндзя (Никелодеон) (мультсериал)",
                "Черепашки-ниндзя (фильмы / 2014 / 2016)",
                "Чёрный котёл",
                "Чёрный Плащ",
                "Чип и Дейл (1947-1955)",
                "Чип и Дейл спешат на помощь (мультсериал)",
                "Чокнутый",
                "Чудеса на виражахШевели ластами (1-2 части)",
                "Школа волшебниц (Клуб Винкс)",
                "Школа монстров (Монстер Хай)",
                "Шрек",
                "Шрек 2",
                "Шрек 3",
                "Шрек 4: Шрек навсегда",
                "Шрек мороз, зеленый нос",
                "Шрек: Медовый месяц (или Призрак Лорда Фаркуада)",
                "Шрек: Хэллоуин (Страшилки)Щенячий патрульЭлвин и бурундуки (1-4 части)",
                "Эмоджи",
                "Эпик"
            ]
            self.result['message'] = 'Случайный мультик: ' + random.choice(m)
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
