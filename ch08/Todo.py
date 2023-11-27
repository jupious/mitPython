class Todo:
    def __init__(self,count = 0):
        self.count = count
        self.todo_list = ['으아아아아' for _ in range(count)]
    def add_todo(self, something = '내용없음'):
        self.todo_list.append(something)
        self.count += 1
    def input_todo(self):
        self.todo_list.append(input("일정 입력"))
        self.count +=1
    def closest_todo(self):
        if self.count:
            print(self.todo_list[0])
        else:
            print("등록된 할 일이 없습니다.")
    def farthest_todo(self):
        if self.count:
            print(self.todo_list[-1])
        else:
             print("등록된 할 일이 없습니다.")
    def __str__(self):
        return ", ".join(self.todo_list)


#todo_test = Todo()
#이것 저것 테스트해보기
todo_test = Todo()
print('할일 추가 테스트')

todo_test.add_todo('이거 테스트코드 짜기')
todo_test.add_todo('점심먹기')
todo_test.add_todo('오후수업 듣기')
todo_test.add_todo('집에가기')
todo_test.add_todo('저녁먹기')
todo_test.add_todo()

todo_test.input_todo()

print('가장 가까운 일정=======')
todo_test.closest_todo()
print('가장 먼 일정==========')
todo_test.farthest_todo()
print('전체 일정')
print(todo_test)
