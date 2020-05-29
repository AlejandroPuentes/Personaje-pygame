
from Sprites import *

class CharacterFactory:
    
    def createLeftState(self):
        pass

    def createUpState(self):
        pass

    def createRightState(self):
        pass

    def createDownState(self):
        pass

    def createJumpState(self):
        pass


class WarriorFactory(CharacterFactory):

    def createLeftState(self):
        return WarriorLeftState()
    
    def createUpState(self):
        return WarriorUpState()

    def createRightState(self):
        return WarriorRightState

    def createDownState(self):
        return WarriorDownState()

    def createJumpState(self):
        return WarriorJumpState()

class WizardFactory(CharacterFactory):

    def createLeftState(self):
        return WizardLeftState()
    
    def createUpState(self):
        return WizardUpState()

    def createRightState(self):
        return WizardRightState

    def createDownState(self):
        return WizardDownState()

    def createJumpState(self):
        return WizardJumpState()


class MonsterFactory(CharacterFactory):

    def createLeftState(self):
        return MonsterLeftState()
    
    def createUpState(self):
        return MonsterUpState()

    def createRightState(self):
        return MonsterRightState

    def createDownState(self):
        return MonsterDownState()

    def createJumpState(self):
        return MonsterJumpState()

