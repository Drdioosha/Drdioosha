import telebot
import config
from telebot import types
bot = telebot.TeleBot("6629424816:AAFhj0TI4ztwVbIq_jJOz8pmo_K9ZPGg42s", parse_mode=None)
	
@bot.message_handler(commands=['start'])
def welcome(message):
	bot.reply_to(message, "Приветствую, <b>{0.first_name}</b>! ✌\nЭтот бот может быть вам полезен для подготовки к <b>ОГЭ</b>\nПомощь ➜ /help\nПоддержать денежными средствами можно тут ➜ https://www.donationalerts.com/r/andrey_shahov_tg" .format(message.from_user, bot.get_me()),
		parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
	bot.reply_to(message, "Донат: https://www.donationalerts.com/r/andrey_shahov_tg\nКомманды для материалов подготовки к <b>ОГЭ</b>: \n <b>Математика</b> ➜ /matem \n <b>Английский язык</b> ➜ /en \n <b>Информатика</b> ➜ /inf \n <b>Немецкий язык</b> ➜ /de \n <b>Французский язык</b> ➜ /fr \n <b>Испанский язык</b> ➜ /sp \n <b>Физика</b> ➜ /phys \n <b>Химия</b> ➜ /chem \n <b>Биология</b> ➜ /bio \n <b>География</b> ➜ /geo \n <b>Обществознание</b> ➜ /soc \n <b>Литература</b> ➜ /lit \n <b>История</b> ➜ /hist \n <b>Русский язык (письменный экзамен)</b> ➜ /rus \n <b>Русский язык (устное собеседование)</b> ➜ /ruso",
		parse_mode='html')

@bot.message_handler(commands=['donate'])
def donate(message):
	bot.reply_to(message, "Поддержать монеточкой можно тут ➜ https://www.donationalerts.com/r/andrey_shahov_tg",
		parse_mode='html')


@bot.message_handler(commands=['математика', 'матем', 'Математика', 'matem'])
def matem(message):
		matem_but = types.InlineKeyboardMarkup()
		matem_but.add(types.InlineKeyboardButton('1 вариант', url='https://math-oge.sdamgia.ru/test?id=55445928'))
		matem_but.add(types.InlineKeyboardButton('2 вариант', url='https://math-oge.sdamgia.ru/test?id=55445929'))
		matem_but.add(types.InlineKeyboardButton('3 вариант', url='https://math-oge.sdamgia.ru/test?id=55445930'))
		matem_but.add(types.InlineKeyboardButton('4 вариант', url='https://math-oge.sdamgia.ru/test?id=55445931'))
		matem_but.add(types.InlineKeyboardButton('5 вариант', url='https://math-oge.sdamgia.ru/test?id=55445932'))
		matem_but.add(types.InlineKeyboardButton('6 вариант', url='https://math-oge.sdamgia.ru/test?id=55445933'))
		matem_but.add(types.InlineKeyboardButton('7 вариант', url='https://math-oge.sdamgia.ru/test?id=55445934'))
		matem_but.add(types.InlineKeyboardButton('8 вариант', url='https://math-oge.sdamgia.ru/test?id=55445935'))
		matem_but.add(types.InlineKeyboardButton('9 вариант', url='https://math-oge.sdamgia.ru/test?id=55445936'))
		matem_but.add(types.InlineKeyboardButton('10 вариант', url='https://math-oge.sdamgia.ru/test?id=55445937'))
		matem_but.add(types.InlineKeyboardButton('11 вариант', url='https://math-oge.sdamgia.ru/test?id=55445938'))
		matem_but.add(types.InlineKeyboardButton('12 вариант', url='https://math-oge.sdamgia.ru/test?id=55445939'))
		matem_but.add(types.InlineKeyboardButton('13 вариант', url='https://math-oge.sdamgia.ru/test?id=55445940'))
		matem_but.add(types.InlineKeyboardButton('14 вариант', url='https://math-oge.sdamgia.ru/test?id=55445941'))
		matem_but.add(types.InlineKeyboardButton('15 вариант', url='https://math-oge.sdamgia.ru/test?id=55445942'))

		bot.reply_to(message, "<b>Математика.</b> Выберите вариант",
		parse_mode='html', reply_markup=matem_but)
		
@bot.message_handler(commands=['английский язык', 'английский', 'Английский язык', 'Английский', 'en'])
def en(message):
		en = types.InlineKeyboardMarkup()
		en.add(types.InlineKeyboardButton('1 вариант', url='https://en-oge.sdamgia.ru/test?id=1500894'))
		en.add(types.InlineKeyboardButton('2 вариант', url='https://en-oge.sdamgia.ru/test?id=1500895'))
		en.add(types.InlineKeyboardButton('3 вариант', url='https://en-oge.sdamgia.ru/test?id=1500896'))
		en.add(types.InlineKeyboardButton('4 вариант', url='https://en-oge.sdamgia.ru/test?id=1500897'))
		en.add(types.InlineKeyboardButton('5 вариант', url='https://en-oge.sdamgia.ru/test?id=1500898'))
		en.add(types.InlineKeyboardButton('6 вариант', url='https://en-oge.sdamgia.ru/test?id=1500899'))
		en.add(types.InlineKeyboardButton('7 вариант', url='https://en-oge.sdamgia.ru/test?id=1500900'))
		en.add(types.InlineKeyboardButton('8 вариант', url='https://en-oge.sdamgia.ru/test?id=1500901'))
		en.add(types.InlineKeyboardButton('9 вариант', url='https://en-oge.sdamgia.ru/test?id=1500902'))
		en.add(types.InlineKeyboardButton('10 вариант', url='https://en-oge.sdamgia.ru/test?id=1500903'))
		en.add(types.InlineKeyboardButton('11 вариант', url='https://en-oge.sdamgia.ru/test?id=1500904'))
		en.add(types.InlineKeyboardButton('12 вариант', url='https://en-oge.sdamgia.ru/test?id=1500905'))
		en.add(types.InlineKeyboardButton('13 вариант', url='https://en-oge.sdamgia.ru/test?id=1500906'))
		en.add(types.InlineKeyboardButton('14 вариант', url='https://en-oge.sdamgia.ru/test?id=1500907'))
		en.add(types.InlineKeyboardButton('15 вариант', url='https://en-oge.sdamgia.ru/test?id=1500908'))

		bot.reply_to(message, "<b>Английский язык.</b> Выберите вариант",
		parse_mode='html', reply_markup=en)

@bot.message_handler(commands=['информатика', 'Информатика', 'inf'])
def inf(message):
		inf = types.InlineKeyboardMarkup()
		inf.add(types.InlineKeyboardButton('1 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792653'))
		inf.add(types.InlineKeyboardButton('2 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792654'))
		inf.add(types.InlineKeyboardButton('3 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792655'))
		inf.add(types.InlineKeyboardButton('4 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792656'))
		inf.add(types.InlineKeyboardButton('5 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792657'))
		inf.add(types.InlineKeyboardButton('6 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792658'))
		inf.add(types.InlineKeyboardButton('7 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792659'))
		inf.add(types.InlineKeyboardButton('8 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792661'))
		inf.add(types.InlineKeyboardButton('9 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792662'))
		inf.add(types.InlineKeyboardButton('10 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792663'))
		inf.add(types.InlineKeyboardButton('11 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792664'))
		inf.add(types.InlineKeyboardButton('12 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792665'))
		inf.add(types.InlineKeyboardButton('13 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792666'))
		inf.add(types.InlineKeyboardButton('14 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792667'))
		inf.add(types.InlineKeyboardButton('15 вариант', url='https://inf-oge.sdamgia.ru/test?id=18792668'))

		bot.reply_to(message, "<b>Информатика.</b> Выберите вариант",
		parse_mode='html', reply_markup=inf)




@bot.message_handler(commands=['немецкий', 'Немецкий', 'de'])
def de(message):
		de = types.InlineKeyboardMarkup()
		de.add(types.InlineKeyboardButton('1 вариант', url='https://de-oge.sdamgia.ru/test?id=74097'))
		de.add(types.InlineKeyboardButton('2 вариант', url='https://de-oge.sdamgia.ru/test?id=74098'))
		de.add(types.InlineKeyboardButton('3 вариант', url='https://de-oge.sdamgia.ru/test?id=74099'))
		de.add(types.InlineKeyboardButton('4 вариант', url='https://de-oge.sdamgia.ru/test?id=74100'))
		de.add(types.InlineKeyboardButton('5 вариант', url='https://de-oge.sdamgia.ru/test?id=74101'))

		bot.reply_to(message, "<b>Немецкий язык.</b> Выберите вариант",
		parse_mode='html', reply_markup=de)

@bot.message_handler(commands=['французский', 'Французский', 'fr'])
def fr(message):
		fr = types.InlineKeyboardMarkup()
		fr.add(types.InlineKeyboardButton('1 вариант', url='https://fr-oge.sdamgia.ru/test?id=56456'))
		fr.add(types.InlineKeyboardButton('2 вариант', url='https://fr-oge.sdamgia.ru/test?id=56457'))
		fr.add(types.InlineKeyboardButton('3 вариант', url='https://fr-oge.sdamgia.ru/test?id=56458'))
		fr.add(types.InlineKeyboardButton('4 вариант', url='https://fr-oge.sdamgia.ru/test?id=56459'))
		fr.add(types.InlineKeyboardButton('5 вариант', url='https://fr-oge.sdamgia.ru/test?id=56460'))

		bot.reply_to(message, "<b>Французский язык.</b> Выберите вариант",
		parse_mode='html', reply_markup=fr)

@bot.message_handler(commands=['испанский', 'Испанский', 'sp'])
def sp(message):
		sp = types.InlineKeyboardMarkup()
		sp.add(types.InlineKeyboardButton('1 вариант', url='https://sp-oge.sdamgia.ru/test?id=39978'))
		sp.add(types.InlineKeyboardButton('2 вариант', url='https://sp-oge.sdamgia.ru/test?id=39979'))
		sp.add(types.InlineKeyboardButton('3 вариант', url='https://sp-oge.sdamgia.ru/test?id=39980'))
		sp.add(types.InlineKeyboardButton('4 вариант', url='https://sp-oge.sdamgia.ru/test?id=39981'))
		sp.add(types.InlineKeyboardButton('5 вариант', url='https://sp-oge.sdamgia.ru/test?id=39982'))

		bot.reply_to(message, "<b>Испанский язык.</b> Выберите вариант",
		parse_mode='html', reply_markup=sp)

@bot.message_handler(commands=['физика', 'Физика', 'phys'])
def phys(message):
		phys = types.InlineKeyboardMarkup()
		phys.add(types.InlineKeyboardButton('1 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344214'))
		phys.add(types.InlineKeyboardButton('2 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344215'))
		phys.add(types.InlineKeyboardButton('3 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344216'))
		phys.add(types.InlineKeyboardButton('4 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344217'))
		phys.add(types.InlineKeyboardButton('5 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344218'))
		phys.add(types.InlineKeyboardButton('6 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344219'))
		phys.add(types.InlineKeyboardButton('7 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344220'))
		phys.add(types.InlineKeyboardButton('8 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344221'))
		phys.add(types.InlineKeyboardButton('9 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344222'))
		phys.add(types.InlineKeyboardButton('10 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344223'))
		phys.add(types.InlineKeyboardButton('11 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344224'))
		phys.add(types.InlineKeyboardButton('12 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344225'))
		phys.add(types.InlineKeyboardButton('13 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344226'))
		phys.add(types.InlineKeyboardButton('14 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344227'))
		phys.add(types.InlineKeyboardButton('15 вариант', url='https://phys-oge.sdamgia.ru/test?id=3344228'))

		bot.reply_to(message, "<b>Физика.</b> Выберите вариант",
		parse_mode='html', reply_markup=phys)

@bot.message_handler(commands=['химия', 'Химия', 'chem'])
def chem(message):
		chem = types.InlineKeyboardMarkup()
		chem.add(types.InlineKeyboardButton('1 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008138'))
		chem.add(types.InlineKeyboardButton('2 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008139'))
		chem.add(types.InlineKeyboardButton('3 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008140'))
		chem.add(types.InlineKeyboardButton('4 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008141'))
		chem.add(types.InlineKeyboardButton('5 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008142'))
		chem.add(types.InlineKeyboardButton('6 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008143'))
		chem.add(types.InlineKeyboardButton('7 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008144'))
		chem.add(types.InlineKeyboardButton('8 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008145'))
		chem.add(types.InlineKeyboardButton('9 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008146'))
		chem.add(types.InlineKeyboardButton('10 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008147'))
		chem.add(types.InlineKeyboardButton('11 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008148'))
		chem.add(types.InlineKeyboardButton('12 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008149'))
		chem.add(types.InlineKeyboardButton('13 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008150'))
		chem.add(types.InlineKeyboardButton('14 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008151'))
		chem.add(types.InlineKeyboardButton('15 вариант', url='https://chem-oge.sdamgia.ru/test?id=3008152'))

		bot.reply_to(message, "<b>Химия.</b> Выберите вариант",
		parse_mode='html', reply_markup=chem)

@bot.message_handler(commands=['биология', 'Биология', 'bio'])
def bio(message):
		bio = types.InlineKeyboardMarkup()
		bio.add(types.InlineKeyboardButton('1 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083137'))
		bio.add(types.InlineKeyboardButton('2 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083138'))
		bio.add(types.InlineKeyboardButton('3 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083139'))
		bio.add(types.InlineKeyboardButton('4 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083140'))
		bio.add(types.InlineKeyboardButton('5 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083141'))
		bio.add(types.InlineKeyboardButton('6 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083142'))
		bio.add(types.InlineKeyboardButton('7 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083143'))
		bio.add(types.InlineKeyboardButton('8 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083144'))
		bio.add(types.InlineKeyboardButton('9 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083145'))
		bio.add(types.InlineKeyboardButton('10 вариант', url='https://bio-oge.sdamgia.ru/test?id=308346'))
		bio.add(types.InlineKeyboardButton('11 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083147'))
		bio.add(types.InlineKeyboardButton('12 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083148'))
		bio.add(types.InlineKeyboardButton('13 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083149'))
		bio.add(types.InlineKeyboardButton('14 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083150'))
		bio.add(types.InlineKeyboardButton('15 вариант', url='https://bio-oge.sdamgia.ru/test?id=3083151'))

		bot.reply_to(message, "<b>Биология.</b> Выберите вариант",
		parse_mode='html', reply_markup=bio)

@bot.message_handler(commands=['география', 'География', 'geo'])
def geo(message):
		geo = types.InlineKeyboardMarkup()
		geo.add(types.InlineKeyboardButton('1 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414376'))
		geo.add(types.InlineKeyboardButton('2 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414377'))
		geo.add(types.InlineKeyboardButton('3 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414378'))
		geo.add(types.InlineKeyboardButton('4 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414379'))
		geo.add(types.InlineKeyboardButton('5 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414380'))
		geo.add(types.InlineKeyboardButton('6 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414381'))
		geo.add(types.InlineKeyboardButton('7 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414382'))
		geo.add(types.InlineKeyboardButton('8 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414383'))
		geo.add(types.InlineKeyboardButton('9 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414384'))
		geo.add(types.InlineKeyboardButton('10 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414385'))
		geo.add(types.InlineKeyboardButton('11 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414386'))
		geo.add(types.InlineKeyboardButton('12 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414387'))
		geo.add(types.InlineKeyboardButton('13 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414388'))
		geo.add(types.InlineKeyboardButton('14 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414389'))
		geo.add(types.InlineKeyboardButton('15 вариант', url='https://geo-oge.sdamgia.ru/test?id=2414390'))

		bot.reply_to(message, "<b>География.</b> Выберите вариант",
		parse_mode='html', reply_markup=geo)

@bot.message_handler(commands=['обществознание', 'Обществознание', 'soc'])
def soc(message):
		soc = types.InlineKeyboardMarkup()
		soc.add(types.InlineKeyboardButton('1 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809014'))
		soc.add(types.InlineKeyboardButton('2 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809015'))
		soc.add(types.InlineKeyboardButton('3 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809016'))
		soc.add(types.InlineKeyboardButton('4 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809017'))
		soc.add(types.InlineKeyboardButton('5 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809018'))
		soc.add(types.InlineKeyboardButton('6 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809019'))
		soc.add(types.InlineKeyboardButton('7 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809020'))
		soc.add(types.InlineKeyboardButton('8 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809021'))
		soc.add(types.InlineKeyboardButton('9 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809022'))
		soc.add(types.InlineKeyboardButton('10 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809023'))
		soc.add(types.InlineKeyboardButton('11 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809024'))
		soc.add(types.InlineKeyboardButton('12 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809025'))
		soc.add(types.InlineKeyboardButton('13 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809026'))
		soc.add(types.InlineKeyboardButton('14 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809027'))
		soc.add(types.InlineKeyboardButton('15 вариант', url='https://soc-oge.sdamgia.ru/test?id=4809028'))

		bot.reply_to(message, "<b>Обществознание.</b> Выберите вариант",
		parse_mode='html', reply_markup=soc)

@bot.message_handler(commands=['литература', 'Литература', 'lit'])
def lit(message):
		lit = types.InlineKeyboardMarkup()
		lit.add(types.InlineKeyboardButton('1 вариант', url='https://lit-oge.sdamgia.ru/test?id=237668'))
		lit.add(types.InlineKeyboardButton('2 вариант', url='https://lit-oge.sdamgia.ru/test?id=237669'))
		lit.add(types.InlineKeyboardButton('3 вариант', url='https://lit-oge.sdamgia.ru/test?id=237670'))
		lit.add(types.InlineKeyboardButton('4 вариант', url='https://lit-oge.sdamgia.ru/test?id=237671'))
		lit.add(types.InlineKeyboardButton('5 вариант', url='https://lit-oge.sdamgia.ru/test?id=237672'))
		lit.add(types.InlineKeyboardButton('6 вариант', url='https://lit-oge.sdamgia.ru/test?id=237673'))
		lit.add(types.InlineKeyboardButton('7 вариант', url='https://lit-oge.sdamgia.ru/test?id=237674'))
		lit.add(types.InlineKeyboardButton('8 вариант', url='https://lit-oge.sdamgia.ru/test?id=237675'))
		lit.add(types.InlineKeyboardButton('9 вариант', url='https://lit-oge.sdamgia.ru/test?id=237676'))
		lit.add(types.InlineKeyboardButton('10 вариант', url='https://lit-oge.sdamgia.ru/test?id=237677'))
		lit.add(types.InlineKeyboardButton('11 вариант', url='https://lit-oge.sdamgia.ru/test?id=237678'))
		lit.add(types.InlineKeyboardButton('12 вариант', url='https://lit-oge.sdamgia.ru/test?id=237679'))
		lit.add(types.InlineKeyboardButton('13 вариант', url='https://lit-oge.sdamgia.ru/test?id=237680'))
		lit.add(types.InlineKeyboardButton('14 вариант', url='https://lit-oge.sdamgia.ru/test?id=237681'))
		lit.add(types.InlineKeyboardButton('15 вариант', url='https://lit-oge.sdamgia.ru/test?id=237682'))

		bot.reply_to(message, "<b>Литература.</b> Выберите вариант",
		parse_mode='html', reply_markup=lit)

@bot.message_handler(commands=['история', 'История', 'hist'])
def hist(message):
		hist = types.InlineKeyboardMarkup()
		hist.add(types.InlineKeyboardButton('1 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002250'))
		hist.add(types.InlineKeyboardButton('2 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002251'))
		hist.add(types.InlineKeyboardButton('3 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002252'))
		hist.add(types.InlineKeyboardButton('4 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002253'))
		hist.add(types.InlineKeyboardButton('5 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002254'))
		hist.add(types.InlineKeyboardButton('6 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002255'))
		hist.add(types.InlineKeyboardButton('7 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002256'))
		hist.add(types.InlineKeyboardButton('8 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002257'))
		hist.add(types.InlineKeyboardButton('9 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002258'))
		hist.add(types.InlineKeyboardButton('10 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002259'))
		hist.add(types.InlineKeyboardButton('11 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002260'))
		hist.add(types.InlineKeyboardButton('12 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002261'))
		hist.add(types.InlineKeyboardButton('13 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002262'))
		hist.add(types.InlineKeyboardButton('14 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002263'))
		hist.add(types.InlineKeyboardButton('15 вариант', url='https://hist-oge.sdamgia.ru/test?id=1002264'))

		bot.reply_to(message, "<b>История.</b> Выберите вариант",
		parse_mode='html', reply_markup=hist)

@bot.message_handler(commands=['русскийязыкпис', 'Русскийязыкпис', 'rus'])
def rus(message):
		rus = types.InlineKeyboardMarkup()
		rus.add(types.InlineKeyboardButton('1 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815639'))
		rus.add(types.InlineKeyboardButton('2 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815640'))
		rus.add(types.InlineKeyboardButton('3 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815641'))
		rus.add(types.InlineKeyboardButton('4 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815642'))
		rus.add(types.InlineKeyboardButton('5 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815643'))
		rus.add(types.InlineKeyboardButton('6 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815644'))
		rus.add(types.InlineKeyboardButton('7 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815645'))
		rus.add(types.InlineKeyboardButton('8 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815646'))
		rus.add(types.InlineKeyboardButton('9 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815647'))
		rus.add(types.InlineKeyboardButton('10 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815648'))
		rus.add(types.InlineKeyboardButton('11 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815649'))
		rus.add(types.InlineKeyboardButton('12 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815650'))
		rus.add(types.InlineKeyboardButton('13 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815651'))
		rus.add(types.InlineKeyboardButton('14 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815652'))
		rus.add(types.InlineKeyboardButton('15 вариант', url='https://rus-oge.sdamgia.ru/test?id=11815653'))

		bot.reply_to(message, "<b>Русский язык (письменный экзамен).</b> Выберите вариант",
		parse_mode='html', reply_markup=rus)

@bot.message_handler(commands=['русскийязыкуст', 'Русскийязыкуст', 'ruso'])
def ruso(message):
		ruso = types.InlineKeyboardMarkup()
		ruso.add(types.InlineKeyboardButton('1 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704295'))
		ruso.add(types.InlineKeyboardButton('2 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704296'))
		ruso.add(types.InlineKeyboardButton('3 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704297'))
		ruso.add(types.InlineKeyboardButton('4 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704298'))
		ruso.add(types.InlineKeyboardButton('5 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704299'))
		ruso.add(types.InlineKeyboardButton('6 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704300'))
		ruso.add(types.InlineKeyboardButton('7 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704301'))
		ruso.add(types.InlineKeyboardButton('8 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704302'))
		ruso.add(types.InlineKeyboardButton('9 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704303'))
		ruso.add(types.InlineKeyboardButton('10 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704304'))
		ruso.add(types.InlineKeyboardButton('11 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704305'))
		ruso.add(types.InlineKeyboardButton('12 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704306'))
		ruso.add(types.InlineKeyboardButton('13 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704307'))
		ruso.add(types.InlineKeyboardButton('14 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704308'))
		ruso.add(types.InlineKeyboardButton('15 вариант', url='https://ruso-oge.sdamgia.ru/test?id=1704309'))

		bot.reply_to(message, "<b>Русский язык (устное собеседование).</b> Выберите вариант",
		parse_mode='html', reply_markup=ruso) 





print("Бот готов к работе!")
bot.polling(none_stop=True)