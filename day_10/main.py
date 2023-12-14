pipe_map = []

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __eq__(self, value: object) -> bool:
        return (self.x == value.x and self.y == value.y)

class Pipe:
    def __init__(self, symbol, pos):
        self.symbol = symbol
        self.pos: Vector = pos
        self.directions: list[Vector] = []
        self.connections: list[Pipe] = []
        self.distance = None

        if self.symbol == '|':
            self.directions.extend([Vector(0, -1), Vector(0, 1)])
        elif self.symbol == '-':
            self.directions.extend([Vector(1, 0), Vector(-1, 0)])
        elif self.symbol == 'L':
            self.directions.extend([Vector(0, -1), Vector(1, 0)])
        elif self.symbol == 'J':
            self.directions.extend([Vector(0, -1), Vector(-1, 0)])
        elif self.symbol == '7':
            self.directions.extend([Vector(0, 1), Vector(-1, 0)])
        elif self.symbol == 'F':
            self.directions.extend([Vector(0, 1), Vector(1, 0)])
        elif self.symbol == 'S':
            self.directions.extend([Vector(0, -1), Vector(0, 1), Vector(1, 0), Vector(-1, 0)])

def inversed_vector(vec: Vector) -> Vector:
    return Vector(-vec.x, -vec.y)

def get_connections(pipe: Pipe):
    connections: list[Pipe] = []

    if pipe.symbol == '.':
        return []

    for direction in pipe.directions:
        try:
            new_y = pipe.pos.y + direction.y
            new_x = pipe.pos.x + direction.x
            print(f"Dir: {direction.x, direction.y} -> {new_x, new_y}")
            if new_y < 0 or new_x < 0:
                continue

            adjacent_pipe: Pipe = pipe_map[new_y][new_x]
            print(f"Adjacent pipe found {adjacent_pipe.symbol}: {new_x, new_y}, current pipe {pipe.symbol}: {pipe.pos.x, pipe.pos.y}")

            if inversed_vector(direction) in adjacent_pipe.directions and not adjacent_pipe in connections:
                connections.append(adjacent_pipe)
        except IndexError:
            continue
    
    return connections

def check_dist(current_pipe: Pipe, prev_pipe: Pipe):
    for connection in current_pipe.connections:
        if connection.distance != None:
            continue
        connection.distance = prev_pipe.distance + 1
        print(connection.distance)
        check_dist(connection, current_pipe)

with open("input.txt") as f:
    for y, line in enumerate(f):
        row = []
        tiles = list(line.strip())
        for x, tile in enumerate(tiles):
            new_pipe = Pipe(tile, Vector(x, y))
            row.append(new_pipe)
        
        pipe_map.append(row)

start_pipe: Pipe = None

for row in pipe_map:
    for pipe in row:
        connections = get_connections(pipe)
        pipe.connections = connections
        if pipe.symbol != '.':
            print(f"Pipe {pipe.symbol} has the connections: {[x.symbol for x in connections]}\n")
            if pipe.symbol == 'S':
                start_pipe = pipe

start_pipe.distance = 0
current_pipe = start_pipe

#list of pipes in loop
while True:
    for connection in current_pipe.connections:
        if connection.distance != None:
            continue
        connection.distance = current_pipe.distance + 1
        current_pipe = connection
        print(connection.distance)

highest = 0
for row in pipe_map:
    for pipe in row:
        if pipe.distance == None:
            print('.', end='')
        else:
            print(pipe.distance, end='')
            if pipe.distance > highest:
                highest = pipe.distance
    print("\n")

print(f"Highest distance: {highest}")