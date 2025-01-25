# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import matplotlib.pyplot as plt
x = int(input())
y = int(input())
y = 8-y
x = x-1
board_size = 8
fig, ax = plt.subplots()
data = [[1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1]]
plt.xticks(range(board_size), labels=[f"{i}" for i in "ABCDEFGH"])
plt.yticks(range(board_size), labels=[f"{8-i}" for i in range(board_size)])
Circle = plt.Circle((x, y),0.4, color='red')
ax.add_patch(Circle)
queen_position = (x,y)
for i in range(board_size):
    plt.plot([queen_position[0], queen_position[0]], [0, board_size], color='red', linestyle='--')
    plt.plot([0, board_size], [queen_position[1], queen_position[1]], color='red', linestyle='--')
    plt.plot([0, board_size], [queen_position[1] - (queen_position[0]), queen_position[1]  + (board_size - (queen_position[0]))], color='red', linestyle='--')
    plt.plot([0, board_size], [queen_position[1] + (queen_position[0]), queen_position[1] - (board_size - (queen_position[0]))], color='red', linestyle='--')
    break
plt.imshow(data, cmap='binary')
plt.show()