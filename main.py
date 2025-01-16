def on_hit_wall(sprite, location):
    sprites.destroy(Tacos_Malvados)
    info.change_life_by(-1)
scene.on_hit_wall(SpriteKind.food, on_hit_wall)

def on_on_overlap(sprite2, otherSprite):
    sprites.destroy(otherSprite)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

Tacos_Malvados: Sprite = None
game.splash("Jogo dos tacos")
tiles.set_current_tilemap(tilemap("""
    level8
"""))
Miguel = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . b 5 5 b . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . b b b b b 5 5 5 5 5 5 5 b . . 
            . b d 5 b 5 5 5 5 5 5 5 5 b . . 
            . . b 5 5 b 5 d 1 f 5 d 4 f . . 
            . . b d 5 5 b 1 f f 5 4 4 c . . 
            b b d b 5 5 5 d f b 4 4 4 4 b . 
            b d d c d 5 5 b 5 4 4 4 4 4 4 b 
            c d d d c c b 5 5 5 5 5 5 5 b . 
            c b d d d d d 5 5 5 5 5 5 5 b . 
            . c d d d d d d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . .
    """),
    SpriteKind.player)
controller.move_sprite(Miguel, 150, 0)
Miguel.set_position(91, 97)
info.set_score(0)
info.set_life(5)

def on_update_interval():
    global Tacos_Malvados
    Tacos_Malvados = sprites.create(img("""
            . . . . . . . e e e e . . . . . 
                    . . . . . e e 4 5 5 5 e e . . . 
                    . . . . e 4 5 6 2 2 7 6 6 e . . 
                    . . . e 5 6 6 7 2 2 6 4 4 4 e . 
                    . . e 5 2 2 7 6 6 4 5 5 5 5 4 . 
                    . e 5 6 2 2 8 8 5 5 5 5 5 4 5 4 
                    . e 5 6 7 7 8 5 4 5 4 5 5 5 5 4 
                    e 4 5 8 6 6 5 5 5 5 5 5 4 5 5 4 
                    e 5 c e 8 5 5 5 4 5 5 5 5 5 5 4 
                    e 5 c c e 5 4 5 5 5 4 5 5 5 e . 
                    e 5 c c 5 5 5 5 5 5 5 5 4 e . . 
                    e 5 e c 5 4 5 4 5 5 5 e e . . . 
                    e 5 e e 5 5 5 5 5 4 e . . . . . 
                    4 5 4 e 5 5 5 5 e e . . . . . . 
                    . 4 5 4 5 5 4 e . . . . . . . . 
                    . . 4 4 e e e . . . . . . . . .
        """),
        SpriteKind.food)
    Tacos_Malvados.set_position(randint(10, 145), 5)
    Tacos_Malvados.set_velocity(0, 20)
game.on_update_interval(500, on_update_interval)
