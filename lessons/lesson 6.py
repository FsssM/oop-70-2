# # @abstractmethod
# # @staticmethod
# # @classmethod
# # @property
#
# # def simple_decorator(func):
# #     def wrapper():
# #         print("До выполнения")
# #         func()
# #         print("После выполнения")
# #     return wrapper
# #
# # @simple_decorator
# # def say_hello():
# #     print("hello")
# #
# # say_hello()
#
# def greeting_decorator(func):
#     def wrapper(*args):
#         print(args)
#     return wrapper
#
# @greeting_decorator
# def greeting(name, test):
#     pass
#     print(f'{name} Как дела?')
#
# # greeting("Ardager",{"test": "test"})
#
# # def greeting_decorator(func):
# #     def wrapper(*args):
# #         print(args)
# #     return wrapper
# #
# # def repeat_decorator(n):
# #     def decorator(func):
# #         def wrapper(name):
# #             for i in range(n):
# #                 func(name)
# #         return wrapper
# #     return decorator
#
# # @repeat_decorator(4)
# # def hello(name):
# #     print(f"Hello {name}")
# #
# # hello("Ardager")
#
#
# def class_decorator(cls):
#     class NewClass:
#         def action(self):
#             print('Новый метод!!')
#     return NewClass
#
# @class_decorator
# class OldClas:
#     def action(self):
#         print("Старый метод!!")
#
# test_obj = OldClas()
#
# test_obj.action()
# # print(type(test_obj))

# nums_list = [2,7,11,15]

# for index, item in enumerate(nums_list):
#     print(index, " ", item)

nums_list = [7,11,15,3]
target_int = 9.25
def twoSum(nums,target):
    num_map = {
    }
    step_count = 0
    for index, item in enumerate(nums):
        step_count += 1
        print(f"Итерация {step_count}")
        print(f"Наш словарь {num_map}")
        print(f'Index:{index} Item:{item}')
        complement = target - item
        print(f'Нужно найти в словаре {complement}')
        if complement in num_map:
            return [num_map[complement], index]
        num_map[item] = index
    return []

print(twoSum(nums_list, target_int))