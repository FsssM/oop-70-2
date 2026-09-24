def two_sum(nums, target):
    # Внешний цикл проходит по всем элементам списка (индекс i)
    for i in range(len(nums)):
        # Внутренний цикл проходит по элементам СПРАВА от i (индекс j)
        for j in range(i + 1, len(nums)):
            # Проверка, дает ли сумма элементов под индексами i и j значение target
            if nums[i] + nums[j] == target:
                return [i, j]  # Возвращаем список с индексами найденных чисел


# Проверка работы функции
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(f"Результат: {result}")  # Должно вывести [0, 1]