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
# 字符串运算符
print("a+b:", a + b)  # 输出a+b
print("a*2:", a*2)  # 输出a*2
print("a[4]", a[4])  # 输出a[4]
print("b[2:4]", b[2:4])  # 输出b[2:4]

print("-------------------字符串格式化-------------------------")
# 字符串格式化
print("a = %s" % a, "b = %s" % b)  # 格式化输出a、b
print("a = %s b = %s" % (a, b))  # 格式化输出a、b
print("my name is %s, i am %d years old" % ('heying', 23))  # 我的格式化输出
# f-string
name = "heying"
print("Hello %s" % name)

print(f'hello {name}')   # 替换变量
print(f'{1+2}')    # 使用表达式

w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f"{w['name']}")  # 输出name的值
print("url:" f"{w['url']}")  # 输出url的值
print(f"{w['name']}:{w['url']}")   # f-string方式格式化输出列表的值

print("-------------------python字符串内建函数-------------------------")
# 1.将字符串第一个字符转换为大写 capitalize()
'''
capitalize() 
1.若首字符为字母小写，将首字符转换成大写，其余字符转换成小写
2.若首字符是非字母，首字母不转换为大写，会转换为小写
'''
print("1------------------")
a = 'hello PYTHON'
print("a:", a)
a.capitalize()
print("hello中首字母大写：", a.capitalize())


# 2.返回一个指定的宽度 width 居中的字符串，fill char为填充的字符，默认为空格。 center(width, fill char)
'''
center(width, fillchar)
1.如果宽度小于字符串，不会截断，完整输出
2.fill char默认是空格
3.fill char只能是单个字符
'''
print("2------------------")
print("a.center(20, '*')：", a.center(20, '*'))  # 长度20，使用*填充
print("a.center(5, '*')：", a.center(5, '*'))  # 长度<字符串长度，使用*填充
print("a.center(20)：", a.center(20))  # 默认填充字符
# print("返回一个指定的宽度width居中的字符串：", a.center(20, '?!'))
# TypeError: The fill character must be exactly one character long

# 3.返回str在string里出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数  count(str, beg= 0,end=len(string))
print("3------------------")
a.count('l')
print("hello中‘l’出现的次数：", a.count('l'))
a.count('l', 0, 3)
print("hello中前三个字符中‘l’出现的次数：", a.count('l', 0, 3))

# 4.Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
#   bytes.decode(encoding="utf-8", errors="strict")
# 5.encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
#   encode(encoding='UTF-8', errors='strict')
print("4、5------------------")
str1 = "菜鸟教程"
str_utf8 = str1.encode("UTF-8")
str_gbk = str1.encode("GBK")
print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))

# 6.检查字符串是否以obj结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
#   endswith(suffix, beg=0, end=len(string))
'''
1.endswith区别大小写，大小写影响结果
2.endswith可以匹配空格，可以为''或' '
3.endswith第二和第三个参数必须同时存在
'''
print("6------------------")
a = a + '!!!'
print(a)
print(a.endswith('on', 0, 15))  # 小写   false
print(a.endswith('ON', 0, 15))  # 大写    false
print(a.endswith('ON', 0, 15))  # 长度正好  false
print(a.endswith(' ', 1, 6))  # 匹配空格    true
print(a.endswith('!!!'))  # 仅包括suffix参数     true
su = '!'
print(a.endswith(su, 15))  # 后两个参数仅包含一个 false

# 7.把string中的tab符号转为空格，tab符号默认的空格数是8   expandtabs(tabsize=8)
'''
expandtabs方法补充空格的规则：“\t”前的字符相加为8的倍数
'''
print("7------------------")
str0 = '12345678\tstring example ... wow'   # 8个字符，补充8个
str1 = '1234567\tstring example'   # 7个字符，补充1个
str2 = '123456\tstring example ... wow'   # 6个字符，补充2个
str3 = '12345\tstring example ... wow'   # 5个字符，补充3个
str4 = '1234\tstring example ... wow'   # 4个字符，补充4个
str5 = '123\tstring example ... wow'   # 3个字符，补充5个
str6 = '12\tstring example ... wow'   # 2个字符，补充6个
str7 = '1\tstring example ... wow'   # 1个字符，补充7个
str8 = '\tstring example ... wow'   # 0个字符，补充8个
print("str0替换\\t符号           ：", str0.expandtabs())  # 默认参数
print("str1替换\\t符号           ：", str1.expandtabs())  # 默认参数
print("str2替换\\t符号           ：", str2.expandtabs())  # 默认参数
print("str3替换\\t符号           ：", str3.expandtabs())  # 默认参数
print("str4替换\\t符号           ：", str4.expandtabs())  # 默认参数
print("str5替换\\t符号           ：", str5.expandtabs())  # 默认参数
print("str6替换\\t符号           ：", str6.expandtabs())  # 默认参数
print("str7替换\\t符号           ：", str7.expandtabs())  # 默认参数
print("str8替换\\t符号           ：", str8.expandtabs())  # 默认参数
print("str8使用16个空格替换\\t符号： " + str8.expandtabs(16))

