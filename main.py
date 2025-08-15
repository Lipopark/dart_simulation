from ursina import *
from ursina.shaders import *


def main_menu():

    def switch_r():
        global selected_dart
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
        for y in main_menu_entities:
            y.enabled = False
            selected_dart.enabled = True

    start_button = Button(
        text="Start",
        parent=camera.ui,
        position=(0, -0.35),
        color=rgb(112/255, 146/255, 190/255),
        scale=(0.4, 0.175),
        text_size=2.5,
        text_origin=(0, -0.05)
    )

    settings_button = Button(
        text="Einstellungen",
        parent=camera.ui,
        position=(0.55, -0.35),
        color=rgb(112/255, 146/255, 190/255),
        scale=(0.35, 0.125),
        text_size=1.5,
        text_origin=(0, -0.01)
    )

    switch_r_button = Button(
        text="▶",
        parent=camera.ui,
        position=(0.6, 0.1),
        color=rgb(112/255, 146/255, 190/255),
        scale=(0.1),
        text_size=2,
        text_origin=(0, -0.1)
    )

    switch_l_button = Button(
        text="◀",
        parent=camera.ui,
        position=(-0.6, 0.1),
        color=rgb(112/255, 146/255, 190/255),
        scale=(0.1),
        text_size=2,
        text_origin=(0, -0.1)
    )

    dart1 = Entity(
        model=r"models_compressed\darts\dart1\dart1.obj",
        scale=(100),
        rotation=(-10, 25, 20),
        position=(0, 0.2, 0)
    )

    dart2 = Entity(
        model=r"models_compressed\darts\dart2\dart2.obj",
        scale=(100),
        rotation=(-10, 25, 20),
        position=(7, 0.2, 0)
    )

    global darts_list
    darts_list = [dart1, dart2]
    main_menu_entities = [start_button, settings_button,
                          switch_r_button, switch_l_button]
    main_menu_entities += darts_list
    darts_list[0]
    switch_l_button.collision = False
    switch_r_button.on_click = switch_r
    switch_l_button.on_click = switch_l
    start_button.on_click = start


app = Ursina(
    title="Dartwurf Simulation"
)


x = 0
Entity.default_shader = lit_with_shadows_shader
Text.default_font = r"fonts\arial_unicode_ms_bold.otf"
Text.resolution = 200
# EditorCamera()


main_menu()

selected_dart = darts_list[0]

app.run()
