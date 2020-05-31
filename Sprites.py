

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
        self.image = ['Static/LeftWzFL.png', 'Static/LeftWzM.png', 'Static/LeftWzFL.png']

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
        self.image = ['Static/RightWzFL.png', 'Static/RightWzM.png', 'Static/RightWzFL.png']

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
        self.image = ['Static/UpWzFL.png', 'Static/UpWzM.png', 'Static/UpWzFL.png']

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
        self.image = ['Static/LeftWzFL.png', 'Static/LeftWzM.png', 'Static/LeftWzFL.png']

class WizardDownState(DownState):

    def __init__(self):
        self.image = ['Static/DownWzFL.png', 'Static/DownWzM.png', 'Static/DownWzFL.png']

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
        self.image = ['Static/RightWzFL.png', 'Static/JumpRWzM.png', 'Static/RightWzFL.png']

class MonsterJumpState(JumpState):

    def __init__(self):
        self.image = 'imageMonsterJS'