def attack(self):
        if self.item == "Меч":
            return random.randint(1, 10) + self.strength
        elif self.item == "Магический всплеск":
            return random.randint(1, 10) + self.intellect
        elif self.item == "Жар солнца":
            return random.randint(1, 10) + self.strength + self.intellect
