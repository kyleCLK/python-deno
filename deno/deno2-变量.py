# 变量
message = "hello world"
print(message) # 输出hello world
# 扩展一下：
message = "hello python"
print(message) # 输出hello python
# 在程序中，可以随时修改变量的值，而python会始终记录变量的最新值。

# 使用变量名错误：
#print(mesaage)
# Traceback (most recent call last):          回溯（最近一次通话最后一次）
#   File "E:/python学习案例/python-deno/deno/deno2-变量.py", line 9, in <module>
#     print(mesaage)
# NameError: name 'mesaage' is not defined    名称错误：未定义名称“mesaage”
# 在程序存在错误时，python解释器会帮你找到问题，程序无法运行时，解释器将提供一个traceback
# traceback是一条记录，指出了解释器尝试运行代码时，在什么地方出现了问题。





# 变量名的使用规范：
# 1、变量名只能包含字母、数字、下划线
# 2、变量名能以字母、下划线开头，但不能以数字开头
# 3、变量名不能包含空格，但可以使用下划线来分隔其中的单词
# 4、不能将关键字和函数名作为变量名
# 5、变量名应该短洁，见字识意
# 案例1：
name = "张三"         #输出成功
name1 = "李四"        #输出成功
name_2 = "王五"       #输出成功
#name@ = "刘六"       #输出失败，报错：
                     # SyntaxError: invalid syntax    语法:无效语法
print(name)
print(name1)
print(name_2)
#print(name@)         #输出失败，报错：
                      # SyntaxError: invalid syntax    语法:无效语法
# 案例2：
sex = "男"            #输出成功
_sex = "女"           #输出成功
#1sex = "人妖"        #输出失败，报错：
                     # SyntaxError: invalid syntax    语法:无效语法
print(sex)
print(_sex)
#print(1sex)          #输出失败，报错：
                      # SyntaxError: invalid syntax    语法:无效语法