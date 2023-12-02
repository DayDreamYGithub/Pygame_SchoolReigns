import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("SchoolReigns")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 54)
max_font = pygame.font.Font(None, 200)

academic_performance = 4
physical_health = 4
mental_wellbeing = 4

game_active=True


pygame.mixer.init()
pygame.mixer.music.load("bgm/tense-sad-piano-111679.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

day = 1

random_integer = random.randint(0, 2)

event_list = ["Studying makes the body very tired, and I get a chance to rest. Do you want to rest?","I really want to spend a night at an off-campus Internet cafe...","If I study for half an hour more in the evening, I can study more..."]

academic_performance_surface = font.render(f"Academic Performance: {academic_performance}/8", False, (255, 255, 255))
physical_health_surface = font.render(f"Physical Health: {physical_health}/8", False, (255, 255, 255))
mental_wellbeing_surface = font.render(f"Mental Well-being: {mental_wellbeing}/8", False, (255, 255, 255))
day_surface = font.render(f"Day: {day}", False, (255, 255, 255))

event_surface = big_font.render(f"{event_list[random_integer]}", False, (255, 255, 255))

yes_surface = max_font.render(f"YES", False, (255, 255, 255))
no_surface = max_font.render(f"NO", False, (255, 255, 255))

school_surface = pygame.image.load("img/school.png").convert()


def draw_text_with_wrapping(text, font, color, rect, screen):
    words = text.split(' ')
    space_width, _ = font.size(' ')
    x, y = rect.left + 10, rect.top + 10
    line = ''

    for word in words:
        if font.size(line + word)[0] <= rect.width - 20:
            line += word + ' '
        else:
            text_surface = font.render(line, False, color)
            screen.blit(text_surface, (x, y))
            y += font.size(line)[1] + 5
            line = word + ' '

    text_surface = font.render(line, False, color)
    screen.blit(text_surface, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            pygame.mixer.music.stop()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if random_integer==0:
                if 20 <= mouse_x <= 220 and 360 <= mouse_y <= 560:
                    physical_health += 1
                    academic_performance -=1

                elif 1050 <= mouse_x <= 1250 and 360 <= mouse_y <= 560:
                    physical_health -= 1
                    academic_performance +=1

            if random_integer==1:
                if 20 <= mouse_x <= 220 and 360 <= mouse_y <= 560:
                    mental_wellbeing += 1
                    physical_health +=1
                    academic_performance -=2

                elif 1050 <= mouse_x <= 1250 and 360 <= mouse_y <= 560:
                    mental_wellbeing -= 1
                    physical_health -=1
                    academic_performance += 2

            if random_integer == 2:
                if 20 <= mouse_x <= 220 and 360 <= mouse_y <= 560:
                    physical_health -=1
                    academic_performance +=1
                elif 1050 <= mouse_x <= 1250 and 360 <= mouse_y <= 560:
                    physical_health +=1
                    academic_performance -=1
            day+=1
            random_integer = random.randint(0,2)
            event_surface = big_font.render(f"{event_list[random_integer]}", False, (255, 255, 255))
            pygame.display.flip()

    if academic_performance < 0 or physical_health<0 or mental_wellbeing<0 or academic_performance>8 or physical_health>8 or mental_wellbeing>8:
        game_active = False
    if game_active == False:
        screen.fill((0, 0, 0))
        gameover_surface = max_font.render(f"GAME OVER!", False, (255, 255, 255))
        screen.blit(gameover_surface, (250,300))

    if game_active==True:
        academic_performance_surface = font.render(f"Academic Performance: {academic_performance}/8", False,(255, 255, 255))
        physical_health_surface = font.render(f"Physical Health: {physical_health}/8", False, (255, 255, 255))
        mental_wellbeing_surface = font.render(f"Mental Well-being: {mental_wellbeing}/8", False, (255, 255, 255))
        day_surface = font.render(f"Day: {day}", False, (255, 255, 255))

        screen.fill((0, 0, 0))

        screen.blit(school_surface,(0,0))


        center_x, center_y = screen.get_width() // 2, screen.get_height() // 2


        rectangle = pygame.Rect(center_x - 200, center_y - 300, 400, 600)
        rectangle2 = pygame.Rect(center_x - 200, center_y - 300, 400, 600)
        rectangle2 = pygame.Rect(0, 0, 400, 100)


        pygame.draw.rect(screen, (0,0,0), rectangle)
        pygame.draw.rect(screen, (0,0,0), rectangle2)

        screen.blit(academic_performance_surface, (0, 0))
        screen.blit(physical_health_surface, (0, 30))
        screen.blit(mental_wellbeing_surface, (0, 60))
        screen.blit(day_surface, (1180, 0))

        event_x = rectangle.left + 10
        event_y = rectangle.top + 10

        screen.blit(yes_surface, (20, 360))
        screen.blit(no_surface, (1050, 360))

        draw_text_with_wrapping(event_list[random_integer], big_font, (255, 255, 255), rectangle, screen)

    pygame.display.update()

    clock.tick(60)

pygame.mixer.quit()
