from ursina import Ursina, Entity, Text, Button, Vec3, DirectionalLight, camera, window, duplicate, lerp, rgb, print_on_screen
from ursina.shaders import lit_with_shadows_shader
import math


def main_menu():
    global darts_list
    # Ist der erste Dart ausgewählt, wird der Button nach links deaktiviert
    if i_selected_dart == 0:
        switch_l_button.collision = False
    else:
        switch_l_button.collision = True
    for y in main_menu_entities:
        y.enabled = True

    # Beim Start wird standartmässig der erste Dart angezeigt
    darts_list[0]


def settings():
    # Alle Menu Entities werden deaktiviert
    for y in main_menu_entities:
        y.enabled = False
    # Alle Settings Entities werden aktiviert
    for y in settings_entities:
        y.enabled = True


def switch_r():
    global selected_dart
    global i_selected_dart
    i_selected_dart += 1
    selected_dart.position = -10, 0.2, 0
    selected_dart = darts_list[i_selected_dart]
    selected_dart.position = 0, 0.2, 0
    switch_l_button.collision = True
    if i_selected_dart == 1:
        switch_r_button.collision = False


def switch_l():
    global selected_dart
    global i_selected_dart
    i_selected_dart -= 1
    selected_dart.position = 7, 0.2, 0
    selected_dart = darts_list[i_selected_dart]
    selected_dart.position = 0, 0.2, 0
    switch_r_button.collision = True
    if i_selected_dart == 0:
        switch_l_button.collision = False


def camera_position_r():
    global i_camera_position
    i_camera_position += 1
    if i_camera_position > 1:
        i_camera_position = 0
    camera_position_text.text = camera_positions_list[i_camera_position]


def camera_position_l():
    global i_camera_position
    i_camera_position -= 1
    if i_camera_position < 0:
        i_camera_position = 1
    camera_position_text.text = camera_positions_list[i_camera_position]


def speed_r():
    global i_speed
    global speed
    i_speed += 1
    if i_speed > 4:
        i_speed = 0
    speed_text.text = speed_list[i_speed]
    speed = speed_list[i_speed]


def speed_l():
    global i_speed
    global speed
    i_speed -= 1
    if i_speed < 0:
        i_speed = 4
    speed_text.text = speed_list[i_speed]
    speed = speed_list[i_speed]


def angle_r():
    global i_angle
    i_angle += 1
    if i_angle > 2:
        i_angle = 0
    angle_text.text = angle_list[i_angle]


def angle_l():
    global i_angle
    i_angle -= 1
    if i_angle < 0:
        i_angle = 2
    angle_text.text = angle_list[i_angle]


def back_to_menu():
    # Alles wird zurückgesetzt, damit es wieder wie im Hauptmenü aussieht. Der ausgewählte Dart bleibt aber ausgewählt
    back_to_menu_button.enabled = False
    selected_dart.update = False
    for y in settings_entities:
        y.enabled = False
    board.enabled = False
    selected_dart.scale = 100
    selected_dart.position = (0, 0.2, 0)
    selected_dart.rotation = (-10, 25, 20)
    selected_dart.enabled = False
    # Kamera wird zurückgesetzt
    camera.position = (0, 0, -19.4)
    camera.rotation = (0, 0, 0)
    main_menu()


def curve_function(b):
    pos = lerp(start_pos, target_pos, b)
    pos.y += 0.1 * math.sin(b * math.pi)
    return pos

# Steckwinkel: Flach: 5; Mittel; 14; 23;

# Die verschiedenen Funktionen für die Rotation das Darts auf der x-Achse (nach hinten/vorne Kippen des Darts)


def rotation_function_flat(b):
    return -85.417 * b**3 + 69.167 * b**2 + 9.25 * b + 2


def rotation_function_medium(b):
    return -141.667 * b**3 + 136.667 * b**2 - 11 * b + 2


def rotation_function_steep(b):
    return -197.917 * b**3 + 204.167 * b**2 - 31.25 * b + 2


