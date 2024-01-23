
import random

class Player:
    def __init__(self, name, strength, health, intellect, item):
        self.name = name
        self.strength = strength
        self.health = health
        self.intellect = intellect
        self.item = item

    def attack(self):
        if self.item == "Меч":
            return random.randint(1, 10) + self.strength
        elif self.item == "Магический всплеск":
            return random.randint(1, 10) + self.intellect
        elif self.item == "Жар солнца":
            return random.randint(1, 10) + self.strength + self.intellect

def print_status(player, slime):
    print(f"{player.name}: Сила - {player.strength}, Жизни - {player.health}, Интеллект - {player.intellect}")
    print(f"Арториас: Жизни - {slime}")

def main():
    print("Выберите свой класс:")
    print("1. Мечник")
    print("2. Маг")
    print("3. Пиромант")

    choice = input("Введите номер класса: ")

    if choice == "1":
        player = Player("Мечник", 10, 8, 3, "Меч")
    elif choice == "2":
        player = Player("Маг", 2, 4, 12, "Магический всплеск")
    elif choice == "3":
        player = Player("Пиромант", 4, 6, 8, "Жар солнца")
    else:
        print("Неверный выбор. Завершение игры.")
        return

    print(f"Вы выбрали {player.name}!")
    print(f"Характеристики: Сила - {player.strength}, Жизни - {player.health}, Интеллект - {player.intellect}")
    print(f"Ваш предмет: {player.item}")

    while True:
        input("Нажмите Enter, чтобы начать свой путь...")

        slime_health = 15 

        print("Вы встретили Арториаса. Начинается бой!")

        while player.health > 0 and slime_health > 0:
            print_status(player, slime_health)

            attack_result = player.attack()

            print(f"Вы атакуете с использованием {player.item} и наносите {attack_result} урона!")

            if player.item == "Магический всплеск" and attack_result >= 4:
                print("Арториас погиб! Вы выиграли!")
                break
            elif player.item == "Жар солнца" and attack_result >= 9:
                print("Арториас погиб! Вы выиграли!")
                break
            else:
                slime_attack = random.randint(1, 10)
                player.health -= slime_attack
                print(f"Арториас атакует вас и наносит {slime_attack} урона!")

        if player.health <= 0:
            print("Вы проиграли. Ваши жизни закончились.")
        else:
            print_status(player, slime_health)

        play_again = input("Хотите начать новый бой? (да/нет): ")
        if play_again.lower() != "да":
            break

if __name__ == "__main__":
    main()
