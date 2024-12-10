import pulp
import random

# 1. Генерация данных
# Дисциплины и их курсы
disciplines = {
    'Современные языки программирования': [
        'JavaScript. Разработка пользовательских веб-интерфейсов (HTML-академия)',
        'Основы бэкенд-разработки на Python (часть 1) (Яндекс)',
        'Основы веб-разработки JavaScript',
        'Основы фронтенд-разработки (часть 1) (Яндекс)',
        'Программирование на C/C++ (Прософт)',
        'Программирование на Go (SkillFactory)',
        'Программирование на Java (смешанный курс)',
        'Программирование на Java (Тинькофф)',
        'Программирование на JavaScript (смешанный курс, SkillBox)',
        'Программирование на PHP',
        'Программирование на TypeScript (ArtSoftе)',
        'Программирование на TypeScript (смешанный курс, SkillBox)',
        'Профессия Java-разработчик (SkillFactory)',
        'Разработка web приложений на C# (ООО "Очень интересно")',
        'Разработка на C# и ASP. Net Core (SkillFactory)',
        'Язык R для анализа данных (смешанный курс, Skillbox)'
    ],

    'Базы данных': [
        'Базы данных (Онлайн, СПБГУ, ОК)',
        'Базы данных (традиционный курс)',
        'Базы данных и SQL',
        'Базы данных: SQL, реляционные и MPP СУБД (Карпов Курсы)',
        'Проектирование и реализация баз данных (Онлайн, ИТМО, ОК)'
    ],

    'Системная аналитика': [
        'Бизнес-аналитика',
        'Системная аналитика (Альфа-Банк)',
        'Системная аналитика (ИИТ)',
        'Системная аналитика (МТС)'
    ],

    'Теория вероятностей и математическая статистика': [
        'Теория вероятностей и математическая статистика (традиционный, СМУДЭ (НТК))'
    ],

    'Технологии программирования': [
        'Технологии программирования'
    ],

    'Эффективные коммуникации': [
        'Эффективные коммуникации (онлайн, УрФУ, ОК)',
        'Эффективные коммуникации (Смешанное, УрФУ, ОК)',
        'Эффективные коммуникации (традиционная форма)',
        'Эффективные коммуникации (ЦРЦК)'
    ],

    'Анализ данных и искусственный интеллект': [
        'Анализ данных в разработке игр',
        'Анализ данных и искусственный интеллект',
        'Аналитика данных и методы искусственного интеллекта (Ростелеком)',
        'Аналитика и визуализация данных',
        'Введение в Data Science и машинное обучение (Смешанное; Stepik; Без НТК)',
        'Введение в искусственный интеллект (онлайн, ВШЭ, ОК)',
        'Машинное обучение и анализ данных (онлайн, ИТМО, ОК)',
        'Наука о данных и аналитика больших объемов данных (онлайн, СПБГУ, ОК)',
        'Основы искусственного интеллекта (онлайн, МГУ, ОК)',
        'Технологии искусственного интеллекта'
    ],

    'Архитектура ЭВМ': [
        'Архитектура ЭВМ',
        'Архитектура ЭВМ. Контур (Повышенный уровень)',
        'Введение в архитектуру ЭВМ. Элементы операционных систем. (Смешанный, Stepik)',
        'Основы архитектуры ЭВМ для инженеров и разработчиков ПО'
    ]
}

course_to_discipline = {}
for discipline, courses_list in disciplines.items():
    for course in courses_list:
        course_to_discipline[course] = discipline

courses = [course for course_list in disciplines.values() for course in course_list]

# Допустим, у нас есть 10 преподавателей
professors = [f'Преподаватель{i}' for i in range(1, 11)]

# Генерируем предпочтения по курсам (коэффициенты от 1 до 10)
preferences_courses = {c: random.randint(1, 10) for c in courses}

# Генерируем предпочтения по преподавателям (коэффициенты от 1 до 10)
preferences_professors = {p: random.randint(1, 10) for p in professors}

# Формируем группы для каждого курса (по 3-5 групп на курс)
groups_courses = {}
for c in courses:
    group_count = random.randint(3, 5)  # 3-5 групп
    groups_courses[c] = [f'Группа_{c}_{i}' for i in range(1, group_count + 1)]

