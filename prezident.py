import sys
import os
from colorama import Fore, Style, init as colorama_init

# Windows (cmd)
# py -m pip install -U colorama

import random

import time

from dataclasses import dataclass, field

colorama_autoreset = True   # цвет сбрасывается после каждого print

# ---------------- вложенные записи ----------------
@dataclass
class CitizenHealth:   # Больной ли житель?
    boli: float = 0.0
    prot: float = 0.0

@dataclass
class Citizens:        # Жители
    rab: float = 0.0
    brab: float = 0.0
    bol: CitizenHealth = field(default_factory=CitizenHealth)

@dataclass
class Zax:             # Закс
    n: bool = False
    k: float = 0.0

@dataclass
class Factories:       # Фабрика
    zav: float = 0.0
    fab: float = 0.0

# ---------------- основная запись TPlayer ---------------
@dataclass
class TPlayer:
    Name: str = ""
    Gold: float = 0.0
    Oil: float = 0.0
    Wars: float = 0.0
    Citizens: Citizens = field(default_factory=Citizens)
    Happiness: float = 0.0
    Infrastructure: float = 0.0
    SalaryFund: float = 0.0
    LastSalaryTurn: float = 0.0
    HasHospital: bool = False
    Zax: Zax = field(default_factory=Zax)
    MilitaryBases: float = 0.0
    SpyFunds: float = 0.0
    Factories: Factories = field(default_factory=Factories)
    ApocalypseMeter: float = 0.0

# ---------------- глобальные переменные -----------------
Player: TPlayer = TPlayer()

god: int = 0
mes: int = 0
den: int = 0
dd: int = 0
Action: int = 0
Action2: str = ""
t: float = 0.0
a: float = 0.0
b: float = 0.0
c: float = 0.0
GameOver: bool = False
ABC: float = 0.0
name: str = ""
voina: float = 0.0
ikran: float = 0.0
proth: float = 0.0
CorruptionLevel: float = 0.0   # 0-100
BlackMarket: float = 0.0       # 0-100
CrimeRate: float = 0.0         # 0-100
Win: bool = False
command: bool = False
WarsP: bool = False

# ---------- мелкие утилиты-заглушки ----------
def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

def delay(ms: int):
    time.sleep(ms / 1000)

def readkey() -> None:
    """Кросс-платформенное ожидание нажатия Enter."""
    input("Нажмите Enter для продолжения...")

# ---------- сама процедура ----------
def InitPlayer(player: TPlayer) -> None:
    global name, CorruptionLevel, Win, BlackMarket, CrimeRate, proth

    # 1. Приветствие
    print("Добро пожаловать в игру ПРЕЗИДЕНТ!")
    delay(1500)
    print("ПОЗДРАВЛЯЮ ВАС ИЗБРАЛИ ПРЕЗИДЕНТОМ")
    delay(1500)
    name = input("Представьтесь: ").strip()
    clrscr()

    # 2. Описание игры
    clrscr()
    print("=== Президент: Текстовая стратегическая игра ===\n")
    print("Президент — текстовая стратегическая игра, в которой вы становитесь главой государства.")
    print("Возглавьте страну, управляйте экономикой, обеспечьте благополучие граждан и защитите")
    print("государство от внутренних и внешних угроз.\n")

    print("Ключевые особенности игры:\n")

    print("- Управление экономикой:")
    print("  Развивайте промышленность, стройте фабрики и заводы, контролируйте бюджет.\n")

    print("- Социальное развитие:")
    print("  Стройте больницы, улучшайте инфраструктуру и повышайте уровень счастья граждан.\n")

    print("- Борьба с коррупцией:")
    print("  Выбирайте: вести честную политику или использовать коррупционные схемы.\n")

    print("- Контроль военной мощи:")
    print("  Создавайте военные базы, укрепляйте армию и защищайте свою страну от врагов.\n")

    print("- Тайные операции и разведка:")
    print("  Ведите шпионаж, выявляйте внутренние угрозы и проводите спецоперации.\n")

    print("- Влияние на население:")
    print("  Поддерживайте социальную стабильность, предотвращайте протесты и мятежи.\n")

    print("- Борьба с апокалипсисом:")
    print("  Снижайте угрозу глобального краха, реагируйте на катастрофы и кризисы.\n")

    print("Подсказки перед стартом:")
    print("* Управляй экономикой с умом: не вкладывай все ресурсы в одну область.")
    print("* Держи армию в боеготовности: внешние угрозы могут появиться неожиданно.")
    print("* Следи за уровнем счастья: недовольные граждане могут устроить бунт.")
    print("* Контролируй коррупцию: чем выше её уровень, тем больше проблем в стране.")
    print("* Реагируй на кризисы оперативно: природные катастрофы могут обрушить экономику.")
    print("* Не забывай о больницах: без них люди начинают погибать, снижая численность и счастье населения.")
    print("* Строй больницы и загсы: без больницы загс не может функционировать.\n")
    print("Готов стать лидером нации? Докажи, что можешь править и сохранить страну!\n")
    print("Нажмите любую клавишу, чтобы продолжить...")
    readkey()
    clrscr()

    # 3. Начальные значения глобальных переменных
    CorruptionLevel = 30.0
    Win = False
    BlackMarket = 20.0
    CrimeRate = 40.0
    proth = 20.0

    # 4. Начальные значения полей Player
    player.Name = name
    player.Gold = 2000.0
    player.Oil = 100.0
    player.Wars = 0.0
    player.Citizens.rab = 0.0
    player.Citizens.brab = 500.0
    player.Citizens.bol.prot = 0.0
    player.Happiness = 100.0
    player.Infrastructure = 0.0
    player.LastSalaryTurn = 0.0
    player.HasHospital = False
    player.Zax.n = False
    player.Zax.k = 0.0
    player.MilitaryBases = 0.0
    player.SpyFunds = 250.0
    player.Factories.fab = 0.0
    player.Factories.zav = 0.0
    player.ApocalypseMeter = 0.0

