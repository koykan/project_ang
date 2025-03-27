import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Главное меню")

background = pygame.image.load("firstscreen.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

WHITE = (255, 255, 255)
GRAY = (170, 170, 170)
DARK_GRAY = (100, 100, 100)

font = pygame.font.Font(None, 40)

buttons = [
    ("Начать игру", (WIDTH // 2 - 100, 200, 200, 50)),
    ("Сохранения", (WIDTH // 2 - 100, 270, 200, 50)),
    ("Настройки", (WIDTH // 2 - 100, 340, 200, 50)),
    ("Об игре", (WIDTH // 2 - 100, 410, 200, 50))
]


def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect, border_radius=10)
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    screen.blit(text_surf, text_rect)


running = True
while running:
    screen.blit(background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    for text, rect in buttons:
        color = GRAY if pygame.Rect(rect).collidepoint(mouse_pos) else DARK_GRAY
        draw_button(text, rect, color)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for text, rect in buttons:
                if pygame.Rect(rect).collidepoint(event.pos):
                    print(f"Нажата кнопка: {text}")

pygame.quit()
