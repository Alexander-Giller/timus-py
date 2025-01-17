class Node:
    def __init__(self, id):
        self.id = id
        self.color = 0
        self.friends = []


n = int(input())
nodes = dict()

for i in range(n):
    input_node = Node(i + 1)
    nodes[i + 1] = input_node

    input_args = [int(j) for j in input().split(' ')]
    for friend in input_args:
        if friend == 0:
            break
        input_node.friends.append(friend)


def colorized(node: Node):
     if node.color == 0:
         node.color = 1

     nodes_to_process = set()

     for friend_id in node.friends:
         friend = nodes[friend_id]
         if friend.color == 0:
             if node.color == 1:
                 friend.color = 2
             else:
                 friend.color = 1
             nodes_to_process.add(friend)

     for node_to_process in nodes_to_process:
         colorized(node_to_process)


for node in nodes.values():
    if node.color == 0:
        colorized(node)


red = set()
black = set()

res = -1

for node in nodes.values():
    if len(node.friends) == 0:
        res = 0
        break
    if node.color == 2:
        red.add(node)
    else:
        black.add(node)


if res == 0:
    print(0)
else:
    print(len(red))
    for i in red:
        print(i.id, end=' ')



