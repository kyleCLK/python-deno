# 用括号括起来的都是字符串，其中引号可以是单引号，也可以是双引号。
# 案例1：
message = "This is a string,翻译：这是字符串。"
print(message)   # 输出：This is a string,翻译：这是字符串。
message = 'This is also a string,翻译：这也是字符串。'
print(message)   # 输出：This is also a string,翻译：这也是字符串。

# 案例2：灵活运用单，双引号
told = "I told my friends：'that Python is the best language in the world'" 
print(told)     # 外双，内单
Monty_python = 'The language "Python" is named after Monty Python,not the snake'
print(Monty_python) # 外单，内双
Community = "One of python's strengths is its diverse and supportive community"
print(Community)    # 外双，内单单





# 使用方法去修改字符串的大小写：
# 方法是python可对数据执行的操作，每个方法后面都跟着一堆圆括号。
name = "ada lovelace"
print(name)            # 输出：ada lovelace
print(name.title())    # 输出：Ada LovelaceADA LOVELACE
# 在函数调用print()中，方法title()出现在这个变量的后面。
# 在name.title()中name后面的点号（.）让python对变量name执行方法tilte()指定的操作
# 方法title()以首字母大写的方式显示每个单词

# 案例：
# 全字母大写：upper()
names = "Ada Lovelace"
print(names.upper())    # 输出：ADA LOVELACE
# 全字母小写
names = "Ada Lovelace"
print(names.lower())    # 输出：ada lovelace