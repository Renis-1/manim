import tkinter as tk
from tkinter import messagebox
from manim import *
import subprocess
import os
from pathlib import Path


class AdditionOperations(Scene):
    def __init__(self, z1, z2, **kwargs):
        self.z1 = z1
        self.z2 = z2
        super().__init__(**kwargs)

    def construct(self):
        plane = ComplexPlane(background_line_style={"stroke_opacity": 0}).add_coordinates()
        title = Text("Dodawanie", font_size=36, color=BLUE).to_corner(UP + LEFT)
        self.play(FadeIn(plane, shift=UP))
        self.play(Write(title))

        z1 = self.z1
        z2 = self.z2
        z_sum = z1 + z2

        point_z1 = Dot(plane.n2p(z1), color=RED)
        label_z1 = Text(f"z1 = {z1.real} + {z1.imag}i", font_size=15, color=RED).next_to(point_z1, UR, buff=0.1)
        arrow_z1 = Arrow(plane.n2p(0), plane.n2p(z1), color=RED)

        point_z2 = Dot(plane.n2p(z2), color=GREEN)
        label_z2 = Text(f"z2 = {z2.real} + {z2.imag}i", font_size=15, color=GREEN).next_to(point_z2, UR, buff=0.1)
        arrow_z2 = Arrow(plane.n2p(0), plane.n2p(z2), color=GREEN)

        point_z_sum = Dot(plane.n2p(z_sum), color=ORANGE)
        label_z_sum = Text(f"z1 + z2 = {z_sum.real} + {z_sum.imag}i", font_size=15, color=ORANGE).next_to(point_z_sum,
                                                                                                          UR, buff=0.1)
        arrow_z_sum = Arrow(plane.n2p(0), plane.n2p(z_sum), color=ORANGE, buff=0)

        z2_vector = DashedLine(start=plane.n2p(0), end=plane.n2p(z2), color=YELLOW)
        result_vector = DashedLine(start=plane.n2p(z1), end=plane.n2p(z_sum), color=YELLOW)

        self.play(GrowArrow(arrow_z1), FadeIn(point_z1, label_z1))
        self.wait(1)
        self.play(GrowArrow(arrow_z2), FadeIn(point_z2, label_z2))
        self.wait(1)
        self.play(Create(z2_vector))
        self.wait(1)
        self.play(ReplacementTransform(z2_vector, result_vector))
        self.play(GrowArrow(arrow_z_sum), FadeIn(point_z_sum, label_z_sum))
        self.wait(4)


def create_animation(z1, z2):
    output_file = "addition_operations.mp4"

    class CustomScene(AdditionOperations):
        def __init__(self, **kwargs):
            super().__init__(z1, z2, **kwargs)

    config.media_width = "75%"
    scene = CustomScene()
    scene.render()

    # Moving the output video to the current directory
    rendered_video_path = next(Path(".").rglob("**/AdditionOperations.mp4"))
    os.rename(rendered_video_path, output_file)

    # Play the video using a media player
    if os.name == 'nt':  # for Windows
        os.startfile(output_file)
    elif os.name == 'posix':  # for Linux, macOS
        subprocess.run(['xdg-open', output_file])


def on_submit():
    try:
        z1_real = float(entry_z1_real.get())
        z1_imag = float(entry_z1_imag.get())
        z2_real = float(entry_z2_real.get())
        z2_imag = float(entry_z2_imag.get())

        z1 = complex(z1_real, z1_imag)
        z2 = complex(z2_real, z2_imag)

        create_animation(z1, z2)
        messagebox.showinfo("Success", "Animation created successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for the complex numbers.")


root = tk.Tk()
root.title("Complex Number Addition Animation")

tk.Label(root, text="z1 Real Part:").grid(row=0, column=0)
tk.Label(root, text="z1 Imaginary Part:").grid(row=1, column=0)
tk.Label(root, text="z2 Real Part:").grid(row=2, column=0)
tk.Label(root, text="z2 Imaginary Part:").grid(row=3, column=0)

entry_z1_real = tk.Entry(root)
entry_z1_imag = tk.Entry(root)
entry_z2_real = tk.Entry(root)
entry_z2_imag = tk.Entry(root)

entry_z1_real.grid(row=0, column=1)
entry_z1_imag.grid(row=1, column=1)
entry_z2_real.grid(row=2, column=1)
entry_z2_imag.grid(row=3, column=1)

submit_button = tk.Button(root, text="Create Animation", command=on_submit)
submit_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
