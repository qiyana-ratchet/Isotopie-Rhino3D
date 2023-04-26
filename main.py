import rhinoscriptsyntax as rs
import random as r

X_MINIMUM = Y_MINIMUM = 0
X_MAXIMUM = 10
Y_MAXIMUM = 14


# class
class Walker:
    def __init__(self):
        self.last_choice = None  # 이전 단계의 방향
        self.x = 0
        self.y = 0
        self.z = 0

    def point(self):
        shape = rs.AddPoint(self.x, self.y, self.z)
        return shape

    def get_current(self):  # 현재 좌표 가져오기
        return [self.x, self.y, self.z]

    def step(self):
        flag = True  # 재시도 플래그
        x_y_count = 0  # x,y 축으로 이동 시도한 횟수
        print("Current:", self.x, self.y, self.z)
        while (flag):  # 이동 성공할 때까지 반복
            choiceLength = r.randint(1, 1)  # 한번에 이동할 거리 1~n
            if self.last_choice is None or self.last_choice == 0:  # x축 + 방향
                if x_y_count < 1:  # x,y 축으로 이동하지 않은 경우
                    choice = r.choice([0, 2, 3])  # 우선적으로 x,y 축 이동
                else:
                    choice = r.choice([2, 3, 4, 5])  # z축 이동 가능
                self.last_choice = choice  # 이동방향 저장
            elif self.last_choice == 1:  # x축 - 방향
                if x_y_count < 1:
                    choice = r.choice([1, 2, 3])
                else:
                    choice = r.choice([2, 3, 4, 5])
                self.last_choice = choice
            elif self.last_choice == 2:  # y축 + 방향
                if x_y_count < 1:
                    choice = r.choice([0, 1, 2])
                else:
                    choice = r.choice([0, 1, 4, 5])
                self.last_choice = choice
            elif self.last_choice == 3:  # y축 - 방향
                if x_y_count < 1:
                    choice = r.choice([0, 1, 3])
                else:
                    choice = r.choice([0, 1, 4, 5])
                self.last_choice = choice
            elif self.last_choice in [4, 5]:  # z축 +, - 방향
                choice = r.choice([0, 1, 2, 3])
                self.last_choice = choice

            print("방향:", choice, "거리:", choiceLength)

            if choice == 0:
                if self.x + choiceLength <= X_MAXIMUM:
                    if [self.x + choiceLength, self.y, self.z] not in visited:  # 이전에 방문했었는지 검사
                        self.x += choiceLength  # 이동
                        flag = False  # while문 탈출
                    else:
                        x_y_count += 1  # x, y로 이동 시도
                else:
                    x_y_count += 1  # x, y로 이동 시도
                    print("범위 초과")
            elif choice == 1:
                if self.x - choiceLength >= X_MINIMUM:
                    if [self.x - choiceLength, self.y, self.z] not in visited:
                        self.x -= choiceLength
                        flag = False
                    else:
                        x_y_count += 1
                else:
                    x_y_count += 1
                    print("범위 초과")
            elif choice == 2:
                if self.y + choiceLength <= Y_MAXIMUM:
                    if [self.x, self.y + choiceLength, self.z] not in visited:
                        self.y += choiceLength
                        flag = False
                    else:
                        x_y_count += 1
                else:
                    x_y_count += 1
                    print("범위 초과")
            elif choice == 3:
                if self.y - choiceLength >= Y_MINIMUM:
                    if [self.x, self.y - choiceLength, self.z] not in visited:
                        self.y -= choiceLength
                        flag = False
                    else:
                        x_y_count += 1
                else:
                    x_y_count += 1
                    print("범위 초과")
            elif choice == 4 or choice == 5:  # z축 +, - 방향
                z_count = 1  # z축으로 이동한 횟수
                while True:
                    if self.z <= 0:  # 최대한 0에 가깝게 조작
                        self.z += z_count  # 겹치는 경우 이동 거리 증가
                    else:
                        self.z -= z_count
                    if [self.x, self.y, self.z] not in visited:
                        flag = False
                        break
                    z_count += 1
            else:
                print("잘못 입력하셨습니다.")


w = Walker()

pList = [[0, 0, 0]]
visited = [[0, 0, 0]]  # 방문했었던 좌표들
for t in range(Time):
    print("Time:", t + 1)
    w.step()
    pList.append(w.point())
    visited.append(w.get_current())  # 방문한 좌표를 저장

# print(visited)
# visited.sort(reverse=True, key=lambda x: x[2])
# print(visited)

a = pList
