from Factory import WarriorFactory, WizardFactory, MonsterFactory
from Character import Character

class CharacterBuilder:


    def __init__(self):
        self.Character = None
        self.factory = None

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

    def setImages(self):
        self.Character.setImages()


class WarriorBuilder(CharacterBuilder):

    def __init__(self):
        self.Character = Character()
        self.factory = WarriorFactory()

    def buildUp(self):
        self.Character.setUp(self.factory.createUpState())

    def buildRight(self):
        self.Character.setRight(self.factory.createRightState())

    def buildDown(self):
        self.Character.setDown(self.factory.createDownState())

    def buildLeft(self):
        self.Character.setLeft(self.factory.createLeftState())

    def buildJump(self):
        self.Character.setJump(self.factory.createJumpState())



class WizardBuilder(CharacterBuilder):

    def __init__(self):
        self.Character = Character()
        self.factory = WizardFactory()

    def buildUp(self):
        self.Character.setUp(self.factory.createUpState())

    def buildRight(self):
        self.Character.setRight(self.factory.createRightState())

    def buildDown(self):
        self.Character.setDown(self.factory.createDownState())

    def buildLeft(self):
        self.Character.setLeft(self.factory.createLeftState())

    def buildJump(self):
        self.Character.setJump(self.factory.createJumpState())



class MonsterBuilder(CharacterBuilder):

    def __init__(self):
        self.Character = Character()
        self.factory = MonsterFactory()

    def buildUp(self):
        self.Character.setUp(self.factory.createUpState())

    def buildRight(self):
        self.Character.setRight(self.factory.createRightState())

    def buildDown(self):
        self.Character.setDown(self.factory.createDownState())

    def buildLeft(self):
        self.Character.setLeft(self.factory.createLeftState())

    def buildJump(self):
        self.Character.setJump(self.factory.createJumpState())

    
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
        self.builder.setImages()

    def getCharacter(self):
        return self.builder.getCharacter()