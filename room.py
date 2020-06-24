from pynput.keyboard import Key, Listener
from time import sleep
import os

class Room:
    def __init__(self, size):
        self.size = size
        self.room = []
        self.walls = []
        
    def make_room(self):
        for columns in range(0, self.size):
            column = []
            self.room.append(column)
            for row in range(0, self.size):
                column.append('')
        self.make_walls()
        for wall in self.walls:
            for wall_cell in wall.positions:
                self.room[wall_cell[0]][wall_cell[1]] = wall.icon

    def make_walls(self):
        wall1 = Wall([0,0], [0,9])
        wall2 = Wall([0,9], [9,9])
        wall3 = Wall([9,0], [9,9])
        wall4 = Wall([0,0], [9,0])
        self.walls = [wall1, wall2, wall3, wall4]
    
    def change_object_position(self, object):
        self.room[object.position[0]][object.position[1]] = ''
    
    def add_object_to_room(self, object):
        self.room[object.position[0]][object.position[1]] = object.icon
    
    def show_room(self):
        for row in self.room:
            print(row)

class Player:
    def __init__(self, name, room):
        self.position = [1 , 1]
        self.name = name
        self.room = room
        self.icon = 'P'
        self.room.add_object_to_room(self)
    
    def check_collision_wall(self):
        for wall in self.room.walls:
            for wall_cell in wall.positions:
                if wall_cell == self.position:
                    return True
        return False
        
    def on_press(self, key):
        if key.char == 'a' or key.char == 'w' or key.char == 's' or key.char == 'd':
            self.room.change_object_position(self)
            last_position = self.position
            if key.char == 'w':
                self.position = [self.position[0]-1, self.position[1]]
            if key.char == 's':
                self.position = [self.position[0]+1, self.position[1]]
            if key.char == 'd':
                self.position = [self.position[0], self.position[1]+1]
            if key.char == 'a':
                self.position = [self.position[0], self.position[1]-1]
            if self.check_collision_wall() == False:
                self.room.add_object_to_room(self)
            if self.check_collision_wall() == True:
                self.position = last_position
                self.room.add_object_to_room(self)
        else:
            pass
    
    def on_release(self, key):
        if key == Key.esc:
            # Stop listener
            return False    
        
    def start_player(self):
        listener = Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()

class Wall:
    def __init__(self, start_cor, end_cor):
        self.positions = []
        self.icon = 'w'
        for y in range(start_cor[0], end_cor[0]+1):
            for x in range(start_cor[1], end_cor[1]+1):    
                self.positions.append([y,x])
        print(self.positions)




room1 = Room(10)
room1.make_room()
player1 = Player('boi', room1)


moves = 0
player1.start_player()
while True:
    room1.show_room()
    sleep(0.2)
    os.system('cls')