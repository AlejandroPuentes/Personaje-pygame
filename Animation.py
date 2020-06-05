from Builder import CharacterManager, WarriorBuilder, WizardBuilder, MonsterBuilder
import sys, pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) 
BLACK = 0,0,0
DELAY = 100

manager = CharacterManager()
manager.setBuilder(WizardBuilder())
manager.buildCharacter()
character = manager.getCharacter()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
playing = True
character.place(CENTER)


while playing:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                sys.exit()
    
    screen.fill(BLACK)
    character.update()
    print(character.getPos())
    character.draw(screen)
    pygame.time.delay(DELAY)
    pygame.display.flip()