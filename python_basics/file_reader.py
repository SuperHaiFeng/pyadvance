
# 关键字with在不再需要访问文件后将其关闭 Python自会在合适的时候自动将其关闭 
# 也可以手动调用open和close方法，但是容易出现错误
read_file = 'pi_digits.txt'
try:
	with open(read_file) as file_object:
		# 直接读取所有
		#contents = file_object.read()
		#print(contents.strip())
		# 逐行读取
		for line in file_object:
			#print('line---' + line.strip())
			# 将每行存到一个列表中, readlines也是一次性读取所有
			lines = file_object.readlines()
except FileNotFoundError:
	print('file not exist')


pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)

# 写入文件 'w'为写入文件，'r'为只读，'r+'为可读可写 'a'附加模式
# 此种方式写入文件，在打开是会清空文件内容
write_file = 'write_file.txt'
with open(write_file, 'w') as file_object:
	file_object.write('I love programming.\n')

# 附加文件内容， 此种方式不会清空文件内容
with open(write_file, 'a') as file_object:
	file_object.write('I love Swift\n')


# 保存数据
import json

numbers = [2,3,4,4,5,6,7]
with open('numbers.json', 'w') as f_obj:
	json.dump(numbers, f_obj)

with open('numbers.json') as f_obj:
	nums = json.load(f_obj)
	print(nums)


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
    	username = get_new_username()
    	print("We'll remember you when you come back, " + username + "!")

greet_user()