def update_throw_flat():
    global b
    if b <= 1:
        selected_dart.position = curve_function(b)
        selected_dart.rotation_x = rotation_function_flat(b)
        selected_dart.rotation_z -= speed * 50
        b += speed / 20

    else:
        selected_dart.position = curve_function(b=1)
        selected_dart.rotation_x = rotation_function_flat(b=1)
        selected_dart.update = False


def update_throw_medium():
    global b
    if b <= 1:
        selected_dart.position = curve_function(b)
        selected_dart.rotation_x = rotation_function_medium(b)
        selected_dart.rotation_z -= speed * 50
        b += speed / 20

    else:
        selected_dart.position = curve_function(b=1)
        selected_dart.rotation_x = rotation_function_medium(b=1)
        selected_dart.update = False


def update_throw_steep():
    global b
    if b <= 1:
        selected_dart.position = curve_function(b)
        selected_dart.rotation_x = rotation_function_steep(b)
        selected_dart.rotation_z -= speed * 50
        b += speed / 20

    else:
        selected_dart.position = curve_function(b=1)
        selected_dart.rotation_x = rotation_function_steep(b=1)
        selected_dart.update = False


def start():
    # Alle Menu Entities werden deaktiviert
    for y in main_menu_entities:
        y.enabled = False

    # Wenn die Kameraperspektive verändert wurde, wird sie hier positioniert
    if i_camera_position == 1:
        camera.position = (-4, 0, -17.8)
        camera.rotation = (0, 90, 0)

    # Der ausgewählte Dart wird in Startposition gebracht
    selected_dart.scale = 1
    selected_dart.position = (0, 0.112, -18.717)
    selected_dart.rotation = (2, 176.9, 0)
    selected_dart.enabled = True

    board.enabled = True
    back_to_menu_button.enabled = True

    # Definition für Flugkurve
    global b
    global target_pos
    b = 0
    target_pos = Vec3(0.002, 0.113, -16.79)

    if i_target == 0:
        target_pos = Vec3(0.0035, 0.012, -16.79)

    if i_angle == 0:
        selected_dart.update = update_throw_flat
        target_pos.y -= 0.008
    elif i_angle == 1:
        selected_dart.update = update_throw_medium
    elif i_angle == 2:
        selected_dart.update = update_throw_steep
        target_pos.y += 0.0087


app = Ursina(
    title="Dartwurf Simulation"
)

camera.position = 0, 0, -19.4
# Shader und die Schriftanzeige werden gesetzt
Entity.default_shader = lit_with_shadows_shader
Text.default_font = r"fonts\arial_unicode_ms_bold.otf"
Text.resolution = 200
# EditorCamera()
window.fullscreen = True

settings_entities = []

b = 0
start_pos = Vec3(0.12, 0.112, -19)
color_buttons = rgb(112/255, 146/255, 190/255)
i_selected_dart = 0
i_camera_position = 0
camera_positions_list = ["Frontal", "Seitwärts"]
speed = 1
i_speed = 0
speed_list = [1.0, 0.1, 0.25, 0.5, 0.75]
i_angle = 1
angle_list = ["Flach", "Mittel", "Steil"]
i_target = 0

start_button = Button(
    text="Start",
    parent=camera.ui,
    position=(0, -0.35),
    color=color_buttons,
    scale=(0.4, 0.175),
    text_size=2.5,
    text_origin=(0, -0.05)
)

start_button.on_click = start

settings_button = Button(
    text="Einstellungen",
    parent=camera.ui,
    position=(0.55, -0.35),
    color=color_buttons,
    scale=(0.35, 0.125),
    text_size=1.5,
    text_origin=(0, -0.01)
)

settings_button.on_click = settings

quit_button = Button(
    text="Schliessen",
    parent=camera.ui,
    position=(-0.55, -0.35),
    color=color_buttons,
    scale=(0.35, 0.125),
    text_size=1.5,
    text_origin=(0, -0.01)
)

quit_button.on_click = quit

switch_r_button = Button(
    text="▶",
    parent=camera.ui,
    position=(0.6, 0.1),
    color=color_buttons,
    scale=(0.1),
    text_size=2,
    text_origin=(0, -0.1)
)

switch_r_button.on_click = switch_r

