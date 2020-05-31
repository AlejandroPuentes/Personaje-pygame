

#Estado hacia izquierda
class LeftState:

    def __init__(self):
        self.image = 'imageLeftState'

    def getImage(self):
        return self.image


class WarriorLeftState(LeftState):

    def __init__(self):
        self.image = ['Static/izq.png', 'Static/izq1.png', 'Static/izq.png']

class WizardLeftState(LeftState):

    def __init__(self):
        self.image = ['Static/LeftWzFL.png', 'Static/LeftWzM.png', 'Static/LeftWzFL.png']

class MonsterLeftState(LeftState):

    def __init__(self):
        self.image =['Static/Wizquierda.png', 'Static/Wizquierda2.png', 'Static/Wizquierda.png']

#Estado hacia derecha
class RightState:

    def __init__(self):
        self.image = 'imageRightState'

    def getImage(self):
        return self.image


class WarriorRightState(RightState):

    def __init__(self):
        self.image =  ['Static/der.png', 'Static/der1.png', 'Static/der.png']

class WizardRightState(RightState):

    def __init__(self):
        self.image = ['Static/RightWzFL.png', 'Static/RightWzM.png', 'Static/RightWzFL.png']

class MonsterRightState(RightState):

    def __init__(self):
        self.image = ['Static/Mderecha.png', 'Static/Mderecha2.png', 'Static/Mderecha.png']

#Estado hacia arriba
class UpState:

    def __init__(self):
        self.image = 'imageUpState'

    def getImage(self):
        return self.image


class WarriorUpState(UpState):

    def __init__(self):
        self.image =  ['Static/arr.png', 'Static/arr1.png', 'Static/arr.png']

class WizardUpState(UpState):

    def __init__(self):
        self.image = ['Static/UpWzFL.png', 'Static/UpWzM.png', 'Static/UpWzFL.png']

class MonsterUpState(UpState):

    def __init__(self):
        self.image = ['Static/Warriba.png', 'Static/Warriba2.png', 'Static/Warriba.png']

#Estado hacia abajo
class DownState:

    def __init__(self):
        self.image = 'imageDowntState'

    def getImage(self):
        return self.image


class WarriorDownState(DownState):

    def __init__(self):
        self.image =  ['Static/abaj.png', 'Static/abaj1.png', 'Static/abaj.png']

class WizardDownState(DownState):

    def __init__(self):
        self.image = ['Static/DownWzFL.png', 'Static/DownWzM.png', 'Static/DownWzFL.png']

class MonsterDownState(DownState):

    def __init__(self):
        self.image = ['Static/Wabajo.png', 'Static/Wabajo2.png', 'Static/Wabajo.png']

#Estado salto
class JumpState:

    def __init__(self):
        self.image = 'imageJumpState'

    def getImage(self):
        return self.image


class WarriorJumpState(JumpState):

    def __init__(self):
        self.image =  ['Static/izq.png', 'Static/izq1.png', 'Static/izq.png']

class WizardJumpState(JumpState):

    def __init__(self):
        self.image = ['Static/RightWzFL.png', 'Static/JumpRWzM.png', 'Static/RightWzFL.png']

class MonsterJumpState(JumpState):

    def __init__(self):
        self.image = ['Static/Wizquierda.png', 'Static/Wizquierda2.png', 'Static/Wizquierda.png']