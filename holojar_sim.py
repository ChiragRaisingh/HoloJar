import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

matrix_width = 8
matrix_height = 32
cell_size = 20
matrix_pos = pygame.Vector2(screen.get_width()/2 - 80, 40)
# Initialize the LED matrix with zeros  

led_matrix = [[0 for _ in range(matrix_height)] for _ in range(matrix_width)]




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running = False


    screen.fill((0, 0, 0))  # Clear the screen with black
    
    # Draw the matrix as a grid of rectangles


    for row_index, row in enumerate(led_matrix):
        for col_index, cell in enumerate(row):
            rect = pygame.Rect(
                matrix_pos.x + row_index * 20, 
                matrix_pos.y + col_index * 20, 
                cell_size - 1, 
                cell_size - 1
            )

            color = (255, 0, 0) if cell else (0, 0, 255)  # Red for active cells, black for inactive
            pygame.draw.rect(screen, color, rect, 1)  # Draw grid lines

    dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
    pygame.display.flip()  # Update the display

pygame.quit()






# player_pos = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)  # Center of the screen

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((0, 0, 0))  # Clear the screen with black
#     pygame.draw.circle(screen, (255, 255, 255), player_pos, 50)  # Draw player

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_a]:
#         player_pos.x -= 30 * dt      
#     if keys[pygame.K_d]:
#         player_pos.x += 30 * dt
#     if keys[pygame.K_w]:
#         player_pos.y -= 30 * dt
#     if keys[pygame.K_s]:
#         player_pos.y += 30 * dt


#     dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

#     # Update and draw game objects here
#     # Example: pygame.draw.circle(screen, (255, 0, 0), (640, 360), 50)
#     pygame.display.flip()  # Update the display

# pygame.quit()