switch_l_button = Button(
    text="◀",
    parent=camera.ui,
    position=(-0.6, 0.1),
    color=color_buttons,
    scale=(0.1),
    text_size=2,
    text_origin=(0, -0.1)
)

switch_l_button.on_click = switch_l

settings_title = Text(
    text="Einstellungen",
    parent=camera.ui,
    position=(0, 0.4),
    scale=2,
    origin=(0, 0),

)

camera_position_title = Text(
    text="Kameraperspektive:",
    parent=camera.ui,
    position=(-0.2, 0.32),
    scale=1,
    origin=(0, 0.5),
)

camera_position_r_button = Button(
    text="\n▶\n",
    parent=camera.ui,
    position=(0.3, 0.31),
    color=color_buttons,
    scale=(0.05),
    text_size=2,
    text_origin=(0, -0.4)
)

camera_position_r_button.on_click = camera_position_r

camera_position_l_button = Button(
    text="\n◀\n",
    parent=camera.ui,
    position=(0.06, 0.31),
    color=color_buttons,
    scale=(0.05),
    text_size=2,
    text_origin=(0, -0.4)
)

camera_position_l_button.on_click = camera_position_l

camera_position_text = Text(
    text="Frontal",
    parent=camera.ui,
    position=(0.18, 0.32),
    scale=1,
    origin=(0, 0.5),
)

speed_title = duplicate(
    camera_position_title,
    text="Wiedergabegeschwindigkeit:",
    position=(-0.2, 0.22),
)

speed_r_button = Button(
    text="\n▶\n",
    parent=camera.ui,
    position=(0.3, 0.21),
    color=color_buttons,
    scale=(0.05),
    text_size=2,
    text_origin=(0, -0.4)
)

speed_r_button.on_click = speed_r

speed_l_button = Button(
    text="\n◀\n",
    parent=camera.ui,
    position=(0.06, 0.21),
    color=color_buttons,
    scale=(0.05),
    text_size=2,
    text_origin=(0, -0.4)
)

speed_l_button.on_click = speed_l

speed_text = duplicate(
    camera_position_text,
    text="1.0",
    position=(0.18, 0.22)
)

angle_title = duplicate(
    camera_position_title,
    text="Einschlagswinkel:",
    position=(-0.2, 0.12)
)

angle_r_button = Button(
    text="\n▶\n",
    parent=camera.ui,
    position=(0.3, 0.11),
    color=color_buttons,
    scale=(0.05),
    text_size=2,
    text_origin=(0, -0.4)
)

angle_r_button.on_click = angle_r

angle_l_button = Button(
    text="\n◀\n",
    parent=camera.ui,
    position=(0.06, 0.11),
    color=color_buttons,
    scale=(0.05),
    text_size=2,
    text_origin=(0, -0.4)
)

angle_l_button.on_click = angle_l

angle_text = duplicate(
    camera_position_text,
    text="Mittel",
    position=(0.18, 0.12)
)

target_title = duplicate(
    camera_position_title,
    text="Zielfeld:",
    position=(-0.3, 0.02),
)

bull_button = Button(
    text="Bull's eye",
    parent=target_title,
    position=(0.135, -0.01),
    color=color_buttons,
    scale=(0.14, 0.05),
    text_origin=(0, -0.1)
)

bull_button.color = bull_button.color.tint(-0.2)
bull_button._collision = False

t20_button = Button(
    text="T20",
    parent=target_title,
    position=(0.26, -0.01),
    color=color_buttons,
    scale=(0.07, 0.05),
    text_origin=(0, -0.1)
)

t19_button = Button(
    text="T19",
    parent=target_title,
    position=(0, -0.01),
    color=color_buttons,
    scale=(0.07, 0.05),
    text_origin=(0, -0.1)
)

t19_button.x = t20_button.x + 0.09

t18_button = Button(
    text="T18",
    parent=target_title,
    position=(0, -0.01),
    color=color_buttons,
    scale=(0.07, 0.05),
    text_origin=(0, -0.1)
)

t18_button.x = t19_button.x + 0.09

