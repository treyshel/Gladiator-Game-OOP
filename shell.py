import core


def attacker_decision(name_of_gladiator):
    attack_choices = '\n{}, it\'s your move...\n\t- [N]ormal Punch\n\t\t*random damage between high and low damage\n\t- [M]ega Kick\n\t\t*kicks for a damage of 25 when rage is 40\n\t- [U]ppercut\n\t\t*sacrafices 35 health to uppercut for a damage of 35\n\t- [H]eal\n\t\t*add +5 to health but costs 10 rage\n\t- [S]kip\n\t\t*skips for +20 rage\n\t- [C]ut\n\t\t*cut as a finisher if the opponents health is below 10\n\t- [Q]uit\n\t\t*quits game\nGladiator Choice: '.format(
        name_of_gladiator)
    while True:
        decision = input(attack_choices)
        if decision in ['N', 'M', 'C', 'U', 'H', 'S']:
            return decision
        elif decision == 'Q':
            print('Gladiator {} has quit'.format(name_of_gladiator))
            exit()
        print('INVALID CHOICE')


def gladiator_fight(attacker, defender):
    battle_choice = attacker_decision(attacker.name)
    if battle_choice.lower() == 'N'.lower():
        message = attacker.normal_punch(defender)
        print(message)
    elif battle_choice.lower() == 'M'.lower():
        attacker.mega_kick(defender)
        print('\nMega kicked for a damage of 25')
    elif battle_choice.lower() == 'U'.lower():
        attacker.hard_uppercut(defender)
        print('\nHard Uppercut for damage of 35')
    elif battle_choice.lower() == 'C'.lower():
        attacker.cut()
    elif battle_choice.lower() == 'H'.lower():
        attacker.heal()
        print('\nHealth +5')
    elif battle_choice.lower() == 'S'.lower():
        attacker.skip()
        print('\nSkipped turn. +20 Rage')
    if defender.is_dead():
        print('\t\t\t!!!GAME!!!\n\t\t\t!!!OVER!!!')
        print('(W) New Presidential Gladiator: {}\n(L) Dead Canidate: {}'.
              format(attacker.name, defender.name))
        exit()


def main():
    print('\n\n\t\t\tWELCOME TO THE GLADIATOR BATTLE FOR PRESIDENCY GAME\n\n')
    low_damage_1, high_damage_1 = core.rand_damage(2, 15)
    gladiator_trump = core.Gladiator('Gladiator Trump', 100, 0, low_damage_1,
                                     high_damage_1)
    low_damage_2, high_damage_2 = core.rand_damage(5, 12)
    gladiator_clinton = core.Gladiator('Gladiator Clinton', 100, 0,
                                       low_damage_2, high_damage_2)
    print(repr(gladiator_trump), repr(gladiator_clinton), sep='\n')
    while True:
        gladiator_fight(gladiator_trump, gladiator_clinton)
        gladiator_fight(gladiator_clinton, gladiator_trump)
        print(gladiator_trump)
        print(gladiator_clinton)


if __name__ == '__main__':
    main()