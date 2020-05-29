# 创建列表
list1 = [1, 2, 3, 4, 5]
list2 = ['基础模板', 'test_hy', '酷黑模板', 20200528]

print("-------------------------访问列表-----------------------------")
# 获取list1\list2所有元素
print("list1:", list1)
print("list2:", list2)

# 访问列表
# 获取列表第2-4个数 list[1:4]
print("list1[1:4]:", list1[1:4])
# 输出从第二个元素开始后的所有元素
print("list[1:]", list2[1:])

# 获取列表第3个数 list[2]
print("list2[2]:", list2[2])
# 获取列表倒数第2个数 list[-2]
print("list2[-2]:", list2[-2])


print("-------------------------更新列表-----------------------------")
# 更新列表的第三个参数 list[2]='hy'
print("第三个元素为：", list2[2])
list2[2] = 'hy'
print("更新后的第三个元素为：", list2[2])

print("-----------------------删除列表元素---------------------------")
print("更新后的list2:", list2)
# 删除list2第4个元素 del list[3]
del list2[3]
print("删除后的list2：", list2)

print("-----------------------列表脚本操作符-------------------------")
# 长度
print("len(list1):", len(list1))
print("len(list2):", len(list2))

# 组合
print("list1 + list2:", list1 + list2)
print("list2 + list1:", list2 + list1)

# 重复
print("[1, 2, 3] * 3:", [1, 2, 3] * 3)

# 元素是否在列表中
if 4 in list1:
    print("4 in list1")
else:
    print("4 not in list1")

# 迭代 (end=''表示不换行输出）
for x in [1, 2, 3]:
    print(x, end="")
print("\n")

print("-----------------------列表截取、拼接、嵌套-------------------------")
# 截取
list3 = "hello world!"
print(list3)
print("list3[2]", list3[2])  # 第2个
print("list3[-2]", list3[-2])  # 倒数第2个
print("list3[1:]", list3[1:])   # 输出第二个元素以后的list元素
print("len(list3)", len(list3))

# 拼接
squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]
print("squares:", squares)

# 嵌套
a = ['a', 'b', 'c']
b = [1, 2, 3]
x = [a, b]
print(x)
print(x[0])
print(x[0][2])
print(x[1])

print("-----------------------列表函数&方法-------------------------")
list2 = ['基础模板', 'test_hy', '酷黑模板', 20200528]

# 列表元素个数 len(list)
num = len(list2)
print("list2元素个数:", num)

# 返回列表元素的最大值 max(list)
max_value = max(list1)
print("list2元素最大值:", max_value)

# 返回列表元素的最小值 min(list)
min_value = min(list1)
print("list2元素最大值:", min_value)

# 元组或字符串转换为列表 list(seq)
st = "python test"
tup1 = ('Google', 'Run', 1997, 2000)
print("st type:", type(st))
print("tup1 type:", type(tup1))
# 元组转换为列表
tup1_list = list(tup1)
print(tup1_list)
print('tup1_list type:', type(tup1_list))

# 字符串转换为列表
st_list = list(st)
print(st_list)
print("st_list type:", type(st_list))

# 在列表末尾添加新的对象 list.append(obj)
list1.append(1)
list1.append(2)
list1.append(1)
print("追加后的list1：", list1)

# 统计某个元素在列表中出现的次数 list.count(obj)
list1.count(1)
print("list1.count(1)", list1.count(1))

# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） list.extend(seq)
list1.extend(list3)
print("追加多个值后的list1：", list1)

# 从列表中找出某个值第一个匹配项的索引位置 list.index(obj)
print("list1中第一个o的索引位置：", list1.index('o'))
print("list1中第一个2的索引位置：", list1.index(2))

# 将对象插入列表 list.insert(index, obj)
print("list2-old:", list2)
list2.insert(2, '16:57')
print("list2-new:", list2)

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 list.pop([index=-1])
# 移除默认元素
num = list2.pop(-1)
print("list2移除后:", list2)
print(num)

# 移除第三个元素
num = list2.pop(2)
print("list2第2个元素移除后:", list2)
print(num)

# 移除列表中某个值的第一个匹配项 list.remove(obj)
print("list1:", list1)
list1.remove('o')
print("list1移除第1个匹配元素移除后:", list1)
list1.remove(2)
print("list1移除第1个匹配元素移除后:", list1)

# 反向列表中的元素 list.reverse()
list2.reverse()
print("反向list2：", list2)

# 对原列表进行排序	list.sort( key=None, reverse=False),reverse = True 降序， reverse = False 升序（默认）。
list2.sort(reverse=False)
print("升序输出：", list2)
list2.sort(reverse=True)
print("降序输出：", list2)


# 获取列表的第二个元素
def take_second(elem):
    return elem[1]


random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# 指定第二个元素降序排序
random.sort(key=take_second, reverse=True)
print('排序列表：', random)

# 清空列表 list.clear()
print("原list1：", list1)
list1.clear()
print("清空后的list1：", list1)

# 复制列表 list.copy()
list1 = list2.copy()
print("复制后的list1：", list1)
