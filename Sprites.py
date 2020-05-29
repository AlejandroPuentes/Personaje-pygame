

#Estado hacia izquierda
class LeftState:

    def __init__(self):
        self.image = 'imageLeftState'

    def getImage(self):
        return self.image


class WarriorLeftState(LeftState):

    def __init__(self):
        self.image = 'imageWarriorLS'

class WizardLeftState(LeftState):

    def __init__(self):
        self.image = 'imageWizardLS'

class MonsterLeftState(LeftState):

    def __init__(self):
        self.image = 'imageMonsterLS'

#Estado hacia derecha
class RightState:

    def __init__(self):
        self.image = 'imageRightState'

    def getImage(self):
        return self.image


class WarriorRightState(RightState):

    def __init__(self):
        self.image = 'imageWarriorRS'

class WizardRightState(RightState):

    def __init__(self):
        self.image = 'imageWizardRS'

class MonsterRightState(RightState):

    def __init__(self):
        self.image = 'imageMonsterRS'

#Estado hacia arriba
class UpState:

    def __init__(self):
        self.image = 'imageUpState'

    def getImage(self):
        return self.image


class WarriorUpState(UpState):

    def __init__(self):
        self.image = 'imageWarriorUS'

class WizardUpState(UpState):

    def __init__(self):
        self.image = 'imageWizardUS'

class MonsterUpState(UpState):

    def __init__(self):
        self.image = 'imageMonsterUS'

#Estado hacia abajo
class DownState:

    def __init__(self):
        self.image = 'imageDowntState'

    def getImage(self):
        return self.image


class WarriorDownState(DownState):

    def __init__(self):
        self.image = 'imageWarriorDS'

class WizardDownState(DownState):

    def __init__(self):
        self.image = 'imageWizardDS'

class MonsterDownState(DownState):

    def __init__(self):
        self.image = 'imageMonsterDS'

#Estado salto
class JumpState:

    def __init__(self):
        self.image = 'imageJumpState'

    def getImage(self):
        return self.image


class WarriorJumpState(JumpState):

    def __init__(self):
        self.image = 'imageWarriorJS'

class WizardJumpState(JumpState):

    def __init__(self):
        self.image = 'imageWizardJS'

class MonsterJumpState(JumpState):

    def __init__(self):
        self.image = 'imageMonsterJS'