x = 20
y = 21
z = 22

desk_x = x // 2
desk_y = y // 2
desk_z = z // 2
if desk_x % 2 > 0:
    desk_x = desk_x + 1
if desk_y % 2 > 0:
    desk_y = desk_y + 1
if desk_z % 2 > 0:
    desk_z = desk_z + 1

print(desk_x + desk_y + desk_z)