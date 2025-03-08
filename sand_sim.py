import pygame


class SandSim:
    def __init__(self, colors: list, row_size: int, col_size: int, cell_size: int) -> None:
        self.colors = colors
        self.color_index = 0
        self.row_size = row_size
        self.col_size = col_size
        self.cell_size = cell_size
        self.matrix = [[0] * self.col_size for _ in range(self.row_size)]
        self.alive_cell = []
        self.fall_directions = [(1, 0), (1, -1), (1, 1)]
    
    def handle_event(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.color_index -= 1 
                self.color_index %= len(self.colors)
            elif event.key == pygame.K_RIGHT:
                self.color_index += 1 
                self.color_index %= len(self.colors)
            if event.key == pygame.K_c:
                self.clear()
    
    def add_sand(self, row_index, col_index) -> None:
        if not is_index_out_of_range(row_index, col_index, self.row_size, self.col_size):
            cell = (row_index, col_index)
            if cell not in self.alive_cell:
                self.matrix[row_index][col_index] = self.colors[self.color_index]
                self.alive_cell.append(cell)
    
    def remove_sand(self, row_index, col_index) -> None:
        if not is_index_out_of_range(row_index, col_index, self.row_size, self.col_size):
            cell = (row_index, col_index)
            if cell in self.alive_cell:
                self.matrix[row_index][col_index] = 0
                self.alive_cell.remove(cell)
    
    def clear(self) -> None:
        self.matrix = [[0] * self.col_size for _ in range(self.row_size)]
        self.alive_cell = []
    
    def handle_sand_input(self) -> None:
        mouse_input = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        row_index = int(mouse_pos[1] / self.cell_size)
        col_index = int(mouse_pos[0] / self.cell_size)
    
        if mouse_input[0]:
            self.add_sand(row_index, col_index)

        if mouse_input[2]:
            self.remove_sand(row_index, col_index)
    
    def update(self) -> None:
        new_alive_cell = [row[:] for row in self.alive_cell]  # Create a copy to store updates

        for cell in self.alive_cell:
            
            for direction in self.fall_directions:
                next_cell = (cell[0] + direction[0], cell[1] + direction[1])

                if not is_index_out_of_range(next_cell[0], next_cell[1], self.row_size, self.col_size):
                    if self.matrix[next_cell[0]][next_cell[1]] == 0:

                        # Move the cell
                        self.matrix[next_cell[0]][next_cell[1]] = self.matrix[cell[0]][cell[1]]
                        self.matrix[cell[0]][cell[1]] = 0
                        
                        new_alive_cell.remove(cell)
                        new_alive_cell.append(next_cell)
                        break
        
        self.alive_cell = new_alive_cell
    
    def draw(self, surface: pygame.Surface) -> None:
        for cell in self.alive_cell:
            pos_y = cell[0] * self.cell_size
            pos_x = cell[1] * self.cell_size
            rect = pygame.FRect(pos_x, pos_y, self.cell_size, self.cell_size)
            value = self.matrix[cell[0]][cell[1]]
            pygame.draw.rect(surface, value, rect)


def is_index_out_of_range(row_index, col_index, row_size, col_size) -> bool:
    return not (0 <= row_index < row_size and 0 <= col_index < col_size)