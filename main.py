import os
import random
import sys
from typing import Final

import pygame

from messages import defeat, victory

# Initialize the Pygame
pygame.init()
pygame.mouse.set_visible(False)

# Creating the Variables
SCREEN_WIDTH: Final[int] = 1280
SCREEN_HEIGHT: Final[int] = 600
FPS: Final[int] = 60

# COLORS
vivid_sky_blue = (58, 213, 248)

# Clock 
clock = pygame.time.Clock()

# Calling the Font
font1 = pygame.font.Font(None, 60)
font2 = pygame.font.SysFont("dejavuserif", 30)
print(type(font1))
# Ducks List
ducks_list = []
total_ducks = random.randint(35, 50)

class Font:
  def __init__(self, initial_text:str, font_type:pygame.font.Font,
               x:int, y:int, color:tuple[int, int, int]) -> None:
    self.text = initial_text
    self.font_type = font_type
    self.color = color
    self.x, self.y = x, y
  
  def display_text(self, win: pygame.Surface, text:str):
    self.text = text
    self.surface = self.font_type.render(self.text, True, self.color)
    self.rect = self.surface.get_rect(center=(self.x, self.y))
    win.blit(self.surface, self.rect)

class Cloud:
  def __init__(self, image_loc:str, posx, posy) -> None:
    self.image = pygame.image.load(image_loc)
    self.rect = self.image.get_rect()
    self.pos = posx, posy
    self.rect.center = self.pos
    self.vel = 1
    self.outstretch = random.randint(100, 200)

  def draw(self, win:pygame.Surface):
    win.blit(self.image, self.rect)

  def update(self):
    if self.rect.x <= self.pos[0] - self.outstretch:
      self.vel *= -1
    if self.rect.x >= self.pos[0] + self.outstretch:
      self.vel *= -1

    self.rect.x += self.vel


class Ducks:
  def __init__(self, image, posx, posy) -> None:
    self.image = pygame.image.load(os.path.join("Resource", image))
    self.rect = self.image.get_rect()
    self.rect.center = posx, posy
    self.vel = random.randint(0, 3)

  def draw(self, win):
    win.blit(self.image, self.rect)

  def update(self):
    self.rect.x += self.vel

    if self.rect.midleft[0] >= SCREEN_WIDTH + 100:
      self.rect.x = -100


