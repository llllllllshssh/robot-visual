"""
TASK1 类与对象演示：机器人战车
体现：类与对象、封装、继承、多态
"""

class Robot:
    def __init__(self, name, speed):
        # 封装：把名字、速度封装为对象内部属性，外部不直接乱改
        self._name = name
        self.speed = speed

    def move(self):
        print(f"{self._name} 以 {self.speed} 的速度移动")

    def get_name(self):
        # 封装：对外提供读取私有属性的接口
        return self._name


class TankRobot(Robot):
    # 继承：子类继承父类 Robot 的属性和方法
    def __init__(self, name, speed, cannon):
        super().__init__(name, speed)
        self.cannon = cannon

    def move(self):
        # 多态：重写父类 move，坦克有自己的行进方式
        print(f"坦克 {self.get_name()} 履带行进，火炮：{self.cannon}")


class ScoutRobot(Robot):
    # 继承：侦察车同样继承 Robot
    def move(self):
        # 多态：重写 move，侦察车高速巡逻
        print(f"侦察车 {self.get_name()} 高速巡逻")


if __name__ == "__main__":
    # 由类实例化出具体对象
    r1 = TankRobot("主战坦克", 20, "120mm 主炮")
    r2 = ScoutRobot("侦察小车", 40)

    robots = [r1, r2]
    for rob in robots:
        rob.move()   # 多态：同一个 move 接口，不同对象执行不同逻辑
