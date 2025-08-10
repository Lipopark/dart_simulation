from ursina import *
from ursina.shaders import lit_with_shadows_shader


def main_menu():
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
        model=r"models\darts\models_compressed\dart1.obj",
        scale=(100),
        rotation=(-10, 25, 20),
        position=(0, 0.2, 0)
    )


app = Ursina(
    title="Dartwurf Simulation"
)

Entity.default_shader = lit_with_shadows_shader
Text.default_font = r"fonts\arial_unicode_ms_bold.otf"
Text.resolution = 200
EditorCamera()

main_menu()

app.run()
