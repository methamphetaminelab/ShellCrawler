# ShellCrawler

### Главное меню

- Главное меню

  - Новая игра
  - Загрузить игру
  - Выйти из игры

- Новая игра

  - Название персонажа
    - Распределить очки навыков
      - Начать игру
      - Выйти обратно
    - Выйти обратно
  - Выход в меню

- Распределение очков навыков (изначально доступно 10 очков навыков, игроку предлагается их распределить)

  - Сила [+/-]
  - Ловкость [+/-]
  - Интеллект [+/-]
  - Удача [+/-]

- Меню загрузки сохранений

  - Сохранение 1
  - Сохранение 2
  - Сохранение 3
  - Выход в меню

### Основное игровое меню (ХАБ)

- Основное игровое меню (ХАБ)

  - Войти в подземелье
  - Персонаж
  - Торговцы
  - Квесты
  - Сохранить игру
  - Загрузить игру
  - Выход в главное меню

- Персонаж

  - Статистика
  - Инвентарь
  - Навыки
  - Экипировка
  - Достижения
  - Выход в главное меню

- Статистика

  - Уровень
  - Опыт (текущий\нужно)
  - Золото
  - Сытость (текущий\макс)

  - HP (текущий\макс)
  - MP (текущий\макс)

  - Броня
  - Урон
  - Шанс крит. удара
  - Множитель крит. удара
  - Скорость

  - Сила
  - Ловкость
  - Интеллект
  - Удача

  - Всего денег заработано
  - Всего врагов убито
  - Всего пройдено подземелий
  - Всего выполнено квестов
  - Всего получено достижений
  - Всего времени в игре

- Инвентарь (10 предметов на странице, неограниченный (типо склад))

  - Список предметов (название, эффект)
    - Использовать предмет
    - Положить предмет в рюкзак
    - Прочесть описание
    - Выкинуть предмет
  - Следующая\предыдущая страница
  - Выход в главное меню

- Навыки

  - Количество очков навыков (даются за повышение уровня)
  - Сила [+] [1LVL - 999LVL]
  - Ловкость [+] [1LVL - 999LVL]
  - Интеллект [+] [1LVL - 999LVL]
  - Удача [+] [1LVL - 999LVL]
  - Выход в главное меню

- Экипировка (экипированные предметы)

  - Оружие (урон, эффект)
  - Броня (защите, прочность, эффект)
  - Аксессуары (эффект)

- Достижения

  - Полученные достижения (название, эффект)
    - Прочитать описание
      - Эффект
      - Условие
      - Описание
      - Выход в меню достижений
  - Неполученные достижения (название, эффект)
    - Прочитать описание
      - Эффект
      - Условие
      - Описание
      - Выход в меню достижений
  - Выйти в главное меню

- Сохранить игру

  - Название сохранения (изначально называется [id слота сохранения]\_[название персонажа] (например 1_hero, 2_gerald, 3_knight))
  - Сохранить
  - Выход в главное меню

- Загрузить игру

  - Сохранение 1
  - Сохранение 2
  - Сохранение 3
  - Выход в главное меню

### Меню паузы и механика подземелья

- ПАУЗА

  - Имя персонажа
  - Краткая статистика (уровень, опыт(текущий\нужно), HP(текущий\макс), MP(текущий\макс), голод(текущий\макс), золото, урон, броня)
  - Карманы
  - Закрыть
  - Выйти из игры (в главное меню)

- Как будет выглядеть подземелье?
  - Будет использована ascii графика аля как в Dwarf Fortress
  - Будет сгенерирована структура подземелья (из заранее заготовленных или процедурно сгенерированных)
  - Игрок сможет перемещаться по подземелью стрелками
  - В подземелье будут встречаться враги ()
  - В подземелье будут встречаться сундуки (сундуки будут содержать вещи)
  - Чтобы покинуть подземелье нужно найти выход (вернуться через вход нельзя)
  - Изначально спавнится фиксированное количество врагов и сундуков (количество зависит от сложности подземелья)
  - Сложность подземелья высчитывается по формуле (кол-во врагов, кол-во комнат, кол-во сундуков): сложность = 1 + [уровень_персонажа]
  - Количество врагов высчитывается по формуле: _НЕ ПРИДУМАЛ_
  - Количество комнат высчитывается по формуле: _НЕ ПРИДУМАЛ_
  - Количество сундуков высчитывается по формуле: _НЕ ПРИДУМАЛ_
  - Урон врага высчитывается по формуле: урон = [базовый_урон_врага] + [уровень_персонажа] + [сложность_подземелья]
  - Броня врага высчитывается по формуле: броня = [базовый_урон_врага] + [уровень_персонажа] + [сложность_подземелья]
  - Каждое подземелье имеет шанс заспавнить босса
  - Шанс спавна босса высчитывается по формуле: шанс = [уровень_персонажа] \* [сложность_подземелья] \ 100