class App:
  def __init__(self, width:int|float, height:int|float, FPS:int|float)->None:
    self.width =  width
    self.height = height
    self.FPS = FPS
    self.animation = True
    self.game_controller = True
    self.time_controller = True

    # Location Variables
    self.land_position_y = 450
    self.water_position_y = 500

    self.window = pygame.display.set_mode((self.width, self.height))
    print(self.window)
    pygame.display.set_caption(title="Duck Shooting")

    # Loading Assets
    # Relative Path
    self.wood_bg = pygame.image.load(os.path.join("Resource", "Wood_BG.png")).convert_alpha()

    # Land and Water Background
    self.land_bg = pygame.image.load(os.path.join("Resource", "Land_BG.png"))
    self.land_speed = 1
    
    self.water_bg = pygame.image.load(os.path.join("Resource", "Water_BG.png"))
    self.water_speed = 2

    # Crosshair 
    self.crosshair = pygame.image.load(os.path.join("Resource", "crosshair.png"))
    self.crosshair_rect = self.crosshair.get_rect()

    # Score
    self.score = 0
    self.score_font = Font(initial_text=f"SCORE: {self.score}", 
    font_type=font2, x=1000, y=100, color=(0, 8, 20))

    # Timer
    self.duration = 60000

    self.time_font = Font(initial_text=f"TIME LEFT: {self.duration//1000:.0f} Secs",
    font_type=font1, x=600, y=550, color=(255,255,255))

    # Victory/Defeat Score Text
    self.defeat_text1 = Font(initial_text="",
  font_type=font1, x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2, color=(38, 38, 38))
    self.defeat_text2 = Font(initial_text="",
  font_type=font1, x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2 + 50, color=(38, 38, 38))
    self.defeat_text3 = Font(initial_text="",
  font_type=font1, x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2 + 100, color=(38, 38, 38))
    
    self.victory_text1 = Font(initial_text="",
  font_type=font1, x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2, color=(38, 38, 38))
    self.victory_text2 = Font(initial_text="",
  font_type=font1, x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2 + 50, color=(38, 38, 38))
    self.victory_text3 = Font(initial_text="",
  font_type=font1, x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2 + 100, color=(38, 38, 38))
    self.victory_text4 = Font(initial_text="",
  font_type=font1, x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2 + 150, color=(38, 38, 38))
    

  def control(self):
    while self.animation:
      dt = clock.tick(FPS)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          self.animation = False
          sys.exit("Game Terminated!")
        if event.type == pygame.MOUSEMOTION:
          self.crosshair_rect.center = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
          for index, duck in enumerate(ducks_list):
            """if self.crosshair_rect.colliderect(duck.rect):
              ducks_list.pop(index)"""
            if duck.rect.collidepoint(event.pos):
              self.score += 1
              ducks_list.pop(index)
            
      if self.game_controller:
        self.window.fill(vivid_sky_blue)
        
        self.window.blit(self.wood_bg, (0, 0))
  
        cloud1.draw(self.window)
        cloud1.update()
        cloud2.draw(self.window)
        cloud3.draw(self.window)
        cloud3.update()
        cloud4.draw(self.window)
        cloud5.draw(self.window)
        cloud5.update()
        cloud6.draw(self.window)
  
        self.land_position_y -= self.land_speed
        self.water_position_y += self.water_speed
  
        if self.land_position_y <= 400 or self.land_position_y >= 500:
          self.land_speed *= -1
  
        if self.water_position_y <= 460 or self.water_position_y >= 540:
          self.water_speed *= -1
          
        self.window.blit(self.land_bg, (0, self.land_position_y))
        self.window.blit(self.water_bg, (0, self.water_position_y))
  
        for duck in ducks_list:
          duck.draw(win=self.window)
          duck.update()
  
  
        self.window.blit(self.crosshair, self.crosshair_rect)
        self.score_font.display_text(win=self.window, text=f"Score: {self.score}")


      # Time Remaining
      if self.time_controller:
        self.duration -= dt 
        print(self.duration)
        self.time_font.display_text(win=self.window, 
        text=f"TIME LEFT: {self.duration//1000:.0f} Secs")
        
      if self.duration <= 0:
        self.game_controller = False
        self.window.fill((255, 255, 255))
        lose = defeat(score=self.score, total_ducks=total_ducks)
        self.defeat_text1.display_text(win=self.window, text=lose[0])
        self.defeat_text2.display_text(win=self.window, text=lose[1])
        self.defeat_text3.display_text(win=self.window, text=lose[2])

      if len(ducks_list) <= 0:
        self.time_controller = False
        self.game_controller = False
        self.window.fill((255, 255, 255))
        win = victory(score=self.score, time_duration=f"{60 -self.duration//1000:.0f}")
        self.victory_text1.display_text(win=self.window, text=win[0])
        self.victory_text2.display_text(win=self.window, text=win[1])
        self.victory_text3.display_text(win=self.window, text=win[2])
        self.victory_text3.display_text(win=self.window, text=win[3])
        
      pygame.display.flip()


if __name__ == "__main__":
  # Drawing the Images
  cloud1 = Cloud(os.path.join("Resource", "Cloud1.png"), posx=100, posy=50)
  cloud2 = Cloud(os.path.join("Resource", "Cloud1.png"), posx=170, posy=80)

  cloud3 = Cloud(os.path.join("Resource", "Cloud2.png"), posx=604, posy=10)
  cloud4 = Cloud(os.path.join("Resource", "Cloud2.png"), posx=1105, posy=120)

  cloud5 = Cloud(os.path.join("Resource", "Cloud1.png"), posx=1000, posy=150)
  cloud6 = Cloud(os.path.join("Resource", "Cloud2.png"), posx=400, posy=25)

  # Drawing the Ducks
  ducks_list = [Ducks("duck.png", random.randint(0, SCREEN_WIDTH), 
  random.randint(0, 11 * SCREEN_HEIGHT//12)) for _ in range(0, total_ducks)]

  # Calling the Main Function
  app = App(SCREEN_WIDTH, SCREEN_HEIGHT, FPS)
  app.control()
  