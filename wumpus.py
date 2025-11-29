import random

class WumpusWorld:
    def __init__(self, size):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.locations = [['.' for _ in range(size)] for _ in range(size)]
        self.counter = [[ 0 for _ in range(size)] for _ in range(size)]
        self.safe_wampus = set()
        self.safe_pit = set()
        self.agent_position = (0, 0)
        self.grid[0][0] = 'A'  # Agent's starting position
        self.safe_pit.add((0, 0))
        self.safe_pit.add((0, 1))
        self.safe_pit.add((1, 0))
        self.safe_wampus.add((0, 0))
        self.safe_wampus.add((0, 1))
        self.safe_wampus.add((1, 0))

    def place_pits(self, num_pits, pit_x, pit_y):
        for _ in range(num_pits):
            self.locations[pit_x][pit_y] = 'P'
            self.add_wind(pit_x, pit_y)

    def place_wumpus(self, w_x, w_y):
        self.locations[w_x][w_y] = 'W'
        self.add_stench(w_x, w_y)

    def place_gold(self, gold_x, gold_y):
        self.locations[gold_x][gold_y] = 'G'

    def add_wind(self, x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size and self.locations[nx][ny] == '.':
                self.locations[nx][ny] = 'B'

    def add_stench(self, x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size and self.locations[nx][ny] == '.':
                self.locations[nx][ny] = 'S'
            elif 0 <= nx < self.size and 0 <= ny < self.size and self.locations[nx][ny] == 'B':
                self.locations[nx][ny] = 'SB'

    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))
        print()

        for row in self.locations:
            print(' '.join(row))
        print()

        for row in self.counter:
            print(' '.join(str(row)))
        print()


    def move_agent(self):
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        possible_moves = []

        for move in moves:
            new_position = (self.agent_position[0] + move[0], self.agent_position[1] + move[1])
            if self.is_valid_move(new_position):
                possible_moves.append(new_position)

        if possible_moves:
            # پیدا کردن حرکت با کمترین مقدار counter
            min_counter_move = min(possible_moves, key=lambda pos: self.counter[pos[0]][pos[1]])
            self.grid[self.agent_position[0]][self.agent_position[1]] = '.'  # Clear previous position
            self.agent_position = min_counter_move
            self.counter[self.agent_position[0]][self.agent_position[1]] += 1
            self.grid[self.agent_position[0]][self.agent_position[1]] = 'A'  # Update new position


    # def move_agent(self):
    #     moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #     while True:
    #         # move = random.choice(moves)
    #         for move in moves:
    #             i, j = move
    #             adj = [[20, 1, 4],
    #                    [14, 1, 1]]
    #             adj.append([self.counter[self.agent_position[0]+i][self.agent_position[1]+j], self.agent_position[0]+i, self.agent_position[1]+j])
    #             adj2.sort(key= lambda x: x[0])
    #             # adj[self.counter[self.agent_position[0]+i][self.agent_position[1]+j]] = (self.agent_position[0]+i, self.agent_position[1]+j)
    #             # adj.append(self.counter[self.agent_position[0]+i][self.agent_position[1]+j])

    #         adj2 = dict(sorted(adj.items))
                
    #         new_position = (self.agent_position[0] + move[0], self.agent_position[1] + move[1])
    #         if self.is_valid_move(new_position) and  ( self.counter[new_position[0]][new_position[1]] <= 20 ):
    #             self.grid[self.agent_position[0]][self.agent_position[1]] = '.'  # Clear previous position
    #             self.agent_position = new_position
    #             self.counter[self.agent_position[0]][self.agent_position[1]] += 1
    #             self.grid[self.agent_position[0]][self.agent_position[1]] = 'A'  # Update new position
    #             break
    #         # moves.remove(move)


    def is_valid_move(self, position):
        x, y = position
        if 0 <= x < self.size and 0 <= y < self.size:
            return (position in self.safe_pit) and (position in self.safe_wampus)
        return False


    def update_safe_lists(self):
        x, y = self.agent_position
        if 'S' not in self.locations[x][y]:
            surroundings = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for nx, ny in surroundings:
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    self.safe_wampus.add((nx, ny))
        if 'B' not in self.locations[x][y]:
            surroundings = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for nx, ny in surroundings:
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    self.safe_pit.add((nx, ny))
        # surroundings = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        # for nx, ny in surroundings:
        #     if 0 <= nx < self.size and 0 <= ny < self.size and self.locations[nx][ny] != 'W' and self.locations[nx][ny] != 'P':
        #         if self.locations[nx][ny] != 'B':
        #             self.safe_pit.add((nx, ny))
        #         if self.locations[nx][ny] != 'S':
        #             self.safe_wampus.add((nx, ny))

    def play(self):
        self.update_safe_lists()
        mamad = 1
        while self.locations[self.agent_position[0]][self.agent_position[1]] != 'G' and mamad:
            self.update_safe_lists()
            self.move_agent()
            print('safe_pits: ',self.safe_pit)
            print('safe_wampus: ', self.safe_wampus)
            print("Agent moved to:", self.agent_position)
            self.display_grid()
            if self.locations[self.agent_position[0]][self.agent_position[1]] == 'P':
                print("Agent fell into a pit!")
                break
            if self.locations[self.agent_position[0]][self.agent_position[1]] == 'W':
                print("Agent encountered the Wumpus!")
                break
            for i in range ( self.size ):
                for j in range ( self.size ):
                    if self.counter[i][j] == 50 :
                        mamad = 0
                        break
        if self.locations[self.agent_position[0]][self.agent_position[1]] == 'G' and mamad:
            print("Agent found the gold!")
        elif not mamad : 
             print ('timam tamoom shod')

# تعریف سایز صفحه بازی
size = 4
world = WumpusWorld(size)

# جایگذاری عناصر
world.place_pits(1, 2, 2)
world.place_wumpus(2, 0)
world.place_gold(3, 1)

# نمایش صفحه بازی
world.display_grid()

# اجرای بازی
world.play()