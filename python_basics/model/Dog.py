
"""一个描述Dog的类"""
class Dog(): 
    """一次模拟小狗的简单尝试""" 

    def __init__(self, name, age): 
        """初始化属性name和age"""
        self.name = name 
        self.age = age

    def sit(self): 
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


class Alaska(Dog):

    def funny(self):
        self.hair = '黑加白'
        print(self.name.title() + '太搞笑了' + self.hair)

    def roll_over(self):
        super().roll_over()
        print(self.name.title() + '打滚像一只鸡')