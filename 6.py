class Queue:
    def __init__(self):
        self.elements = []

    def empty(self):
        self.elements = []

    def show(self):
        return self.elements

    def add(self, content):
        self.elements.append(content)

    def delite(self, s):
        try:
            self.elements.pop(self.elements.index(s))
        except:
            print("eroor delite task")


class TaskBoard:
    def __init__(self):
        self.main_queue = Queue()
        self.remakes = Queue()
        self.log = []

    def new_task(self, s):
        self.main_queue.add(s)

    def done(self, s):
        try:
            self.main_queue.delite(s)
            self.log.append(s)
        except:
            print("not found")

    def done_from_remake(self, s):
        try:
            self.remake.delite(s)
            self.log.append(s)
        except:
            print("not found")

    def remake(self, s):
        try:
            self.remakes.add(s)
            self.log.pop(self.log.index(s))
        except:
            print("not found")

    def show(self):
        return f"{self.remakes.show()} - переделать \n{self.log} - сделано \n {self.main_queue.show()} - надо сделать"


queue = TaskBoard()
queue.new_task("test1")
queue.new_task("test2")
queue.new_task("test3")
queue.new_task("test4")
queue.new_task("test5")
queue.done("test5")
queue.done("test4")
queue.remake("test5")
print(queue.show())
