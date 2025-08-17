from ursina import *
from ursina.shaders import *


def main_menu():

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

    def start():

        # Alle Menu Entities werden deaktiviert
        for y in main_menu_entities:
            y.enabled = False

        # Der ausgewählte Dart wird in Startposition gebracht
        selected_dart.scale = 1
        selected_dart.position = (0.12, 0, -20)
        selected_dart.rotation = (67, 176.9, 0)
        selected_dart.enabled = True
        selected_dart.x_rot_speed = 10

        # Board wird angezeigt
        board.enabled = True

        # Animation startet
        def update():
            selected_dart.position -= selected_dart.forward / 9.35
            selected_dart.rotation_x -= selected_dart.x_rot_speed

            # Übergang von Phase 1 des Wurfs in Phase 2 wird überprüft
            if selected_dart.rotation_x <= 13:
                selected_dart.x_rot_speed = 2

            # Bei Kollision mit dem Board wird die Update Funktion beendet
            if selected_dart.intersects(board):
                selected_dart.update = False

        selected_dart.update = update

    start_button = Button(
        text="Start",
        parent=camera.ui,
        position=(0, -0.35),
        color=color_buttons,
        scale=(0.4, 0.175),
        text_size=2.5,
        text_origin=(0, -0.05)
    )

    settings_button = Button(
        text="Einstellungen",
        parent=camera.ui,
        position=(0.55, -0.35),
        color=color_buttons,
        scale=(0.35, 0.125),
        text_size=1.5,
        text_origin=(0, -0.01)
    )

    switch_r_button = Button(
        text="▶",
        parent=camera.ui,
        position=(0.6, 0.1),
        color=color_buttons,
        scale=(0.1),
        text_size=2,
        text_origin=(0, -0.1)
    )

    switch_l_button = Button(
        text="◀",
        parent=camera.ui,
        position=(-0.6, 0.1),
        color=color_buttons,
        scale=(0.1),
        text_size=2,
        text_origin=(0, -0.1)
    )

    board = Entity(
        model=r"models_compressed\board\board.obj",
        texture=r"\models\board\board_picture.jpg",
        scale=(1),
        rotation=(0, 90, 0),
        position=(0, 0, -17.74),
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

    global darts_list
    darts_list = [dart1, dart2]
    main_menu_entities = [start_button, settings_button,
                          switch_r_button, switch_l_button]
    main_menu_entities += darts_list

    # Beim Start wird standartmässig der erste Dart angezeigt und der Switch Button nach links deaktiviert
    darts_list[0]
    switch_l_button.collision = False
    switch_r_button.on_click = switch_r
    switch_l_button.on_click = switch_l
    start_button.on_click = start


app = Ursina(
    title="Dartwurf Simulation"
)


x = 0
color_buttons = rgb(112/255, 146/255, 190/255)

# Shader und die Schriftanzeige werden gesetzt
Entity.default_shader = lit_with_shadows_shader
Text.default_font = r"fonts\arial_unicode_ms_bold.otf"
Text.resolution = 200
EditorCamera()


main_menu()

selected_dart = darts_list[0]

app.run()
