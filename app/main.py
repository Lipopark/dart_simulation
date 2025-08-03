from ursina import *


def main_menu():
    start_button = Button(
        text="Start",
        parent=camera.ui,
        position=(0, -0.35),
        color=rgb(112/255, 146/255, 190/255),
        scale=(0.35, 0.125),
        text_size=2,
        text_origin=(0, -0.05))

    settings_button = Button(
        text="Einstellungen",
        parent=camera.ui,
        position=(0.55, -0.35),
        color=rgb(112/255, 146/255, 190/255),
        scale=(0.35, 0.125),
        text_size=1.5,
        text_origin=(0, -0.01)
    )

    dart1 = Entity(model="dart1.blend")


app = Ursina()

Text.default_font = "poppins\Poppins-Bold.ttf"
Text.resolution = 100

main_menu()

app.run()
