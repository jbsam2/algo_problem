key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]

dim3key = [list(zip(*key))]
for _ in range(3):
    dim3key.append(list(zip(*dim3key[-1])))

print(dim3key)