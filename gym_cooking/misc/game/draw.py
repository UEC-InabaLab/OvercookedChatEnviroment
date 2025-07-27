import pygame
import sys

def draw_start_screen(self):
    # 背景色
    self.screen.fill(self.BLACK)
        
    # タイトルテキスト
    title_text = self.title_font.render("My Awesome Game", True, self.WHITE)
    title_rect = title_text.get_rect(center=(self.width // 2, self.height // 4))
    self.screen.blit(title_text, title_rect)
        
    # スタートボタン
    pygame.draw.rect(self.screen, self.GREEN, self.start_button_rect)
    start_text = self.button_font.render("Start Game", True, self.BLACK)
    start_text_rect = start_text.get_rect(center=self.start_button_rect.center)
    self.screen.blit(start_text, start_text_rect)

def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button_rect.collidepoint(event.pos):
                    self.game_started = True
                    self.running = False

def run(self):
        while self.running:
            self.handle_events()
            self.draw_start_screen()
            
            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()