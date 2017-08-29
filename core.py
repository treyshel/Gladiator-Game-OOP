from random import randint


class Gladiator:
    """ a gladiator that has a name, health, rage, high_damage, low_damage"""

    def __init__(self, name, health, rage, low_damage, high_damage):
        """ (Gladiator, str, str, str, str, str) -> NoneType
                ***create Gladiator***
        """
        self.name = name
        self.health = health
        self.rage = rage
        self.low_damage = low_damage
        self.high_damage = high_damage

    def normal_punch(self, other):
        """ (Gladiator) attacks for a random damage dealt
            ***higher the rage, higher chance for crit hit
        """
        random_damage = randint(self.low_damage, self.high_damage)
        if randint(1, 100) <= self.rage:
            other.health -= (2 * random_damage)
            self.rage = 0
            message = '\nCRIT HIT OF {}'.format(2 * random_damage)
        else:
            other.health -= random_damage
            self.rage += 15
            message = '\nHIT OF {}'.format(random_damage)
        other.health = max(0, other.health)
        return message

    def mega_kick(self, other):
        """ (Gladiator) kicks for a damage of 25 when rage is 40"""
        if self.rage >= 40:
            other.health -= 25
            self.rage = 0

    def hard_uppercut(self, other):
        """ (Gladiator) sacrafices 35 health to uppercut for a damage of 35"""
        if self.health >= 36:
            other.health -= 35
            self.health -= 35

    def cut(other):
        """ (Gladiator) can cut as a finisher if the opponents health is below 10 """
        if other.health < 10:
            other.health = 0

    def is_dead(self):
        """ (Gladiator) is dead when health reaches 0"""
        if self.health <= 0:
            return True
        return False

    def heal(self):
        """ (Gladiator) can add +5 to health but costs 10 rage"""
        if self.rage >= 10:
            self.rage = max(self.rage - 10, 0)
            self.health = min(self.health + 5, 100)

    def skip(self):
        """ (Gladiator) skips to gain +20 rage"""
        self.rage += 20

    def __repr__(self):
        """ return a string representation of this Gladiator
        >>> gladiator = Gladiator('Kapo', '100', '0', '5', '25')
        >>> gladiator.__repr__()
        'Gladiator Kapo --> | 100 HP | 0 RAGE | 5 DAMAGE LOW | 25 DAMAGE HIGH |'
        """
        return '{} --> | {} HP | {} RAGE | {} DAMAGE LOW | {} DAMAGE HIGH |'.format(
            self.name, self.health, self.rage, self.low_damage,
            self.high_damage)

    def __str__(self):
        """ return a string representation of this Gladiator
        >>> gladiator = Gladiator('Kapo', '100', '0', '5', '25')
        >>> gladiator.__str__()
        'Gladiator Name: Kapo --> | 100 HP | 0 RAGE |'
        """
        return '\nAfter last move: {} --> | {} HP | {} RAGE |'.format(
            self.name, self.health, self.rage)


def rand_damage(damage_1, damage_2):
    d1 = randint(damage_1, damage_2)
    d2 = randint(damage_1, damage_2)
    return min(d1, d2), max(d1, d2)
