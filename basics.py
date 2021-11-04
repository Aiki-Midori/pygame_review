import pygame as pg, sys

pg.init() 
pg.display.set_caption("Back with Pygame!")
screen = pg.display.set_mode((800, 400))
clock = pg.time.Clock()
FPS = 60

# --------- PLAIN SURFACE --------- #
# test_surface = pg.Surface((100, 100))
# test_surface.fill('Green')

# --------- IMAGE SURFACE --------- #
sky_surface = pg.image.load('graphics/Sky.png').convert()
ground_surface = pg.image.load('graphics/Ground.png').convert()
snail_surface = pg.image.load('graphics/snail/Snail1.png').convert_alpha()
player_surface = pg.image.load('graphics/player/Player_Walk_1.png').convert_alpha()

# --------- RECTANGLES --------- #
player_rect = player_surface.get_rect(midbottom=(50, 300))

# --------- TEXT SURFACE --------- #
# create a font then attach that into a surface
test_font = pg.font.Font("font/Pixeltype.ttf", 70)
text_surface = test_font.render("PyGame Review", True, (100, 150, 200))

# --------- GAME VARS --------- #
snail_x, snail_y = 700, 265


# ---------  MAIN LOOP --------- #
while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit() # allows u to exit any code u typed entirely

  # screen.blit(test_surface, (200, 100))
  screen.blit(sky_surface, (0,0))
  screen.blit(ground_surface, (0,300))
  screen.blit(text_surface, (100, 100))
  screen.blit(snail_surface, (snail_x, snail_y))
  screen.blit(player_surface, player_rect) 

  # ---------  ANIMATION --------- #
  snail_x -= 5
  if snail_x < 0: snail_x = 700
  
  player_rect.left += 1

  
  pg.display.update()
  clock.tick(FPS)



# "surface" for image information, "rectangles" are for placement, & "sprites" combines those two into one

# placing the surface into the pos of the rect