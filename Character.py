from Factory import WarriorFactory, WizardFactory, MonsterFactory

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

class Character:

    def __init__(self):
        self.left = None
        self.right = None
        self.down = None
        self.up = None
        self.jump = None

    def setLeft(self, left):
        self.left = left

    def setUp(self, up):
        self.up = up.getImage()

    def setRight(self, right):
        self.right = right

    def setDown(self, down):
        self.down = down

    def setJump(self, jump):
        self.jump = jump

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getDown(self):
        return self.down

    def getJump(self):
        return self.jump




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

    def getCharacter(self):
        return self.builder.getCharacter()