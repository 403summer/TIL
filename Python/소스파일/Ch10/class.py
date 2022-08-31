#데이터
names = ["Messi", "Ramos", "Ronaldo", "Park", "Buffon"]
positions = ["MF", "DF", "CF", "WF", "GK"]
numbers = [10, 4, 7, 13, 1]

#이차원 리스트
players = [[name, position, number] for name, position, number in zip(names, positions, numbers)]
print(players)
print(players[0])

#전체 SoccerPlayer 코드
class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    def change_back_number(self, new_number):
        print("선수의 등 번호를 변경한다: From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number
    def __str__(self):
        return "Hello, My name is %s. I play in %s in center." % (self.name, self.position)

# 클래스-인스턴스
player_objects = [SoccerPlayer(name, position, number) for name, position, number in zip(names, positions, numbers)]
print(player_objects[0])
