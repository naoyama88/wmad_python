class MyCustomList:
    def __init__(self):
        self.my_list = []

    def addItem(self, new_num):
        for num in self.my_list:
            if new_num == num:
                return
        self.my_list.append(new_num)

    def calculateSum(self):
        return sum(self.my_list)

    def calculateMax(self):
        return max(self.my_list)

    def printList(self):
        print(self.my_list)


class TestClass:
    @staticmethod
    def testMyCustomList():
        my_custom_list = MyCustomList()
        my_custom_list.addItem(1)
        my_custom_list.addItem(2)
        my_custom_list.addItem(3)
        # print [1, 2, 3]
        print('print [1, 2, 3]')
        my_custom_list.printList()
        my_custom_list.addItem(2)
        # print [1, 2, 3]
        print('print [1, 2, 3]')
        my_custom_list.printList()

        my_custom_list.addItem(5)
        my_custom_list.addItem(4)
        sum_num = my_custom_list.calculateSum()
        max_num = my_custom_list.calculateMax()
        # print 15
        print('sum is', sum_num)
        # print 5
        print('max is', max_num)