# ---------- Winer ----------
def Winer(player: TPlayer) -> None:
    global Win
    if (player.Gold > 1_000_000 and
        player.Oil > 1_000_000 and
        (player.Citizens.brab + player.Citizens.rab) > 1_000_000 and
        player.Happiness >= 100):
        Win = True

# ---------- Corruption ----------
def Corruption() -> None:
    global CorruptionLevel
    print("Коррупционный скандал! Чиновник пойман на взятке.")
    print("1 - Наказать по закону")
    print("2 - Закрыть глаза")
    choice = input().strip()

    if choice == "1":
        CorruptionLevel -= 10
        print("Чиновник уволен и посажен в тюрьму.")
    else:
        CorruptionLevel += 10
        print("Вы закрыли глаза на коррупцию. Она усиливается.")
    print()

# ---------- BlackMarketGrowth ----------
def BlackMarketGrowth() -> None:
    global BlackMarket
    BlackMarket += random.randint(1, 5)   # +1..5 %
    print(f"Черный рынок растет. Текущий уровень: {BlackMarket:.0f}%")
    if BlackMarket > 50:
        print("Нелегальная экономика начинает подрывать официальную.")
    print()

# ---------- AntiCrimeOperation ----------
def AntiCrimeOperation() -> None:
    global CrimeRate, BlackMarket, CorruptionLevel, a
    print("Вы начали спецоперацию против преступности...")
    success_chance = random.randint(0, 99)

    if success_chance > CrimeRate and success_chance > BlackMarket:
        print("Операция успешна! Уровень преступности снижен.")
        a = random.randint(0, 20)
        CrimeRate -= a
        a = random.randint(0, 20)
        BlackMarket -= a
        a = random.randint(0, 20)
        CorruptionLevel -= a
    else:
        print("Операция провалена. Преступники ушли от наказания.")
        a = random.randint(0, 20)
        CrimeRate += a
        BlackMarket += a

# ---------- мелкие утилиты ----------
def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

def delay(ms: int):
    time.sleep(ms / 1000)

def textcolor(code: int):
    """Только для совместимости: 2-зелёный, 10-светло-зелёный, 15-белый"""
    colors = {2: Fore.GREEN, 10: Fore.LIGHTGREEN_EX, 15: Fore.WHITE}
    print(colors.get(code, ''), end='')

# ---------- PrintPlayerInfo ----------
def PrintPlayerInfo(player: TPlayer) -> None:
    textcolor(2)
    delay(10)
    print('==================================================')
    delay(10)
    print('             ГОСУДАРСТВЕННЫЕ ДАННЫЕ                ')
    delay(10)
    textcolor(10)
    print('==================================================')
    delay(10)
    print(f'Господин президент:                 {player.Name}')
    delay(10)
    print(f'Время правления            {god} год, {mes} месяцев, {den} дней')
    delay(10)

    if t / 9 > 4:
        print(f'Выплата зарплат через {9 - (t / 9):3.0f} ходов.')
    if t > 1 and t / 9 <= 0:
        print('После этого хода выплата зарплат.')
    print('--------------------------------------------------')
    delay(10)
    textcolor(2)
    print(f'  | Казна:                 {player.Gold:7.0f} $       Постоянная сумма для налога к 1 жителю:     {b:6.0f} $')
    delay(10)
    print(f'  | Полезные ископаемые:   {player.Oil:7.0f} тонн     Общая сумма налога:                      {b * (player.Citizens.brab + player.Citizens.rab):6.0f} $')
    delay(10)
    print(f'  | Количество войн:       {player.Wars:3.0f}', end='')
    if voina > 0 and voina > t and WarsP:
        print(f'                    Война начнется через {voina - t} ходов.')
    elif voina == t and t > 1:
        print('После этого хода на вас нападут.')
    else:
        print()

    delay(10)
    print(f'   |Уровень коррупции:              {CorruptionLevel:3.0f}')
    print(f'   |Развитие нелегальной экономики: {BlackMarket:3.0f}')
    print(f'   |Уровень преступности:           {CrimeRate:3.0f}')
    print()
    delay(10)
    total_pop = player.Citizens.brab + player.Citizens.rab
    print(f'  | Жители:                {total_pop:7.0f}        Постоянная сумма для зарплат к 1 рабочему:  {b + 10:6.0f} $')
    print(f'   | Рабочих              {player.Citizens.rab:7.0f}          Общая сумма зарплат:                     {(b / 0.1) * player.Citizens.rab:6.0f} $')
    print(f'   | Безработных          {player.Citizens.brab:7.0f}')
    print(f'     | Больные            {player.Citizens.bol.boli:7.0f}')
    print(f'     | Процент больных    {player.Citizens.bol.prot:3.0f} %')
    print()
    delay(10)
    print(f'  | Счастье жителей:       {player.Happiness:3.0f} %')
    delay(10)
    print(f'  | Инфраструктура:        {player.Infrastructure:3.0f}')
    delay(10)
    print(f'  | Военные базы:          {player.MilitaryBases:3.0f}')
    delay(10)
    print(f'  | Шпионский фонд:        {player.SpyFunds:5.0f} $')
    delay(10)
    print(f'  | Заводы:                {player.Factories.zav:3.0f}')
    print(f'  | Фабрики:               {player.Factories.fab:3.0f}')
    delay(10)
    print(f'  | Уровень апокалипсиса:  {player.ApocalypseMeter:3.0f} %')
    delay(10)
    print('==================================================')
    delay(10)

