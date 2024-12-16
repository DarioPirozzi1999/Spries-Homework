import pygame
import random
import time


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Hunt Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60


font = pygame.font.Font(None, 36)


player_size = 50
treasure_size = 30
trap_size = 30

player = pygame.Rect(WIDTH // 2, HEIGHT - player_size - 10, player_size, player_size)

player_color = (0, 128, 255)

def create_treasure():
    return pygame.Rect(random.randint(0, WIDTH - treasure_size), random.randint(0, HEIGHT - treasure_size), treasure_size, treasure_size)

def create_trap():
    return pygame.Rect(random.randint(0, WIDTH - trap_size), random.randint(0, HEIGHT - trap_size), trap_size, trap_size)


treasures = [create_treasure() for _ in range(5)]
traps = [create_trap() for _ in range(3)]
score = 0
lives = 3
start_time = time.time()
game_duration = 60  # 1 minute timer

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
         if player.y > 0:
            player.y -= 5
    elif keys[pygame.K_DOWN]:
         if player.y<700:
            player.y += 5
    elif keys[pygame.K_LEFT]:
         if player.x > 0:
            player.x -=5
    elif keys[pygame.K_RIGHT]:
         if player.x<900:
            player.x += 5
    pygame.draw.rect(screen, player_color, player)

    
    for treasure in treasures:
        pygame.draw.rect(screen, GOLD, treasure)
    for trap in traps:
        pygame.draw.rect(screen, RED, trap)

   
    for treasure in treasures[:]:
        if player.colliderect(treasure):
            treasures.remove(treasure)
            treasures.append(create_treasure())
            score += 10

    
    for trap in traps[:]:
        if player.colliderect(trap):
            traps.remove(trap)
            traps.append(create_trap())
            lives -= 1

    
    if lives <= 0:
        running = False

    
    elapsed_time = time.time() - start_time
    remaining_time = max(0, game_duration - int(elapsed_time))
    if remaining_time == 0:
        running = False


    score_text = font.render(f"Score: {score}", True, BLACK)
    lives_text = font.render(f"Lives: {lives}", True, BLACK)
    timer_text = font.render(f"Time: {remaining_time}s", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))
    screen.blit(timer_text, (10, 90))

  
    pygame.display.update()
    clock.tick(FPS)

screen.fill(WHITE)
end_text = font.render("Game Over!", True, BLACK)
final_score_text = font.render(f"Final Score: {score}", True, BLACK)
screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - 50))
screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 + 10))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
