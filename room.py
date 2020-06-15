from pynput.keyboard import Key, Listener
from time import sleep

class room:
    def __init__(self, size):
        self.size = size
        self.room = []
        
    def make_room(self):
        for columns in range(0, self.size):
            column = []
            self.room.append(column)
            for row in range(0, self.size):
                column.append('')
    
    def change_object_position(self, object):
        self.room[object.position[0]][object.position[1]] = ''
    
    def add_object_to_room(self, object):
        self.room[object.position[0]][object.position[1]] = object
    
    def show_room(self):
        for row in self.room:
            print(row)

class player:
    def __init__(self, name, room):
        self.position = [0 , 0]
        self.name = name
        self.room = room
        self.room.add_object_to_room(self)
        
    def on_press(self, key):
        if key.char == True and key.char == 'w' or key.char ==  'a' or key.char ==  's' or key.char ==  'd':
            self.room.change_object_position(self)
            if key.char == 'w':
                self.position[0] -= 1
            if key.char == 's':
                self.position[0] += 1
            if key.char == 'd':
                self.position[1] += 1
            if key.char == 'a':
                self.position[1] -= 1
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
        
                
# Collect events until released


room1 = room(10)
room1.make_room()
player1 = player('boi', room1)


moves = 0
player1.start_player()
while True:
    sleep(2)
    room1.show_room()