# ---------- BuildMilitaryBase ----------
def BuildMilitaryBase(player: TPlayer) -> None:
    base_cost = 650.0
    if player.Gold >= base_cost:
        player.Gold -= base_cost
        player.MilitaryBases += 1
        print('Военная база построена! Снижение потерь в войне на 5%.')
    else:
        print('Недостаточно $ в казне для строительства военной базы!')

# ---------- StartWar ----------
def StartWar(player: TPlayer) -> None:
    print('Вы объявили войну!')
    if player.Gold >= 200 and player.Oil >= 100:
        player.Wars += 1
        player.Happiness -= 25
        print('Война состоялась!')
    else:
        print('Недостаточно ресурсов для войны!')

# ---------- MakeTrade ----------
def MakeTrade(player: TPlayer) -> None:
    print('1. Обмен $ на полезные ископаемые (20 $ = 1 полезные ископаемые)')
    print('2. Обмен полезные ископаемые в $ (1 полезные ископаемые = 20 $)')
    choice = input().strip()
    if choice == '1':
        print('Сколько $ в казне обменять на полезные ископаемые? (Обменяются все 20)')
        amount = float(input())
        if player.Gold >= amount:
            player.Gold -= amount
            player.Oil += amount / 20
            print('Успешно обменяли $ на полезные ископаемые!')
        else:
            print('Недостаточно $ в казне!')
    elif choice == '2':
        print('Сколько полезных ископаемых обменять в $?')
        amount = float(input())
        if player.Oil >= amount:
            player.Oil -= amount
            player.Gold += amount * 20
            print('Успешно обменяли полезные ископаемые в $!')
        else:
            print('Недостаточно полезных ископаемых!')

# ---------- CollectTaxes ----------
def CollectTaxes(player: TPlayer) -> None:
    global b
    tax_amount = b
    player.Gold += tax_amount * (player.Citizens.brab + player.Citizens.rab)
    player.Happiness -= 15
    print('Вы собрали налоги!')
    print()
    
