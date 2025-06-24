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

ship: game.LedSprite = None
ship = game.create_sprite(2, 5)

# Hits a cada 200 de brightness.
ship.set(LedSpriteProperty.BRIGHTNESS, 1000)