### Список предметов

- Еда (восстановление голода, эффект, описание)

  - Яблоко (10, +5 к HP, Восстанавливает 10 голода и немного увеличивает максимальное здоровье.)
  - Хлеб (15, —, Простая еда, восстанавливающая 15 голода, без дополнительных эффектов.)
  - Суп из овощей (20, +10 к восстановлению HP, Восстанавливает 20 голода и увеличивает восстановление здоровья на 10 HP на следующий ход.)
  - Мясной пирог (25, +10 к силе, Восстанавливает 25 голода и временно увеличивает силу на 10 единиц.)
  - Ягодный смузи (15, +5 к ловкости, Восстанавливает 15 голода и временно увеличивает ловкость на 5 единиц.)
  - Мед (5, +1 к восстановлению маны, Восстанавливает 5 голода и немного увеличивает восстановление маны.)
  - Фрукты тропиков (30, +5 к максимальному HP, Восстанавливает 30 голода и увеличивает максимальное здоровье на 5 единиц.)
  - Крепкий эль (20, +10% к шансу критического удара, Восстанавливает 20 голода и увеличивает шанс критического удара на 10% на один бой.)
  - Золотая рыба (15, +15% к удаче, Восстанавливает 15 голода и увеличивает удачу на 15% на 10 минут.)
  - Салат из морепродуктов (25, +5 к скорости, Восстанавливает 25 голода и временно увеличивает скорость передвижения на 5 единиц.)

- Оружие (урон, скорость, эффект, описание)

  - Короткий меч (5-10, 1.5, —, Легкий и маневренный меч, идеален для быстрого боя.)
  - Длинный меч (8-15, 1.2, —, Сбалансированный меч, хорошо подходит для большинства бойцов.)
  - Двуручный меч (12-20, 0.8, —, Мощный меч, требующий обеих рук для использования, наносящий сильный урон.)
  - Меч с зазубринами (10-18, 1.0, +10% шанс крит. удара, Имеет зазубрины, увеличивает шанс критического удара.)
  - Меч из темного металла (15-25, 0.9, +2 урона от тьмы, Ужасающий меч, закованный в темный металл.)
  - Ритуальный меч (8-14, 1.1, +1 восстановление маны, Меч, использовавшийся в древних ритуалах, обладает магическими свойствами.)
  - Меч из ледяного кристалла (10-15, 1.0, Замедляет врага на 20% на 3 секунды, Меч, выкованный из ледяного кристалла.)
  - Двуручный меч с огненным лезвием (14-22, 0.7, +3 урона огнем, Пылающий меч, оставляющий следы огня.)
  - Меч из чистого серебра (9-16, 1.3, +20% урон против нежити, Эффективный против темных существ и нежити.)
  - Световой меч (12-18, 1.1, +2 HP при критическом ударе, Излучающий свет, защищающий от темноты.)