# ---------- BuildInfrastructure ----------
def BuildInfrastructure(player: TPlayer) -> None:
    global a          # используем как рабочую переменную
    build = True

    print('Доступные виды инфраструктуры:')
    print('1. Школы (Стоимость: 500 $, +счастье, +жители, 3 % рабочих от общего кол-ва)')
    print('2. Аэропорты (Стоимость: 800 $, +счастье, +жители, 2 % рабочих)')
    print('3. Заводы (Стоимость: 700 $, +250 рабочих, +100-5000 $ в казну)')
    print('4. Фабрики (Стоимость: 30 нефти, +100 рабочих, +50-200 $, +10-500 нефти)')
    print('5. ЗАГС (Стоимость: 600 $, +жители, 1 % рабочих)')
    print('6. Больницы (Стоимость: 600 $, +счастье, 3 % рабочих)')
    choice = input('Выберите инфраструктуру для строительства (1-6): ').strip()

    # ---------- 1. Школы ----------
    if choice == '1':
        if player.Gold >= 500:
            a = (player.Citizens.brab + player.Citizens.rab) * 0.03
            if player.Citizens.brab >= a:
                player.Citizens.brab -= a
                player.Citizens.rab += a
            else:
                build = False

            if build:
                player.Gold -= 500
                player.Infrastructure += 1
                player.Citizens.brab += 200
                player.Citizens.rab += 30
                player.Happiness += 10
                print('Вы построили Школу! Счастье увеличилось, и количество жителей выросло.')
            else:
                print('Не достаточно безработных жителей.')
        else:
            print('Недостаточно $ в казне для строительства Школы!')

    # ---------- 2. Аэропорты ----------
    elif choice == '2':
        if player.Gold >= 800:
            a = (player.Citizens.brab + player.Citizens.rab) * 0.02
            if player.Citizens.brab >= a:
                player.Citizens.brab -= a
                player.Citizens.rab += a
            else:
                build = False

            if build:
                player.Gold -= 800
                player.Infrastructure += 1
                player.Citizens.brab += 150
                player.Citizens.rab += 300
                player.Happiness += 15
                print('Вы построили Аэропорт! Счастье увеличилось, и количество жителей немного выросло.')
            else:
                print('Не достаточно безработных жителей.')
        else:
            print('Недостаточно $ в казне для строительства Аэропорта!')

    # ---------- 3. Заводы ----------
    elif choice == '3':
        if player.Gold >= 700:
            if player.Citizens.brab >= 300:
                player.Citizens.brab -= 300
                player.Citizens.rab += 300
                player.Factories.zav += 1
                player.Gold -= 700
                player.Infrastructure += 1
                print(f'Завод построен! Теперь у вас {player.Factories.zav} заводов и {player.Factories.fab} фабрик.')
            else:
                print('Не достаточно безработных жителей.')
        else:
            print('Недостаточно $ в казне для строительства Завода!')

    # ---------- 4. Фабрики ----------
    elif choice == '4':
        if player.Oil >= 30 and player.Citizens.brab >= 100:
            player.Oil -= 30
            player.Citizens.brab -= 100
            player.Citizens.rab += 100
            player.Factories.fab += 1
            if player.Citizens.bol.boli > 9:
                player.Citizens.bol.boli -= 10
            print(f'Фабрика построена! Теперь у вас {player.Factories.zav} заводов и {player.Factories.fab} фабрик.')
        else:
            print('Недостаточно ресурсов для постройки фабрики.')

    # ---------- 5. ЗАГС ----------
    elif choice == '5':
        a = (player.Citizens.brab + player.Citizens.rab) * 0.01
        if player.Citizens.brab >= a:
            player.Citizens.brab -= a
            player.Citizens.rab += a
        else:
            build = False

        if build:
            if player.Gold >= 600:
                player.Gold -= 600
                player.Zax.k += 1
                player.Infrastructure += 1
                player.Zax.n = True
                player.Happiness += 20
                print('Вы построили ЗАГС! Счастье жителей увеличилось.')
            else:
                print('Недостаточно $ в казне для строительства ЗАГС!')
        else:
            print('Не достаточно безработных жителей!')

    # ---------- 6. Больницы ----------
    elif choice == '6':
        if player.Gold >= 600:
            a = (player.Citizens.brab + player.Citizens.rab) * 0.03
            if player.Citizens.brab >= a:
                player.Citizens.brab -= a
                player.Citizens.rab += a
            else:
                build = False

            if build:
                player.Gold -= 600
                player.Infrastructure += 1
                player.HasHospital = True
                player.Happiness += 20
                player.Citizens.bol.prot -= 10
                print('Вы построили Больницу! Счастье жителей увеличилось.')
            else:
                print('Не достаточно безработных жителей.')
        else:
            print('Недостаточно $ в казне для строительства Больницы!')

    else:
        print('Неверный выбор!')

# ---------- PaySalaries ----------
def PaySalaries(player: TPlayer) -> None:
    global b
    salary_per_citizen = b
    total_salary = (salary_per_citizen / 0.1) * player.Citizens.rab

    if total_salary <= player.Gold:
        player.Gold -= total_salary
        player.Happiness += 25
        print('Зарплаты успешно выплачены! Жители довольны.')
    else:
        player.Happiness -= 50
        player.Gold -= total_salary
        print('Недостаточно средств для выплаты зарплат! Жители недовольны.')
    print()

import random
import sys

# ---------- NegotiatePeace ----------
def NegotiatePeace(player: TPlayer) -> None:
    if player.Wars > 0:
        negotiation_chance = random.randint(0, 99)  # 0..99
        if negotiation_chance < 50:                 # 50 % шанс
            print('Переговоры прошли успешно! Заключено мирное соглашение с противником.')
            player.Wars -= 1
        else:
            print('Переговоры не удались. Придётся продолжать войну!')
    else:
        print('В данный момент нет действующей войны.')

# ---------- NaturalDisaster ----------
def NaturalDisaster(player: TPlayer) -> None:
    print('Произошло стихийное бедствие! Вы потеряли 50 % казны и 30 % полезных ископаемых.')
    player.Gold *= 0.5
    player.Oil  *= 0.7
    print()

# ---------- EnemySpy ----------
def EnemySpy(player: TPlayer) -> None:
    if random.randint(0, 99) < 80:          # 80 %
        print('Вражеские шпионы украли 15 % казны и 5 % нефти!')
        player.Gold *= 0.85
        player.Oil  *= 0.95
        print()

