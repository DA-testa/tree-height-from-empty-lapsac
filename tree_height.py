#Lauma Gailite 2. grupa
import sys
import threading

def compute_height(n, parents):
    nodes = [[] for _ in range(n)]
    for i in range(n):
        p = parents[i]
        if p == -1:
            root = i
        else:
            nodes[p].append(i)

    # koka augstums 
    def compute_depth(node):
        if not nodes[node]:
            return 1
        max_depth = 0
        for child in nodes[node]:
            depth = compute_depth(child)
            max_depth = max(max_depth, depth)
        return max_depth + 1

    return compute_depth(root)

def main():
    input_type = input()

    if 'I' in input_type:
        n = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)
        print(height)
    elif 'F' in input_type:
        filename = input()
        with open("test/" + filename, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            height = compute_height(n, parents)
            print(height)
    else:
        print("Invalid input, try again.")
        exit()

sys.setrecursionlimit(10**7)
threading.stack_size(2**27) 
threading.Thread(target=main).start()
