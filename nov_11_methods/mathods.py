# 11/11/2024
# self bhi ak constructor hai   instance method hoga


class Rbi:
    def __init__(self):
        print("hello abhi")
    @classmethod
    def new1(cls):
        print("welcom")
obj1=Rbi()
obj1.new1()
        