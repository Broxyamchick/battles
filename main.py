from Character import Character
from berserk import Berserk
from vampire import Vampire

player1 = Vampire('Vasya', damage=1)
player2 = Berserk('Berserk', health=50, damage=2)

print(player1)
print(player2)

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    vampire_damage = player1.damage
    player1.healing(player1)
    berserk_damage = player2.attack(player1)




    print(f'{player1.name} нанес {vampire_damage} урона')
    print(f'{player1.name} восстановил 1 здоровья')
    print(f'{player2.name} нанес {berserk_damage} урона')
    print(player1)
    print(player2)