# ---------- Elections ----------
def Elections(player: TPlayer) -> None:
    print('Прошли выборы!')
    if player.Happiness < 50:
        if random.randint(0, 99) > 25:      # 75 % проигрыша
            print('Вы проиграли выборы из-за низкого счастья! Игра окончена.')
            sys.exit()
        else:
            print('Вы были переизбраны, но счастье жителей слишком низкое. В следующий раз вас могут не переизбрать.')
    elif player.Happiness > 50:
        print('Вы переизбраны! Продолжайте править.')
    print()

# ---------- Crisis ----------
def Crisis(player: TPlayer) -> None:
    print('Произошёл экономический кризис! Вы потеряли 3000 $ из казны и 800 полезных ископаемых.')
    player.Gold -= 3000
    player.Oil  -= 800
    print()

# ---------- Popolnenie ----------
def Popolnenie() -> None:
    global Player
    money = float(input('Введите сумму для финансирования разведки: '))
    if Player.Gold < money:
        print('Недостаточно средств.')
    else:
        Player.SpyFunds += money
        Player.Gold     -= money

# ---------- Atack ----------
def Atack(player: TPlayer) -> None:
    global proth, Action, a
    a = random.randint(0, 3)          # 0..3 → 1..4
    print('Выберите направление, с которого хотите ударить по врагу:')
    print('  1. Север.')
    print('  2. Юг.')
    print('  3. Запад.')
    print('  4. Восток.')
    Action = int(input())

    if Action == a + 1:               # попали в тыл
        print('Вы атаковали врага в тыл.')
        print('Шанс победы увеличился на 5 процентов.')
        proth += 5
    elif Action == a or Action == a + 2:  # рядом
        print('Вы нанесли удар по инфраструктуре и военным базам противника.')
        a = random.randint(1, 2)
        print(f'Шанс победы увеличился на {a} %')
        proth += a
    else:
        print('Вы не смогли нанести удар по врагу.')

# ---------- comand ----------
def comand() -> None:
    global Player, command, Win, dd, proth
    print('Командная строка запущена.')
    if not command:
        print('Командная строка не может быть активирована, т.к. выключен командный режим.')
        return

    cmd = input('Введите команду: ').strip()
    if cmd == 'build':
        print('Введите ID-код постройки.')
        sub = input().strip()
        if sub == '1':          # Школа
            Player.Infrastructure += 1
            Player.Citizens.brab += 200
            Player.Citizens.rab += 30
            Player.Happiness += 10
            print('Вы построили Школу! Счастье увеличилось, и количество жителей выросло.')
        elif sub == '2':        # Больница
            Player.Infrastructure += 1
            Player.HasHospital = True
            Player.Happiness += 20
            Player.Citizens.bol.prot -= 10
            print('Вы построили Больницу! Счастье жителей увеличилось.')
        elif sub == '3':        # Завод
            Player.Factories.zav += 1
            Player.Infrastructure += 1
            print(f'Завод построен! Теперь у вас {Player.Factories.zav} заводов и {Player.Factories.fab} фабрик.')
        elif sub == '4':        # Аэропорт
            Player.Infrastructure += 1
            Player.Happiness += 15
            print('Вы построили Аэропорт! Счастье увеличилось, и количество жителей немного выросло.')
        elif sub == '5':        # Фабрика
            Player.Factories.fab += 1
            print(f'Фабрика построена! Теперь у вас {Player.Factories.zav} заводов и {Player.Factories.fab} фабрик.')
        elif sub == '6':        # ЗАГС
            Player.Zax.k += 1
            Player.Infrastructure += 1
            Player.Zax.n = True
            print('Вы построили ЗАГС! Счастье жителей увеличилось.')
        else:
            print('Неверный ID постройки.')

    elif cmd == 'give':
        sub = input('Введите ID для выдачи: ').strip()
        if sub == 'Gold':
            Player.Gold += 100_000
        elif sub == 'Oil':
            Player.Oil += 100_000
        elif sub == 'Villager':
            Player.Citizens.brab += 100_000
        elif sub == 'Inf':
            Player.Infrastructure += 100
        elif sub == 'Wars':
            Player.Wars = 0
        elif sub == 'dd':
            dd = 250
        elif sub == 'rab':
            Player.Citizens.rab += 500
        elif sub == 'Win':
            Win = True
        else:
            print('Неверный код.')

# ---------- vd (военные действия) ----------
def vd(player: TPlayer) -> None:
    global proth, Action2
    if player.Wars < 1:
        print('Неверный выбор.')
        return

    print('Выберите действие:')
    print(' 1. Атаковать противника.')
    print(' 2. Усилить армию. (-500 $, -250 нефти, -300 $ из шпионского фонда)')
    Action2 = input().strip()

    if Action2 == '1':
        Atack(player)
    elif Action2 == '2':
        if player.Gold > 499 and player.Oil > 249 and player.SpyFunds > 299:
            player.Gold -= 500
            player.Oil -= 250
            player.SpyFunds -= 300
            proth += 5
            print('Сила армий +5 %, шанс победы +5 %, потери в войне на 3 % меньше.')
        else:
            print('Недостаточно средств.')
    else:
        print('Неверный выбор.')

