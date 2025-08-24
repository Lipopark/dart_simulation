from ursina import *
from ursina.shaders import *


def main_menu():
    global darts_list
    # Ist der erste Dart ausgewählt, wird der Button nach links deaktiviert
    if x == 0:
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

    # Der x-te Dart ist immer der ausgewählte Dart
    global x
    x += 1
    selected_dart.position = -10, 0.2, 0
    selected_dart = darts_list[x]
    selected_dart.position = 0, 0.2, 0
    switch_l_button.collision = True
    if x == 1:
        switch_r_button.collision = False


def switch_l():
    global selected_dart
    global x
    x -= 1
    selected_dart.position = 7, 0.2, 0
    selected_dart = darts_list[x]
    selected_dart.position = 0, 0.2, 0
    switch_r_button.collision = True
    if x == 0:
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


def back_to_menu():
    # Alles wird zurückgesetzt, damit es wieder wie im Hauptmenü aussieht. Der ausgewählte Dart bleibt aber ausgewählt
    back_to_menu_button.enabled = False
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
    # selected_dart.position = (0.12, 0, -19)
    selected_dart.position = (0.12, -0.2, -19)
    selected_dart.rotation = (45, 176.9, 0)
    selected_dart.enabled = True

    # Board wird angezeigt
    board.enabled = True

    selected_dart.throw_dir = selected_dart.back.normalized()
    rot_per_unit = 83
    # Animation startet

    def update():
        distance_per_frame = speed * time.dt
        # Übergang von Phase 1 des Wurfs in Phase 2 wird überprüft
        # if selected_dart.z <= -18.519989013671875:
        if selected_dart.rotation_x >= 0:
            # Phase 1
            selected_dart.position += selected_dart.throw_dir * distance_per_frame
            selected_dart.rotation_x -= rot_per_unit * distance_per_frame

        else:
            selected_dart.rotation_x = 0
            selected_dart.update = False
            selected_dart.update = update_phase_2

    def update_phase_2():
        # Kollision mit Board ca. bei selected_dart.x = 0.0953
        if selected_dart.intersects(board):
            selected_dart.update = False
            back_to_menu_button.enabled = True
        else:
            # Phase 2
            selected_dart.position += selected_dart.back * speed * time.dt
            selected_dart.rotation_x

    selected_dart.update = update


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

speed = 0.1

color_buttons = rgb(112/255, 146/255, 190/255)
i_camera_position = 1

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
    # model=r"models_compressed\board\board_distance.obj",
    texture=r"\models\board\board_picture.jpg",
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

# Anzeigeeinstellung


def input(key):
    if key == "t":
        print_on_screen("rotate")
        camera.rotation_y += 90

    if key == "p":
        print_on_screen(camera.position)

    if key == "w":
        camera.position += camera.forward

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


x = 0


darts_list = [dart1, dart2]
main_menu_entities = [start_button, settings_button,
                      quit_button, switch_r_button, switch_l_button]
main_menu_entities += darts_list

settings_entities = [settings_title, camera_position_r_button,
                     camera_position_l_button, back_to_menu_button, camera_position_title, camera_position_text]
for y in settings_entities:
    y.enabled = False

camera_positions_list = ["Frontal", "Seitwärts"]
camera_position = camera_positions_list[0]

main_menu()

selected_dart = darts_list[0]

app.run()
