from pygame.locals import *
import pygame
import sys

def id_input(player_number):
    pygame.init()   
    if pygame.joystick.get_count() == 1:
        joy_id1 = 0
        joystick1 = pygame.joystick.Joystick(joy_id1)
        joystick1.init()

    elif pygame.joystick.get_count() > 1:
        joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        for i, joystick in enumerate(joysticks):
            joystick.init()

        if len(joysticks) >= 2:
            joystick1, joystick2 = joysticks[:2]
                
    
    WIDTH = 560 
    HEIGHT = 720
    screen = pygame.display.set_mode((560, 720))    
    pygame.display.set_caption("Pygame sample app")  
    
    buttons = [
        pygame.Rect(80, 380, 80, 50),  
        pygame.Rect(184, 380, 80, 50),  
        pygame.Rect(288, 380, 80, 50),  
        pygame.Rect(392, 380, 80, 50),  
        pygame.Rect(80, 480, 80, 50),   
        pygame.Rect(184, 480, 80, 50),  
        pygame.Rect(288, 480, 80, 50),  
        pygame.Rect(392, 480, 80, 50),  
        pygame.Rect(80, 580, 80, 50),  
        pygame.Rect(184, 580, 80, 50), 
        pygame.Rect(288, 580, 80, 50),
        pygame.Rect(392, 580, 80, 50) 
        
    ]
    
    font = pygame.font.SysFont('msgothic', 20, bold=True)  
    font_big = pygame.font.SysFont('msgothic', 40, bold=True) 
   
    color =  (0,0,0)
    texts = [
        font.render("A", True, color),
        font.render("B", True, color),
        font.render("C", True, color),
        font.render("D", True, color),
        font.render("0", True, color),
        font.render("1", True, color),
        font.render("2", True, color),
        font.render("3", True, color),
        font.render("4", True, color),
        font.render("5", True, color),
        font.render("Delete", True, color),
        font.render("Enter", True, color)
    ]
    
    selected = [0, 0]  
    
    running = True

    txt_words = []
    txt_tmp = ''  

    while running:
        color_screen = (255,245,225)
        screen.fill(color_screen) 

        text = f"プレイヤー{player_number+1}のID\nを入力して下さい"
        lines = text.split("\n")  
        line_spacing = font_big.get_height() + 5  

        for i, line in enumerate(lines):
            rendered_text = font_big.render(line, True, (0, 0, 0))
            text_x = WIDTH/2 - rendered_text.get_width() / 2  
            text_y =100+ i * line_spacing  
            screen.blit(rendered_text, (text_x, text_y))


        colors = [
            (255, 0, 0), (0, 255, 0), (0, 0, 250), (255, 255, 0), (128, 0, 128),
            (255, 165, 0), (255, 192, 203), (0, 255, 255), (165, 42, 42), (128, 128, 128),
            (144, 238, 144), (255, 215, 0)  
        ]
        for i, button in enumerate(buttons):
            if i < 10:
                pygame.draw.rect(screen, colors[i], button, 0 if selected == [i // 4, i % 4] else 3)
                screen.blit(texts[i], (button.x + 35, button.y + 17.5))
            else:
                pygame.draw.rect(screen, colors[i], button, 0 if selected == [i // 4, i % 4] else 3)
                screen.blit(texts[i], (button.x + 15, button.y + 17.5))

        if len(txt_words) > 0: 
            txt = font_big.render(''.join(txt_words) + '|', True, color)  
        else:
            txt = font_big.render('|', True, color)
        screen.blit(txt, (
                    (WIDTH / 2) - (txt.get_width() / 2),
                    (HEIGHT / 2) - (txt.get_height() / 2) - 100
                ))

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected[1] = (selected[1] + 1) % 4 
                elif event.key == pygame.K_LEFT:
                    selected[1] = (selected[1] - 1) % 4  
                elif event.key == pygame.K_DOWN:
                    selected[0] = (selected[0] + 1) % 3 
                elif event.key == pygame.K_UP:
                    selected[0] = (selected[0] - 1) % 3  
                elif event.key == pygame.K_RETURN:
                    button_number = selected[0] * 4 + selected[1]  
                    if button_number < 4:  
                        txt_words.append(chr(65 + button_number))  
                    elif 4 <= button_number < 10:  # 0〜5 の場合
                        txt_words.append(str(button_number - 4))  
                    elif button_number == 10:  # 
                        if len(txt_words) > 0:
                            txt_words.pop()

                    elif button_number == 11: 
                        txt = ''.join(txt_words)
                        pygame.quit()
                        return txt
    
            if event.type == pygame.JOYBUTTONDOWN:
                button = event.button
                if event.joy == player_number:
                    if button == 11:  
                        selected[0] = (selected[0] - 1) % 3  
                    elif button == 12:  
                        selected[0] = (selected[0] + 1) % 3 
                    elif button == 13: 
                        selected[1] = (selected[1] - 1) % 4  
                    elif button == 14:  
                        selected[1] = (selected[1] + 1) % 4
                    elif button == 0: 
                        button_number = selected[0] * 4 + selected[1] 
                        if button_number < 4:  
                            txt_words.append(chr(65 + button_number)) 
                        elif 4 <= button_number < 10:  
                            txt_words.append(str(button_number - 4)) 
                        elif button_number == 10:  # Delete
                            if len(txt_words) > 0:
                                txt_words.pop()
                        elif button_number == 11:  # Enter
                            txt = ''.join(txt_words)
                            pygame.quit()
                            return txt
                