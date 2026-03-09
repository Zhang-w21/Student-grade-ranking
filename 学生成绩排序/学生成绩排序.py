# 需求：给定一个学生信息列表，根据学生的成绩进行排序
# 原始列表
students = [
    {'sno': 101, 'sname': "小张", 'sgrade': 88},
    {'sno': 102, 'sname': "小王", 'sgrade': 77},
    {'sno': 103, 'sname': "小李", 'sgrade': 99},
    {'sno': 104, 'sname': "小赵", 'sgrade': 66}
]
# 结合匿名函数简化代码（当代码只使用一次没必要专门定义）:lambda 形参：返回值

# 根据学生成绩进行排序
students_sort1 = sorted(students, key = lambda x:x["sgrade"]) # 升序排列
students_sort2 = sorted(students, key = lambda x:x["sgrade"], reverse = True) # 降序排列
print(f"原列表：{students}")
print(f"升序排序后：{students_sort1}")
print(f"降序排序后：{students_sort2}")


# 注意：匿名函数只能实现简单的逻辑，如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化
# 一般而言，匿名函数调用次数很少，基本只调用一次