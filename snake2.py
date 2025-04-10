import pygame, random, sys

pygame.init()

# Cấu hình màn hình
WIDTH, HEIGHT, SIZE = 720, 480, 20
gameSurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Màu sắc
WHITE, RED, GRAY, BLACK = (255,255,255), (255,0,0), (128,128,128), (0,0,0)

# Khởi tạo rắn và thức ăn ban đầu
snake = [[100, 60], [80, 60], [60, 60]]   # rắn có 3 phần, 2 thân 1 đầuđầu
food = [random.randrange(1, WIDTH//SIZE) * SIZE, random.randrange(1, HEIGHT//SIZE) * SIZE] #random thức ăn trong phạm vi màng hình và nhân với kích thứcthức
direction = 'RIGHT'
score = 0

# Hàm hiển thị điểm số
def show_score():
    font = pygame.font.SysFont('consolas', 20)
    score_text = font.render(f'Score: {score}', True, BLACK)
    gameSurface.blit(score_text, (10, 10))

# Hàm hiển thị Game Over
def game_over():
    font = pygame.font.SysFont('consolas', 40)
    over_text = font.render(f'Game Over! Score: {score}', True, RED)
    rect = over_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    gameSurface.blit(over_text, rect)
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

clock = pygame.time.Clock()

# Vòng lặp game
while True:
    gameSurface.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
    
    # Di chuyển rắn
    head = snake[0][:]
    if direction == 'RIGHT': head[0] += SIZE
    elif direction == 'LEFT': head[0] -= SIZE
    elif direction == 'UP': head[1] -= SIZE
    elif direction == 'DOWN': head[1] += SIZE
    snake.insert(0, head)
    
    # Xử lý ăn thức ăn
    if head == food:
        score += 1
        food = [random.randrange(1, WIDTH//SIZE) * SIZE, random.randrange(1, HEIGHT//SIZE) * SIZE]
    else:
        snake.pop()
    
    # Kiểm tra va chạm
    if head in snake[1:] or head[0] < 0 or head[1] < 0 or head[0] >= WIDTH or head[1] >= HEIGHT:
        game_over()
    
    # Vẽ rắn và thức ăn
    for segment in snake:
        pygame.draw.rect(gameSurface, GRAY, (*segment, SIZE, SIZE))
    pygame.draw.rect(gameSurface, RED, (*food, SIZE, SIZE))
    pygame.draw.rect(gameSurface, GRAY, (0, 0, WIDTH, HEIGHT), 2)
    show_score()
    pygame.display.flip()
    clock.tick(10)
