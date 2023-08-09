import pygame
import random
import sys


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 400, 400

class Pet:
    def __init__(self, name,):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.health = 50

    def feed(self):
        self.hunger += 10
        self.happiness += 5
        self.health += 5

    def play(self):
        self.hunger -= 5
        self.happiness += 15
        self.health -= 5

    def heal(self):
        self.health += 20

    def update_status(self):
        self.hunger -= 5
        self.happiness -= 5
        self.health -= 5

        self.hunger = max(0, min(100, self.hunger))
        self.happiness = max(0, min(100, self.happiness))
        self.health = max(0, min(100, self.health))

def draw_text(screen, text, x, y, font_size=20):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pocket Companions")

    clock = pygame.time.Clock()

    name = input("Enter your pet's name: ")
    pet = Pet(name)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        draw_text(screen, f"{name}'s Status", WIDTH // 2, 50)
        draw_text(screen, f"Hunger: {pet.hunger}", WIDTH // 2, 100)
        draw_text(screen, f"Happiness: {pet.happiness}", WIDTH // 2, 130)
        draw_text(screen, f"Health: {pet.health}", WIDTH // 2, 160)

        draw_text(screen, "1. Feed", WIDTH // 2, 250)
        draw_text(screen, "2. Park Trip", WIDTH // 2, 280)
        draw_text(screen, "3. Vet Visit", WIDTH // 2, 310)
        draw_text(screen, "4. Exit", WIDTH // 2, 340)

        pygame.display.flip()

        choice = input("Choose an action: ")

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.heal()
        elif choice == '4':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Try again.")

        if random.randint(1, 10) == 1:
            print(f"Oh no! A random event occurred. {name} threw up a nasty hairball.")
            pet.health -= 10

            if random.randint(1, 10) == 2:
             print(f"Oh no! A random event occurred. {name} Pee'd in the house.")
            pet.happiness -= 10

            if random.randint(1, 10) == 3:
             print(f"Oh no! A random event occurred. {name} found a dead bird to play with.")
            pet.health -= 10
            pet.happiness +=10


        pet.update_status()

        if pet.happiness <= 0:
            print(f"{name} wasn't happy and ran away, to be with their own kind. GAME OVER...")
            break

        if pet.health <= 0:
            print(f"{name} has been taken from you, you were deemed a negligent owner. GAME OVER...")
            break

        if pet.hunger <= 0:
            print(f"{name} was so hungry they ate you. GAME OVER...")
            break

        clock.tick(5)

if __name__ == "__main__":   
 main()