# 8.检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
#   find(str, beg=0, end=len(string))
'''
返回的索引值不包含空格
'''
print("8------------------")
print(len(str1))
print("不存在字符:", str1.find('hy'))        # 查找不存在的字符，返回-1
print("已存在字符:",  str1.find('string', 1, len(str1)))    # 查找存在的字符，使用默认值

# 9.同find，若str不在字符串中报一个异常 str.index(str, beg=0, end=len(string))
print("9------------------")
str1 = "Run example....wow123哈哈!!!"
str2 = "exam"

print(str1.index(str2))     # 比较字符
print(str1.index(str2, 4))      # 比较字符和开始索引值
# print(str1.index(str2, 10))   # 开始索引超范围 ValueError: substring not found

# 10.如果字符串至少有一个字符且索引字符都是[字母或数字]，返回true，否则返回false
# isalnum()
'''
！汉字也会返回true
'''
print("10------------------")
print("str1:%s,  str2:%s" % (str1, str2))
print("str1:", f'{str1}', "str2:", f'{str2}')
print("str1.isalnum():", str1.isalnum())    # false
print("str2.isalnum():", str2.isalnum())    # true

# 11.如果字符串至少有一个字符且索引字符都是[字母]，返回true，否则返回false
# isalpha()
'''
！汉字也会返回true
'''
print("11------------------")
print("str1:", f'{str1}', "str2:", f'{str2}')
print("str1.isalpha()", str1.isalpha())     # false
print("str2.isalpha()", str2.isalpha())     # true

# 12.如果字符串至少有一个字符且索引字符都是[数字]，返回true，否则返回false  str.islower()
# isdigit()
print("12------------------")
str3 = '1234567'
print("str1:", f'{str1}', "str3:", f'{str3}')
print("str1.isalpha()", str1.isdigit())     # false
print("str3.isalpha()", str3.isdigit())     # true

# 13.检测字符串中是否由小写字母组成
# islower()
print("13------------------")
example = "RUNOOB example....wow!!!"
print(example.islower())    # false

example = "runoob example....wow!!!"
print(example.islower())    # true

# 14.如果字符串中只包含数字字符，则返回true，否则返回false
# isnumeric()
print("14------------------")
print('hy123'.isnumeric())  # false
print('123'.isnumeric())    # true
print('1km2'.isnumeric())   # false

# 15.如果字符串中只包含空白，则返回 True，否则返回 False.
# isspace()
'''
1.''不是空白字符串
2.' ','\n', '\t'是空白字符串
'''
print("15------------------")
print("".isspace())     # false
print(" ".isspace())    # true
print("\t".isspace())   # true
print("\n".isspace())   # true

# 16.如果字符串是标题化的(见 title())则返回 True，否则返回 False
'''
标题化字符串中输入汉字，仍返回true
'''
print("16------------------")
example = 'My Name Is Heying哈哈哈'
print(example.istitle())    # 符合格式，true
example = 'My Name Is HeYing'
print(example.istitle())    # 不完全符合格式，false
example = 'my name is heying'
print(example.istitle())    # 完全不符合格式，false

# 17.如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
# isupper()
'''
大写字符串中输入汉字，仍返回true
'''
print("17------------------")
example = "THIS IS STRING EXAMPLE....WOW哈哈!!!"
print(example.isupper())    # true

example = "THIS is string example....wow!!!"
print(example.isupper())    # false

# 18.以指定的字符串作为分隔符，将seq中所有的元素（的字符串表示）合并为一个新的字符串
# join(seq) seq: 要连接的元素序列
print("18------------------")
l1 = '_'
l2 = '-'
l3 = ''
l4 = 'q'
l5 = '哈'
str1 = ('h', 'e', '', 'y', 'i', 'n', 'g', '!')
print(l1.join(str1))
print(l2.join(str1))
print(l3.join(str1))
print(l4.join(str1))
print(l5.join(str1))

# 19.返回字符串长度
# len(string)
print("19------------------")
print(len(str1))