# Распределяем преподавателей по группам (случайным образом)
professors_groups = {}
for c, gs in groups_courses.items():
    for g in gs:
        professors_groups[g] = random.choice(professors)

# Определяем возможные дни недели
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
# Временные интервалы
times_per_day = [
    '8:30-10:00',
    '10:15-11:45',
    '12:00-13:30',
    '14:15-15:45',
    '16:00-17:30',
    '17:40-19:10',
    '19:15-20:45'
]

# Формируем список всех временных слотов
time_slots = []
for day in days:
    for t in times_per_day:
        time_slots.append(f'{day}_{t}')

# Привязка слотов к дням
time_to_day = {}
for day in days:
    time_to_day[day] = [slot for slot in time_slots if slot.startswith(day)]

# Каждой группе зададим временной слот
time_groups = {}
for g in professors_groups.keys():
    time_groups[g] = random.sample(time_slots, 1)

# Добавляем фиксированные курсы
fixed_courses = {
    'Физкультура': ['Среда_10:15-11:45', 'Пятница_14:15-15:45']
}

# Расширяем список недоступных временных слотов
unavailable_times = [
    'Понедельник_8:30-10:00',
    'Вторник_8:30-10:00',
    'Среда_8:30-10:00',
    'Четверг_8:30-10:00',
    'Вторник_10:15-11:45',
    'Четверг_12:00-13:30',
    'Пятница_14:15-15:45',
    'Суббота_8:30-10:00',
    'Суббота_10:15-11:45',
    'Суббота_12:00-13:30',
    'Суббота_14:15-15:45',
    'Суббота_16:00-17:30',
    'Суббота_17:40-19:10',
    'Суббота_19:15-20:45'
]

fixed_time_slots = [time for times in fixed_courses.values() for time in times]
# Доступные временные слоты студента (все, кроме недоступных и фиксированных)
available_times = [t for t in time_slots if t not in unavailable_times + fixed_time_slots]

# Коэффициенты значимости
alpha = 0.5  # Важность приоритета курса
beta = 0.5   # Важность предпочтения преподавателя
delta = 1    # Коэффициент для минимизации 'окон'

# Максимальное количество пар в день
M = 3

# 2. Реализация алгоритма
prob = pulp.LpProblem('Student_Schedule_Optimization', pulp.LpMaximize)

# Переменные решения: x[(c, g, t)]
x = pulp.LpVariable.dicts(
    'x',
    [(c, g, t) for c in courses for g in groups_courses[c] for t in time_groups[g] if t in available_times],
    cat='Binary'
)

# Переменные для фиксированных курсов
x_fixed = pulp.LpVariable.dicts(
    'x_fixed',
    [(c, t) for c in fixed_courses for t in fixed_courses[c]],
    cat='Binary'
)

# Переменные для 'окон'
gap = pulp.LpVariable.dicts('gap', time_slots, cat='Binary')

# Сумма 'окон'
total_gaps = pulp.lpSum([gap[t] for t in time_slots])

# Целевая функция
prob += pulp.lpSum([
    (alpha * preferences_courses[c] + beta * preferences_professors[professors_groups[g]]) * x[(c, g, t)]
    for (c, g, t) in x
]) - delta * total_gaps

# 3. Добавление ограничений

# 1. Каждый курс может быть выбран не более одного раза
for c in courses:
    prob += pulp.lpSum([x[(c, g, t)] for g in groups_courses[c] for t in time_groups[g] if t in available_times]) <= 1, f'Course_{c}_once'

# 2. Один курс из каждой дисциплины
for d in disciplines:
    prob += pulp.lpSum([x[(c, g, t)] for c in disciplines[d] for g in groups_courses[c] for t in time_groups[g] if t in available_times]) == 1, f'One_Course_Per_Discipline_{d}'

# 3. Не более одного занятия в один временной слот
for t in available_times:
    prob += pulp.lpSum([x[(c, g, t_var)] for (c, g, t_var) in x if t_var == t]) <= 1, f'One_Class_Per_Time_{t}'

# 4. Фиксированные курсы должны быть строго на своём месте
for c in fixed_courses:
    for t in fixed_courses[c]:
        prob += x_fixed[(c, t)] == 1, f'Fixed_Course_{c}_{t}'

