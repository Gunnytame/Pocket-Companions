import pygame
import sys
from faker import Faker
from pet_game import Pet


class Owner:
    def __init__(self):
        fake = Faker()
        self.city = fake.city()
        self.environment = fake.random_element(['Urban', 'Suburban', 'Rural'])
        self.lifestyle = fake.random_element(['Active', 'Sedentary', 'Mixed'])


def main(name):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pocket Companions")


    clock = pygame.time.Clock()

    fake = Faker()
    owner = Owner()
    pet = Pet(name)

    while True:


        screen.fill(BLACK)


   
        draw_text(screen, f"City: {owner.city}", WIDTH // 2, 70, font_size=16)
        draw_text(screen, f"Environment: {owner.environment}", WIDTH // 2, 90, font_size=16)
        draw_text(screen, f"Lifestyle: {owner.lifestyle}", WIDTH // 2, 110, font_size=16)



        pygame.display.flip()

       

        clock.tick(5)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide a pet name.")
