with open("input.txt") as f:
    card_public, door_public = [int(x) for x in f.readlines()]


def transform_once(subject: int, num: int) -> int:
    return (subject * num) % 20201227


num = 1
i = 0
while num != door_public:
    i += 1
    num = transform_once(7, num)

door_loop = i

num = 1
for _ in range(door_loop):
    num = transform_once(card_public, num)

print(num)
