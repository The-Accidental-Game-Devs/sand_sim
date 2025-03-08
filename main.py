import sys
import pygame
import settings
from sand_sim import SandSim

class Main:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        self.sand_sim = SandSim(settings.SAND_COLORS, settings.ROW_SIZE, settings.COL_SIZE, settings.CELL_SIZE)
    
    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            self.sand_sim.handle_event(event)

    def update(self) -> None:
        self.sand_sim.handle_sand_input()
        self.sand_sim.update()
    
    def draw(self) -> None:
        self.display_surface.fill("black")
        self.sand_sim.draw(self.display_surface)
        pygame.display.update()

    def run(self) -> None:
        while True:
            self.handle_event()
            self.update()
            self.draw()

if __name__ == "__main__":
    main = Main()
    main.run()
