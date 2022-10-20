from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipe_view(request, recipe):
    # Напишите ваш обработчик. Используйте DATA как источник данных
    # Результат - render(request, 'calculator/index.html', context)
    # В качестве контекста должен быть передан словарь с рецептом:


    if recipe in DATA:
        arr = dict()
        arr.clear()
        for item, val in DATA[recipe].items():
            arr[item] = val
        servings = int(request.GET.get('servings', 1))
        for item, val in arr.items():
            arr[item] = val * servings
        context = {
            'servings': servings,
            'recipe': arr
        }
    else:
        context = False
    return render(request, 'calculator/index.html', context)