# 5. Максимальное количество пар в день не превышает M
for day in days:
    slots_in_day = time_to_day[day]

    # Суммируем занятия из обычных курсов и фиксированных курсов
    total_classes_in_day = (
        pulp.lpSum([x[(c, g, t)] for (c, g, t) in x if t in slots_in_day]) +
        pulp.lpSum([x_fixed[(c, t)] for (c, t) in x_fixed if t in slots_in_day])
    )
    # Ограничение на максимальное количество пар в день
    prob += total_classes_in_day <= M, f'Max_Classes_Per_Day_{day}'


# 6. Ограничения на 'окна' (пропуски)
def add_no_gaps_constraints(prob, time_to_day, x):
    for day, time_slots_in_day in time_to_day.items():
        # Отсортируем временные слоты в порядке их появления
        sorted_slots = sorted(time_slots_in_day, key=lambda x: times_per_day.index(x.split('_')[1]))

        # Проверяем каждую комбинацию начального и конечного слота
        for i in range(len(sorted_slots) - 1):
            for j in range(i + 1, len(sorted_slots)):
                t_start = sorted_slots[i]
                t_end = sorted_slots[j]
                # Все промежуточные слоты
                intermediate_slots = sorted_slots[i + 1:j]

                # Переменные для начального и конечного слотов
                x_start = pulp.lpSum(
                    [x[(c, g, t_start)] for (c, g, t_var) in x if t_start == t_var]
                )
                x_end = pulp.lpSum(
                    [x[(c, g, t_end)] for (c, g, t_var) in x if t_end == t_var]
                )

                # Переменные для промежуточных слотов
                x_intermediate = pulp.lpSum(
                    [x[(c, g, t_var)] for (c, g, t_var) in x if t_var in intermediate_slots]
                )

                # Проверка существования промежуточных переменных и добавление ограничения
                if intermediate_slots:  # Промежуточные слоты существуют
                    prob += x_start + x_end - x_intermediate <= 1, f"No_Gaps_Between_{t_start}_and_{t_end}"


# Применяем ограничения
add_no_gaps_constraints(prob, time_to_day, x)

# 4. Решение задачи
prob.solve(pulp.PULP_CBC_CMD(msg=False))

# 5. Вывод результатов
if pulp.LpStatus[prob.status] == 'Optimal':
    schedule = []
    for (c, g, t) in x:
        if pulp.value(x[(c, g, t)]) == 1:
            # Извлекаем день и время
            day, time_slot = t.split('_', 1)
            discipline = course_to_discipline[c]
            p = professors_groups[g]
            schedule.append((day, time_slot, discipline, c, g, p))

    # Добавляем фиксированные курсы в расписание
    for (c, t) in x_fixed:
        if pulp.value(x_fixed[(c, t)]) == 1:
            day, time_slot = t.split('_', 1)
            schedule.append((day, time_slot, 'Фиксированный курс', c, '-', '-'))

    # Сортируем расписание: сначала по индексу дня, затем по индексу временного слота
    day_order = {d: i for i, d in enumerate(days)}  # Порядок дней
    time_order = {t: i for i, t in enumerate(times_per_day)}  # Порядок времен

    schedule.sort(key=lambda x: (day_order[x[0]], time_order[x[1]]))

    print(f'Составленное расписание c ограничением на {M} пары в день:')
    current_day = None
    pairs_count = 0
    for entry in schedule:
        day, time_slot, discipline, course, group, professor = entry
        if current_day != day:
            if current_day is not None:  # Печатаем итог по предыдущему дню
                print(f'Общее количество пар на день: {pairs_count}\n')
            current_day = day
            pairs_count = 0  # Обнуляем счётчик для нового дня
            print(f'\n*** {current_day} ***')
        print(f'Время: {time_slot} | Дисциплина: {discipline}, Курс: {course}, Группа: {group}, Преподаватель: {professor}')
        pairs_count += 1  # Увеличиваем счётчик пар

    # Итог для последнего дня
    if current_day is not None:
        print(f'Общее количество пар на день: {pairs_count}\n')

    total_gaps_value = sum([pulp.value(gap[t]) for t in time_slots])
    print(f'Общее количество окон: {int(total_gaps_value)}')
else:
    print('Не удалось найти оптимальное решение. Проверьте данные и ограничения.')