# -------------------  ГЛАВНЫЙ ЦИКЛ  -------------------
def main() -> None:
    global Player, name, god, mes, den, dd, t, b, voina, proth
    global GameOver, Win, command, ikran, WarsP, Action, Action2
    global a, c, ABC, CorruptionLevel, BlackMarket, CrimeRate

    # === стартовая инициализация ===
    # SetWindowTitle('ПРЕЗИДЕНТ')   # опционально, если нужно
    Player.Citizens.bol.boli = 0.0
    Player.Citizens.bol.prot = 0.0
    random.seed()
    voina   = 0.0
    t       = 0
    GameOver= False
    Win     = False
    b       = 1.0
    command = False
    dd      = 0
    ikran   = 0.0
    WarsP   = False

    InitPlayer(Player)          # наша переведённая процедура
    textcolor(15)
    clrscr()

    # === игровой цикл ===
    while not GameOver and not Win:
        # ---- болезни свыше 100 % ----
        if Player.Citizens.bol.prot > 100:
            a = Player.Citizens.bol.prot - 100
            Player.Citizens.bol.prot -= a
            a = (Player.Citizens.brab + Player.Citizens.rab) / a
            if Player.Citizens.brab >= a:
                Player.Citizens.brab -= a
            elif Player.Citizens.rab >= a:
                Player.Citizens.rab -= a
            else:
                print('Вы проиграли! Все люди умерли из-за болезней.')
                GameOver = True

        # ---- пересчёт больных ----
        a = Player.Citizens.rab + Player.Citizens.brab
        if Player.Citizens.bol.prot > 0:
            Player.Citizens.bol.boli = (a / 100) * Player.Citizens.bol.prot
        else:
            Player.Citizens.bol.boli = 0.0

        Player.Name = name
        god = dd // 108
        mes = (dd // 9) % 12
        if mes == 0: mes = 12
        den = (dd % 9) * 3
        if den == 0: den = 1
        if t == 0: den = 1

        if Player.Citizens.brab < 0 and Player.Citizens.rab < 0:
            print('Вы проиграли! Все жители погибли! Следующий ход вас не спасёт!')
            time.sleep(0.2)
        Player.Citizens.brab = max(Player.Citizens.brab, 0)
        Player.Citizens.rab  = max(Player.Citizens.rab,  0)

        # ---- печать статуса ----
        PrintPlayerInfo(Player)

        # ---- меню ----
        textcolor(10)
        print('                  ВЫБЕРИТЕ ДЕЙСТВИЕ               ')
        delay(10)
        print('==================================================')
        delay(10)
        print('1.  Объявить войну')
        delay(10)
        print('2.  Сделать обмен')
        delay(10)
        print('3.  Построить военную базу (650 $)')
        delay(10)
        print('4.  Финансирование разведки')
        delay(10)
        print('5.  Переговоры о мире')
        delay(10)
        print('6.  Построить инфраструктуру')
        delay(10)
        print('7.  Изменить постоянную сумму для налога (0<налог<500)')
        delay(10)
        if Player.Wars > 0:
            print('8.   Военные действия')
        delay(10)
        if (CrimeRate > 50) or (BlackMarket > 50) or (CorruptionLevel > 60):
            print('9. Провести спец-операцию')
        delay(10)
        print('0.  Закончить ход')
        print()
        print('  -1. Очистить экран')
        delay(10)
        print('  -2. Сменить имя')
        delay(10)
        print('--------------------------------------------------')
        textcolor(10)
        Action2 = input().strip()
        delay(10)
        textcolor(2)
        print('==================================================')
        delay(10)

        # ---- обработка выбора ----
        if Action2 == '/':
            comand()
        elif Action2 == 'command':
            command = True
        elif Action2 == '1':
            StartWar(Player)
        elif Action2 == '2':
            MakeTrade(Player)
        elif Action2 == '3':
            BuildMilitaryBase(Player)
        elif Action2 == '4':
            Popolnenie()
        elif Action2 == '5':
            NegotiatePeace(Player)
        elif Action2 == '6':
            BuildInfrastructure(Player)
        elif Action2 == '7':
            if den != 3:
                while True:
                    try:
                        bb = float(input('Введите постоянную сумму для налога (0<налог<500): '))
                        if 0 < bb < 500:
                            b = bb
                            print('Сохранено.')
                            input()          # пауза
                            break
                        else:
                            print('Должно быть больше 0 и меньше 500.')
                    except ValueError:
                        pass
            else:
                print('В данный момент вы не можете этого сделать.')
        elif Action2 == '8':
            vd(Player)
        elif Action2 == '9':
            if (CrimeRate > 50) or (BlackMarket > 50) or (CorruptionLevel > 60):
                AntiCrimeOperation()
            else:
                print('Вы ввели неизвестное значение.')
        elif Action2 == '-1':
            ikran = 1
        elif Action2 == '-2':
            name = input('Введите новое имя: ').strip()
            clrscr()
            print('Сохранено.')
        else:
            print('Ваш ход завершён!')

        print('==================================================')
        print()

        # ===== пост-ходовые события =====
        # ---- доход от фабрик ----
        if player.Factories.fab > 0 and random.randint(0, 99) > 39:
            a = random.randint(150, 300)          # 150-300
            player.Gold += a * player.Factories.fab
            a = random.randint(0, 99) * 10
            player.Oil += a * player.Factories.fab

        # ---- доход от заводов ----
        if player.Factories.zav > 0 and random.randint(0, 99) > 39:
            a = random.randint(0, 9) * 1250
            player.Gold += a * player.Factories.zav

        if dd > 5:
            # ---- болезни ----
            if t > 10 and random.randint(0, 99) > 69:
                a = random.randint(0, 14)
                player.Citizens.bol.prot += a

            if random.randint(0, 99) > 85: Corruption()
            if random.randint(0, 99) > 80: BlackMarketGrowth()

            if random.randint(0, 99) > 69 and player.Citizens.bol.prot > 19:
                a = random.randint(0, 19)
                player.Citizens.bol.prot -= a
                a = (player.Citizens.brab + player.Citizens.rab) / max(a, 1)
                if player.Citizens.brab >= a:
                    player.Citizens.brab -= a
                elif player.Citizens.rab >= a:
                    player.Citizens.rab -= a
                else:
                    print('Вы проиграли! Все люди умерли из-за болезней.')
                    GameOver = True

            a = random.randint(2, 9)
            if random.randint(0, 99) > 40:
                player.Citizens.bol.prot += a

            # ---- последствия отсутствия больниц ----
            if not player.HasHospital:
                if random.randint(0, 99) > 20:
                    a = random.randint(0, 7)
                    print(f'Из-за отсутствия больниц % больных увеличился на {a} %')
                    player.Citizens.bol.prot += a
                    a = random.randint(0, 49)
                    if player.Citizens.brab > a:
                        player.Citizens.brab -= a
                        print(f'Из-за отсутствия больниц умерло {a} человек.')
                    elif player.Citizens.rab > a:
                        player.Citizens.rab -= a
                        print(f'Из-за отсутствия больниц умерло {a} человек.')
                    else:
                        print('Вы проиграли! Все люди умерли из-за болезней.')
                        GameOver = True
                    print()

            # ---- лечение в больницах ----
            if player.HasHospital and random.randint(0, 99) > 59:
                a = random.randint(0, 9)
                if player.Citizens.bol.prot >= a:
                    player.Citizens.bol.prot -= a

            # ---- прирост населения при ЗАГС + больница ----
            if player.HasHospital and player.Zax.n:
                c = random.randint(0, 39)
                if player.Zax.k / 5 > 0:
                    player.Citizens.brab += c * (player.Zax.k / 5)
                else:
                    player.Citizens.brab += c

            # ---- зарплаты и налоги ----
            if mes > 0 and den == 1:
                PaySalaries(Player)
            if dd % 9 == 8:
                CollectTaxes(Player)
            if god > 0 and mes == 0 and den == 0:
                Elections(Player)

            # ---- случайные катастрофы ----
            if t > 5 and random.randint(0, 99) <= 15:
                ABC = random.randint(1, 3)
                if ABC == 1: EnemySpy(Player)
                elif ABC == 2: NaturalDisaster(Player)
                elif ABC == 3: Crisis(Player)

            # ---- разведка о будущей войне ----
            if voina == 0 and t > 5 and random.randint(0, 99) <= 10:
                a = random.randint(0, 29)
                if a < 10: a = 10
                if Player.SpyFunds >= 250:
                    WarsP = True
                    print(f'Шпионы узнали, что враг нападёт через {a} дней')
                    Player.SpyFunds -= 250
                    print()
                voina = t + a

            # ---- начало войны ----
            if t > 0 and voina == t:
                voina = 0
                WarsP = False
                Player.Wars += 1
                Player.Happiness -= 25
                print('На вас напали.')
                print()

            # ---- исход войны ----
            if Player.Wars > 0:
                if random.randint(0, 99) < proth + 1:
                    print('Вы победили в войне')
                    Player.Wars -= 1
                    Player.Gold += 15000
                    Player.Oil += 1500
                    Player.Citizens.brab += 50
                    print()
                elif random.randint(0, 99) > 79:
                    print('Вам предлагают мирный договор с условиями:')
                    print('Снос всех военных баз обеих сторон.')
                    print('+1000 $ в казну.')
                    print('-500 полезных ископаемых.')
                    print('Вы согласны на условие? Если ДА — введите 1, если НЕТ — 2.')
                    Action = int(input())
                    if Action == 1:
                        Player.Wars -= 1
                        Player.Gold += 1000
                        Player.Oil -= 500
                        Player.Happiness += 15
                        Player.MilitaryBases = 0
                        print('Вы подписали мирный договор')
                    else:
                        print('Вы отказались подписывать договор.')
                        Player.Happiness -= 15
                    print()
                elif Player.Gold < 500 and Player.Oil < 500 and Player.Happiness < 50:
                    if random.randint(0, 99) > 69:
                        print('Вам предлагают мирный договор с условиями:')
                        print('Снос всех военных баз.')
                        print('-1000 $ из казны.')
                        print('-500 полезных ископаемых.')
                        print('Вы согласны на условие? Если ДА — 1, если НЕТ — 2.')
                        Action = int(input())
                        if Action == 1:
                            Player.Wars -= 1
                            Player.Gold += 1000
                            Player.Oil -= 500
                            Player.Happiness += 5
                            Player.MilitaryBases = 0
                            print('Вы подписали мирный договор')
                        else:
                            print('Вы отказались подписывать договор.')
                            Player.Happiness -= 25
                        print()

                # ---- ежеходные потери от войны ----
                Player.Happiness -= 3
                if Player.Gold > 400 or Player.Oil > 400:
                    a = random.randint(0, 399)
                    if Player.MilitaryBases > 0:
                        a = a / (5 * Player.MilitaryBases)
                    print(f'Из-за войн вы потеряли {a * Player.Wars:.0f} $ из казны')
                    Player.Gold -= a * Player.Wars

                    a = random.randint(0, 399)
                    if Player.MilitaryBases > 0:
                        a = a / (5 * Player.MilitaryBases)
                    print(f'Из-за войн вы потеряли {a * Player.Wars:.0f} тонн полезных ископаемых')
                    Player.Oil -= a * Player.Wars

                    a = random.randint(0, 39)
                    if Player.MilitaryBases > 0:
                        a = a / (5 * Player.MilitaryBases)
                    if Player.Citizens.brab >= a:
                        Player.Citizens.brab -= a * Player.Wars
                    elif Player.Citizens.rab >= a:
                        Player.Citizens.rab -= a * Player.Wars
                    else:
                        print('Вы проиграли! ВСЕ ЛЮДИ ПОГИБЛИ!')
                        GameOver = True
                    if not GameOver:
                        print(f'Из-за войн вы потеряли {a * Player.Wars:.0f} жителей')

                    if random.randint(0, 99) > 39:
                        if Player.MilitaryBases > 0:
                            if Player.MilitaryBases == 1:
                                a = 1
                                Player.MilitaryBases = 0
                            elif Player.MilitaryBases == 2:
                                a = random.randint(0, 1)
                                Player.MilitaryBases -= a
                            else:
                                a = random.randint(0, 2)
                                Player.MilitaryBases -= a
                            print(f'Из-за войн вы потеряли {a} военных баз.')
                else:
                    print('Вы проиграли, ваша страна была уничтожена в войнах.')
                    GameOver = True
                print()

            # ---- бунты по счастью ----
            if Player.Happiness < 6:
                print('Жители недовольны! Счастье жителей слишком низкое...')
                a = random.randint(0, 4) * 100
                Player.Citizens.brab -= a
                print(f'Вы потеряли {a} жителей!')
                print()

            # ---- конец ресурсов ----
            if (Player.Gold <= 0 and Player.Oil <= 0) or (Player.Citizens.brab <= 0 and Player.Citizens.rab <= 0):
                print('Вы проиграли! Все ресурсы исчерпаны.')
                GameOver = True

            # ---- коррупция ----
            if CorruptionLevel > 60 and random.randint(0, 99) > 59:
                print('Кто-то стал воровать $ из казны.')
                if CorruptionLevel < 71:
                    Player.Gold -= 200
                elif CorruptionLevel < 81:
                    Player.Gold -= 1000
                elif CorruptionLevel < 91:
                    Player.Gold -= 1500
                else:
                    Player.Gold -= 2500
                a = random.randint(0, 4)
                CorruptionLevel += a
                print()

            # ---- преступность ----
            if CrimeRate > 30:
                if random.randint(0, 99) > 81:
                    a = random.randint(0, 99)
                    if a < 11:
                        a = random.randint(0, 49)
                        print(f'Преступники напали на полицию. Умерло {a} человек.')
                        Player.Citizens.rab -= a
                        a = random.randint(0, 4)
                        CrimeRate += a
                        print()
                    if a < 21:
                        a = random.randint(0, 49)
                        print('Преступники ограбили банк:')
                        print(f' Погибло {a} человек,')
                        Player.Citizens.brab -= a / 3
                        Player.Citizens.rab -= (a / 3) * 2
                        a = random.randint(0, 4999)
                        Player.Gold -= a
                        print(f' Украли {a} из казны.')
                        a = random.randint(0, 4)
                        CrimeRate += a
                        print()

        # ---- очистка экрана ----
        if ikran == 1:
            print(' Экран очистится, нажмите Enter.')
            input()
            clrscr()
            ikran = 0

        # ---- проверка победы ----
        Winer(Player)

        t += 1
        dd += 1
        print('Ход завершён. НАЖМИТЕ ЛЮБУЮ КЛАВИШУ, ЧТОБЫ ПРОДОЛЖИТЬ...')
        # readkey()  # кросс-платформенный аналог
        input()
        print('\n' * 5)

    print('Игра окончена.')
    input()

# -------------------  ЗАПУСК  -------------------
if __name__ == '__main__':
    main()
