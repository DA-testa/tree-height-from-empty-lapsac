import sys
import threading
import numpy as np

def compute_height(n, parents):
    tree = np.empty((n,), dtype = object)
    root == -1

    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            if tree[parent] is None:
                tree[parent] = [i]
            else:
                tree[parent].append(i)

    def augst(node):
        if tree[node] is None:
            return 1
        return max([height(child) for child in koks[node]], default = 0 ) +1

def main():
    #input_type = input("input 'i' or 'f': ")

    if input_type == 'i':
        n = int(input("Enter the number of elements: "))
        parents = list(map(int, input("enter parents of nodes")))

    elif input_type == 'f':
        filename = input("Enter file name: ").strip()
        if 'a' in filename:
            print("File name can't contain letter 'a'. ")
            return
        
        with open(f"./test/{filename}", 'r') as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().split()))

    else:
        print("invalid input. ")
        return

    print(compute_height(n, parents))


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