- Броня (защита, прочность, эффект, описание)

  - Легкие доспехи (3, 20/20, —, Идеальны для ловких бойцов, позволяя быстро передвигаться.)
  - Кольчуга (5, 25/25, —, Сбалансированная броня, обеспечивающая хорошую защиту без значительной потери скорости.)
  - Тяжелая броня (8, 30/30, —, Предоставляет мощную защиту, но замедляет движение на 10%.)
  - Робо-броня (7, 25/25, +2 к атаке, Современная броня, усиливающая силу атаки владельца.)
  - Капюшон из теней (4, 15/20, +10% уклонения, Легкая броня, увеличивающая шанс уклонения от атак.)
  - Доспехи из драконьей кожи (6, 20/20, +15% урон от огня, Обеспечивают защиту и увеличивают урон от огня.)
  - Костюм из мха (2, 18/20, +5 к восстановлению HP, Удобный костюм, восстанавливающий здоровье владельца на 5 HP в минуту.)
  - Энергетическая броня (9, 22/25, +3 к магической защите, Высокоразвитая броня, обеспечивающая защиту от магических атак.)
  - Серебряные доспехи (6, 25/25, +20% защита против нежити, Эффективны против тёмных существ и нежити.)
  - Мифриловая броня (7, 30/30, —, Легкая, но прочная броня, позволяющая быстро передвигаться без потери защиты.)

- Аксессуары (эффект, описание)

  - Кольцо силы (+2 к силе, Увеличивает силу владельца, позволяя наносить больший урон.)
  - Ожерелье ловкости (+3 к ловкости, Увеличивает ловкость владельца, улучшая уклонение и шансы критических ударов.)
  - Браслет интеллекта (+2 к интеллекту, Увеличивает интеллект, улучшая эффективность магических заклинаний.)
  - Перчатки удачи (+5% шанс находки, Увеличивают шанс находки редких предметов при исследовании.)
  - Кулон жизни (+10 HP, Увеличивает максимальное здоровье владельца.)
  - Серьги мудрости (+1 к восстановлению маны, Увеличивают скорость восстановления маны.)
  - Часы времени (+10% скорость передвижения, Увеличивают скорость передвижения владельца на 10%.)
  - Магический амулет (+2 к магической защите, Обеспечивает дополнительную защиту от магических атак.)
  - Сумка хранения (Увеличивает инвентарь на 5 слотов, Позволяет носить больше предметов.)
  - Знак нежити (+15% урон против нежити, Увеличивает урон против нежити на 15%.)

- Рюкзаки (кол-во слотов, эффект, описание)

  - Маленький рюкзак (5 слотов, Увеличивает инвентарь на 5 слотов. Легкий и компактный.)
  - Средний рюкзак (10 слотов, Увеличивает инвентарь на 10 слотов. Хороший баланс между размером и вместимостью.)
  - Большой рюкзак (15 слотов, Увеличивает инвентарь на 15 слотов. Подходит для приключенцев, собирающих много вещей.)
  - Рюкзак из волшебной ткани (20 слотов, Увеличивает инвентарь на 20 слотов. Легкий и вместительный, способен сохранять вещи в целости.)
  - Рюкзак с бесконечным карманом (999 слотов, Увеличивает инвентарь на 30 слотов. Уникальный рюкзак, позволяющий хранить неограниченное количество предметов.)

### Достижения

- Первая кровь (Убить первого врага)

  - Эффект: +50 опыта
  - Описание: Поздравляем, вы впервые убили врага!

- Собирающий сокровища (Найти 10 предметов)

  - Эффект: +100 золота
  - Описание: Вы проявили смекалку и нашли множество сокровищ.

- Покоритель подземелий (Пройти 5 подземелий)

  - Эффект: +1 уровень
  - Описание: Вы стали мастером подземелий!

- Магический исследователь (Получить 5 магических предметов)

  - Эффект: +2 к интеллекту
  - Описание: Вы открыли для себя секреты магии!

- Супергерой (Достигнуть 10 уровня)

  - Эффект: +5 к максимальному HP
  - Описание: Ваши навыки и способности достигли нового уровня!

- Удачный искатель (Найти редкий предмет)

  - Эффект: +10% шанс находки
  - Описание: Вам повезло найти редкий артефакт!

- Заслуженный наград (Завершить 20 квестов)

  - Эффект: +500 золота
  - Описание: Вы стали легендой среди искателей приключений!

- Мастер брони (Надеть все виды брони)

  - Эффект: +1 к защите
  - Описание: Вы изучили все виды доспехов, теперь вы неуязвимы!

- Вечный искатель приключений (Провести в игре 10 часов)

  - Эффект: +5 к удаче
  - Описание: Вы провели много времени в этом мире, и удача теперь на вашей стороне.