d20_button = Button(
    text="D20",
    parent=target_title,
    position=(0, -0.01),
    color=color_buttons,
    scale=(0.07, 0.05),
    text_origin=(0, -0.1)
)

d20_button.x = t18_button.x + 0.09

d16_button = Button(
    text="D16",
    parent=target_title,
    position=(0, -0.01),
    color=color_buttons,
    scale=(0.07, 0.05),
    text_origin=(0, -0.1)
)

d16_button.x = d20_button.x + 0.09

d12_button = Button(
    text="D12",
    parent=target_title,
    position=(0, -0.01),
    color=color_buttons,
    scale=(0.07, 0.05),
    text_origin=(0, -0.1)
)

d12_button.x = d16_button.x + 0.09

d10_button = Button(
    text="D10",
    parent=target_title,
    position=(0, -0.01),
    color=color_buttons,
    scale=(0.07, 0.05),
    text_origin=(0, -0.1)
)

d10_button.x = d12_button.x + 0.09

d8_button = Button(
    text="D8",
    parent=target_title,
    position=(0, -0.01),
    color=color_buttons,
    scale=(0.07, 0.05),
    text_origin=(0, -0.1)
)

d8_button.x = d10_button.x + 0.09

back_to_menu_button = Button(
    text="Zurück zum\nHauptmenü",
    parent=camera.ui,
    position=(0.55, -0.35),
    color=color_buttons,
    scale=(0.35, 0.125),
    text_size=1.5,
    text_origin=(0, -0.01),
)

back_to_menu_button.on_click = back_to_menu

board = Entity(
    model=r"models_compressed\board\board.obj",
    scale=(1),
    rotation=(0, 90, 0),
    position=(0, 0, -16.74),
    collider="box"
)

board.enabled = False

dart1 = Entity(
    model=r"models_compressed\darts\dart1\dart1.obj",
    scale=(100),
    rotation=(-10, 25, 20),
    position=(0, 0.2, 0),
    collider="box"
)

dart2 = Entity(
    model=r"models_compressed\darts\dart2\dart2.obj",
    scale=(100),
    rotation=(-10, 25, 20),
    position=(7, 0.2, 0),
    collider="box"
)


def input(key):
    if key == "t":
        print_on_screen("rotate")
        camera.rotation_y += 90

    if key == "p":
        print_on_screen(camera.position)

    if key == "w":
        camera.position += camera.forward

    if key == "s":
        camera.position += camera.back

    if key == "a":
        camera.position += camera.left

    if key == "d":
        camera.position += camera.right

    if key == "k":
        camera.position = (-4, 0, -17.8)
        camera.rotation = (0, 90, 0)

    if key == "r":
        camera.position = (0, 0, -19.4)
        camera.rotation = (0, 0, 0)

    if key == "space" and start_button.enabled == True:
        start()

    if key == "s" and start_button.enabled == True:
        settings()

    if key == "escape" and back_to_menu_button.enabled == False:
        quit()

    if key == "escape" and back_to_menu_button.enabled == True:
        back_to_menu()

    if key == "left arrow" and switch_l_button.collision == True:
        switch_l()

    if key == "right arrow" and switch_r_button.collision == True:
        switch_r()


darts_list = [dart1, dart2]
selected_dart = darts_list[0]

light = DirectionalLight(position=Vec3(-1, 2, -1))

main_menu_entities = [start_button, settings_button,
                      quit_button, switch_r_button, switch_l_button]
main_menu_entities += darts_list

settings_entities_add = [settings_title, camera_position_r_button,
                         camera_position_l_button, back_to_menu_button,
                         camera_position_title, camera_position_text,
                         speed_r_button, speed_l_button, speed_title, speed_text,
                         angle_title, angle_r_button, angle_l_button, angle_text,
                         target_title, bull_button, t20_button, t19_button, t18_button,
                         d20_button, d16_button, d12_button, d10_button, d8_button]

settings_entities += settings_entities_add

target_buttons_list = [
    bull_button, t20_button, t19_button, t18_button, d20_button, d16_button, d12_button, d10_button, d8_button
]

for y in settings_entities:
    y.enabled = False

main_menu()

app.run()
