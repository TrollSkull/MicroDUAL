def on_received_number(receivedNumber):
    global enemy_bullet
    enemy_bullet = game.create_sprite(receivedNumber, 0)
    enemy_bullet.set(LedSpriteProperty.BRIGHTNESS, 300)
    while True:
        if enemy_bullet.is_touching(hitbox_lower):
            enemy_bullet.delete()
            break
        enemy_bullet.change(LedSpriteProperty.Y, 1)
        basic.pause(200)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global friendly_bullet
    music.play(music.create_sound_expression(WaveShape.SQUARE,
            3328,
            1,
            255,
            0,
            300,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.UNTIL_DONE)
    friendly_bullet = game.create_sprite(ship.get(LedSpriteProperty.X), ship.get(LedSpriteProperty.Y))
    friendly_bullet.set(LedSpriteProperty.BRIGHTNESS, 300)
    while True:
        if friendly_bullet.is_touching(hitbox_top):
            radio.send_number(friendly_bullet.get(LedSpriteProperty.X))
            friendly_bullet.delete()
            break
        friendly_bullet.change(LedSpriteProperty.Y, -1)
        basic.pause(200)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    while input.is_gesture(Gesture.LOGO_UP):
        ship.change(LedSpriteProperty.Y, 1)
        basic.pause(500)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_left():
    while input.is_gesture(Gesture.TILT_LEFT):
        ship.change(LedSpriteProperty.X, -1)
        basic.pause(500)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_ab():
    ship.set(LedSpriteProperty.BLINK, 300)
    basic.pause(3000)
    if input.button_is_pressed(Button.AB):
        music.play(music.create_sound_expression(WaveShape.SQUARE,
                1088,
                1,
                255,
                0,
                300,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            music.PlaybackMode.UNTIL_DONE)
    ship.set(LedSpriteProperty.BLINK, 0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_tilt_right():
    while input.is_gesture(Gesture.TILT_RIGHT):
        ship.change(LedSpriteProperty.X, 1)
        basic.pause(500)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    while input.is_gesture(Gesture.LOGO_DOWN):
        ship.change(LedSpriteProperty.Y, -1)
        basic.pause(500)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

friendly_bullet: game.LedSprite = None
enemy_bullet: game.LedSprite = None
hitbox_top: game.LedSprite = None
hitbox_lower: game.LedSprite = None
ship: game.LedSprite = None
game.add_life(5)
music.set_built_in_speaker_enabled(True)
ship = game.create_sprite(2, 5)
ship.set(LedSpriteProperty.BRIGHTNESS, 1000)
hitbox_lower = game.create_sprite(2, 5)
hitbox_lower.set(LedSpriteProperty.BRIGHTNESS, 10)
hitbox_top = game.create_sprite(2, -5)
hitbox_top.set(LedSpriteProperty.BRIGHTNESS, 10)
