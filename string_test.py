var1 = "selenium 2"
var2 = "基于python语言"

# 访问字符串的值
print("var2[0]: ", var2[0])  # 输出var2第一个元素
print("var2[1:5]: ", var2[1:9])  # 输出var2从第2元素，到第9个元素

# 字符串更新 取[0：9]是因为想要个空格
var3 = var1[0:9] + var2[2:8]  # var3为var1 1-9+var2 3-8
print("截取拼接的var3:", var3)

print("-------------------字符串运算符-------------------------")
a = "hello"
b = "python"

# 字符串格式化
print("a = %s" % a, "b = %s" % b)  # 格式化输出a、b
print("a = %s b = %s" % (a, b))  # 格式化输出a、b
print("my name is %s, i am %d years old" % ('heying', 23))  # 我的格式化输出

# 字符串运算符
print("a+b:", a + b)  # 输出a+b
print("a*2:", a*2)  # 输出a*2
print("a[4]", a[4])  # 输出a[4]
print("b[2:4]", b[2:4])  # 输出b[2:4]

# f-string
name = "heying"
print("Hello %s" % name)

print(f'hello {name}')
print(f'{1+2}')

w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f"{w['name']}")