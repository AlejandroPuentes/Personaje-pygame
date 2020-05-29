from Character import CharacterManager, WarriorBuilder, WizardBuilder, MonsterBuilder


manager = CharacterManager()
manager.setBuilder(WarriorBuilder())
manager.buildCharacter()
character = manager.getCharacter()

print(character.getDown().getImage())