from Factory import WarriorFactory, WizardFactory, MonsterFactory
from Character import Character

class CharacterBuilder:


    def __init__(self):
        self.Character = None
        self.fabrica = None

    def buildLeft(self):
        pass

    def buildUp(self):
        pass

    def buildRight(self):
        pass

    def buildDown(self):
        pass

    def buildJump(self):
        pass

    def getCharacter(self):
        return self.Character


class WarriorBuilder(CharacterBuilder):

    def __init__(self):
        self.Character = Character()
        self.fabrica = WarriorFactory()

    def buildUp(self):
        self.Character.setUp(self.fabrica.createUpState())

    def buildRight(self):
        self.Character.setRight(self.fabrica.createRightState())

    def buildDown(self):
        self.Character.setDown(self.fabrica.createDownState())

    def buildLeft(self):
        self.Character.setLeft(self.fabrica.createLeftState())

    def buildJump(self):
        self.Character.setJump(self.fabrica.createJumpState())



class WizardBuilder(CharacterBuilder):

    def __init__(self):
        self.Character = Character()
        self.fabrica = WizardFactory()

    def buildUp(self):
        self.Character.setUp(self.fabrica.createUpState())

    def buildRight(self):
        self.Character.setRight(self.fabrica.createRightState())

    def buildDown(self):
        self.Character.setDown(self.fabrica.createDownState())

    def buildLeft(self):
        self.Character.setLeft(self.fabrica.createLeftState())

    def buildJump(self):
        self.Character.setJump(self.fabrica.createJumpState())



class MonsterBuilder(CharacterBuilder):

    def __init__(self):
        self.Character = Character()
        self.fabrica = MonsterFactory()

    def buildUp(self):
        self.Character.setUp(self.fabrica.createUpState())

    def buildRight(self):
        self.Character.setRight(self.fabrica.createRightState())

    def buildDown(self):
        self.Character.setDown(self.fabrica.createDownState())

    def buildLeft(self):
        self.Character.setLeft(self.fabrica.createLeftState())

    def buildJump(self):
        self.Character.setJump(self.fabrica.createJumpState())

    
class CharacterManager:

    def __init__(self):
        self.builder = None

    def setBuilder(self, builder):
        self.builder = builder

    def buildCharacter(self):
        self.builder.buildJump()
        self.builder.buildLeft()
        self.builder.buildRight()
        self.builder.buildUp()
        self.builder.buildDown()
        self.builder.getCharacter().loadImages()

    def getCharacter(self):
        return self.builder.getCharacter()