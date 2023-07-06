## 字符串转换
message = " hello python world!  "
message = message.title()
print(message)
message = message.upper()
print(message)
message = message.lower()
print(message)

# 去掉字符串末尾空格
message = message.rstrip()
# 去掉字符串前段尾空格
message = message.lstrip()
# 去掉两端空白
message = message.strip()

print('2的三次方'+str(2 ** 3))

age = 23
message = "Happy " + str(age) + "rd Birthday!"

print(message)

bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'hello', 'python']
print(bicycles[0])
bicycles.append('append')
print(bicycles)
bicycles.insert(2, ' ')
print(bicycles)
print('删除')
del bicycles[1]
print(bicycles)
redline = bicycles.pop(2)
print(redline)
print(bicycles)
append = bicycles.remove('append')

print('永久排序（改变原来列表顺序）')
bicycles.sort()
print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)
print('临时排序（不改变原来列表顺序)')
print(sorted(bicycles))
print(sorted(bicycles, reverse=True))
print(bicycles)

bicycles.reverse()
print('列表长度: '+ str(len(bicycles)))

for name in bicycles:
	print('for循环'+name)

for x in range(1,5):
	print('for循环数字'+str(x))

number = list(range(2,11,2))
print('将range转换成list偶数列表'+str(number))

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print('数组最大值'+str(max(digits)))
print('数组最小值'+str(min(digits)))
print('数组和'+str(sum(digits)))

squares = [value**2 for value in range(1,11)]
print('列表解析'+str(squares))

print('切片0-2'+str(squares[0:3]))
print('切片2-结尾'+str(squares[1:]))
print('切片末尾3个'+str(squares[-3:]))

for name in squares[:3]:
	print('遍历数组前三个切片'+str(name))

copysquares = squares[:]
copysquares.append(10)
print('使用切片复制列表'+str(copysquares))

dimensions = (200, 50)
print('元组'+str(dimensions[0]))

cars = ['audi', 'bmw', 'subaru', 'Toyota']
for car in cars:
	if car == 'bmw' or car == 'subaru':
		print(car.title())
	elif car == 'Toyota':
		print(car.lower())
	else:
		print(car.upper())

print('bmw是否包含在列表中'+str('bmw' in cars))
print('使用not in 判断byd是否包含在列表中'+str('byd' not in cars))

alien_0 = {'color': 'green', 'points': 5}

print('访问字典' + alien_0['color'])
alien_0['x_position'] = 0
del alien_0['color']

for key, value in alien_0.items():
	print('key=' + key + '   value=' + str(value))

for key in sorted(alien_0.keys()):
	print(key)

for value in set(alien_0.values()):
	print(value)

#msg = input("Tell me something, and I will repeat it back to you: ")
#print(msg)

# username默认值jenny
def greet_user(username='jenny'):
	print('hello ' + username.title())

greet_user('joy')

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print('调用返回值函数' + str(musician))


def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print('传入任意数量的参数' + str(toppings))

make_pizza('pepperoni')
make_pizza('mushrooms', 87, 'extra cheese')


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


# 倒入模块 只导入某个模块的话，需要使用pizza.make_pizza调用函数
# import pizza
# 开可以将模块重命名
# import pizza as p
# 还可以调用模块中所有的函数，直接调用函数就行
# from pizza import *
# 导入指定函数
# from pizza import make_pizza
# 如果重名还可以这么导入
from pizza import make_pizza as mp

mp(10, 'mushrooms', 'green peppers', 'extra cheese')

# 导入Dog类
from model.Dog import *

dog = Dog('paccy', 2)
dog.name = 'oh, my name changed'
print(dog.name.title() + 'this year' + str(dog.age) + 'old')

alaska = Alaska('kun chiken', 3)
alaska.funny()
alaska.roll_over()

# OrderedDict是有顺序的字典
from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['joy'] = 'python'
favorite_language['andy'] = 'swift'

for name, language in favorite_language.items():
	print(name.title() + 'like study' + language + 'language')


# 异常处理
try:
	print(5/0)
except ZeroDivisionError:
	print("you can't divide by zero")

try:
	with open('alice.txt') as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	print('file not exist')
