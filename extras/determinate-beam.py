import tkinter as tk
from math import pow

elasticity = None

def draw_shear_force_diagram(length, a, reaction_a, reaction_b, load, beam_type):
    shear_force_canvas.delete("all")
    if beam_type == "Simply Supported":
        if a !=0 or a == length:
            if a == length:
                x1 = 5
                y1 = 150
                x2 = 450
                shear_force_canvas.create_line(x1, y1,x2,y1, width=2, fill="green")

            elif load >= 0:
                x1 = 5
                x2 = int(a * (450 / length))
                x3 = int(450)-50
                y1 = 50
                y2 = 75
                y3 = y2-y1
                y4 = 50
                shear_force_canvas.create_line(x1, y1, x1, y2, x2, y2, x2, y3 , x3, y3, x3, y4, width=2, fill="green")
                shear_force_canvas.create_text(x1 +20 , y1, text=f"0 N")
                shear_force_canvas.create_text(x1 +20 , y2 + 10, text=f"{(reaction_a):.2f} N")
                shear_force_canvas.create_text(x2 +20 , y2 + 10, text=f"{(reaction_a):.2f} N")
                shear_force_canvas.create_text(x2 +20 , y3 - 10, text=f"{(reaction_a + load):.2f} N")
                shear_force_canvas.create_text(x3 - 20 , y3 - 10, text=f"{(reaction_a + load):.2f} N")
                shear_force_canvas.create_text(x3 - 20 , y3 + 20, text=f" 0 N")
            else:
                x1 = 5
                x2 = int(a * (450 / length))
                x3 = int(450)-50
                y1 = 50
                y2 = 25
                y3 = y1+y2
                y4 = 50
                shear_force_canvas.create_line(x1, y1, x1, y2, x2, y2, x2, y3 , x3, y3, x3, y4, width=2, fill="green")
                shear_force_canvas.create_text(x1 +20 , y1, text=f"0 N")
                shear_force_canvas.create_text(x1 +20 , y2 - 15, text=f"{(reaction_a):.2f} N")
                shear_force_canvas.create_text(x2 +20 , y2 - 15, text=f"{(reaction_a):.2f} N")
                shear_force_canvas.create_text(x2 +20 , y3 + 20, text=f"{(reaction_a + load):.2f} N")
                shear_force_canvas.create_text(x3 - 20 , y3 + 20, text=f"{(reaction_a + load):.2f} N")
                shear_force_canvas.create_text(x3 - 20 , y1, text=f" 0 N")

    elif beam_type == "Cantilever":
        if a !=0:
            if a == length:
                x1 = 5
                y1 = 150
                x2 = 450
                shear_force_canvas.create_line(x1, y1,x2,y1, width=2, fill="green")
            elif load >= 0:
                x1 = 5
                x2 = int(a * (450 / length))
                x3 = int(450)
                y1 = 25
                y2 = 150
                y3 = 25
                shear_force_canvas.create_line(x1, y1, x1, y2, x2, y2, x2, y3 , x3, y1, width=2, fill="green")
                shear_force_canvas.create_text(x1 +20 , y1, text=f"0 N")
                shear_force_canvas.create_text(x1 +20 , y2-20, text=f"{(reaction_a):.2f} N")
                shear_force_canvas.create_text(x2 +20 , y2-20, text=f"{(reaction_a):.2f} N")
                shear_force_canvas.create_text(450 - 20 , y1 + 10, text=f"0 N")
            else:
                x1 = 5
                x2 = int(a * (450 / length))
                x3 = int(450)
                y1 = 150
                y2 = 25
                y3 = 150
                shear_force_canvas.create_line(x1, y1, x1, y2, x2, y2, x2, y3 , x3, y1, width=2, fill="green")
                shear_force_canvas.create_line(x1, y1, x1, y2, x2, y2, x2, y3 , x3, y1, width=2, fill="green")
                shear_force_canvas.create_text(x1 +20 , y1-10, text=f"0 N")
                shear_force_canvas.create_text(x1 +20 , y2-10, text=f"{(reaction_a):.2f} N")
                shear_force_canvas.create_text(x2 +20 , y2-10, text=f"{(reaction_a):.2f} N")

def draw_bending_moment_diagram(length, a, reaction_a, reaction_b, load, beam_type):
    bending_moment_canvas.delete("all")
    scale = bending_moment_canvas.winfo_width() / length

    # Draw bending moment diagram
    if beam_type == "Simply Supported":
        if a !=0 or a == length :
            if load >= 0:
                x1 = 0
                x2 = int(a * (450 / length))
                x3 = int(450)
                y1 = bending_moment_canvas.winfo_height() - 74
                y2 = 150
                bending_moment_canvas.create_line(x1, y1, x2, y2, x3, y1, width=2, fill="red")
                bending_moment_canvas.create_text(x1 +20 , y1, text=f"0 Nm")
                bending_moment_canvas.create_text(x2 +20 , y2 - 15, text=f"{(reaction_a *a):.2f} Nm")
                bending_moment_canvas.create_text(450-75 , y1, text=f" 0 Nm")
            else:
                x1 = 0
                x2 = int(a * (450 / length))
                x3 = int(450)-50
                y1 = bending_moment_canvas.winfo_height() - 74
                y2 = 10
                bending_moment_canvas.create_line(x1, y1, x2, y2, x3, y1, width=2, fill="red")
                bending_moment_canvas.create_line(x1, y1, x2, y2, x3, y1, width=2, fill="red")
                bending_moment_canvas.create_text(x1 +20 , y1, text=f"0 Nm")
                bending_moment_canvas.create_text(x2 +20 , y2 + 15 , text=f"{(reaction_a *a):.2f} Nm")
                bending_moment_canvas.create_text(450-75 , y1, text=f" 0 Nm")


    elif beam_type == "Cantilever":
        if a !=0:
            if load >= 0:
                x1 = 0
                x2 = int(a * (450 / length))
                x3 = int(450)
                y1 = bending_moment_canvas.winfo_height() - 74
                y2 = 150
                bending_moment_canvas.create_line(x1, y1, x2, y2,x2,y1,x3, y1, width=2, fill="red")
                bending_moment_canvas.create_text(x1 +20 , y1-10, text=f"0 Nm")
                bending_moment_canvas.create_text(x2 +30 , y2 - 10, text=f"{(reaction_a *a):.2f} Nm")
                bending_moment_canvas.create_text(450-75 , y1+10, text=f" 0 Nm")
            else:
                x1 = 0
                x2 = int(a * (450 / length))
                x3 = int(450)
                y1 = bending_moment_canvas.winfo_height() - 74
                y2 = 10
                bending_moment_canvas.create_line(x1, y1, x2, y2,x2,y1,x3, y1, width=2, fill="red")
                bending_moment_canvas.create_text(x1 +20 , y1+10, text=f"0 Nm")
                bending_moment_canvas.create_text(x2 +30 , y2 + 10, text=f"{(reaction_a *a):.2f} Nm")
                bending_moment_canvas.create_text(450-75 , y1-10, text=f" 0 Nm")

def calculate_beam():
    global elasticity
    try:
        length = float(length_entry.get())
        load = float(load_entry.get())
        a = float(a_entry.get())
        height = float(height_entry.get())

        # Get the modulus of elasticity input
        elasticity = float(elasticity_entry.get())

        moment_of_inertia = (1/12) * pow(height, 4)

        reaction_a = -load * a / length
        reaction_b = -load * (length - a) / length
        moment_a = -load * a
        moment_b = -load * (a-length)

        max_moment = (-load * length + load * a) / 8

        reaction_a_label.config(text=f"Reaction A: {abs(reaction_a):.2f} N")
        reaction_b_label.config(text=f"Reaction B: {abs(reaction_b):.2f} N")
        max_moment_label.config(text=f"Max Bending Moment: {max_moment:.2f} Nm")

        if elasticity is not None:
            if beam_type.get() == "Simply Supported":
                max_deflection = (5 * load * pow(length, 4)) / (384 * elasticity * moment_of_inertia)
                stress = (6 * load * a) / (moment_of_inertia * pow(length, 2))
            elif beam_type.get() == "Cantilever":
                max_deflection = (load * pow(length, 3)) / (3 * elasticity * moment_of_inertia)
                stress = (load * a) / (moment_of_inertia * height)
                reaction_a = -load
                reaction_b = 0
                reaction_b_label.config(text="Reaction B: N/A")

            max_deflection_label.config(text=f"Max Deflection: {max_deflection:.2f} m")
            stress_label.config(text=f"Max Stress: {stress:.2f} N/m^2")
        else:
            max_deflection_label.config(text="Please set the Modulus of Elasticity.")
            stress_label.config(text="")

        canvas.delete("all")
        draw_beam_diagram(length, a, reaction_a, reaction_b, load, beam_type.get())
        draw_shear_force_diagram(length, a, reaction_a, reaction_b, load, beam_type.get())
        draw_bending_moment_diagram(length, a, reaction_a, reaction_b, load, beam_type.get())

    except (ValueError, ZeroDivisionError):
        reaction_a_label.config(text="Please enter valid numbers for input.")
        reaction_b_label.config(text="")
        max_moment_label.config(text="")
        max_deflection_label.config(text="")
        stress_label.config(text="")

def draw_beam_diagram(length, a, reaction_a, reaction_b, load, beam_type):
    canvas_width = 500
    canvas_height = 250
    canvas.config(width=canvas_width, height=canvas_height)
    moment_a = -load * a
    moment_b = -load * (1-a)
    scale = canvas_width / length

    canvas.create_rectangle(50, 120, 450, 140, fill="white", outline="black")  # Adjusted beam position

    if beam_type == "Simply Supported":
        support_a_x = 50
        support_a_y = 140
        support_b_x = 450
        support_b_y = 140

        canvas.create_polygon(
            support_a_x - 20, support_a_y + 30,  # bottom left
            support_a_x, support_a_y,  # top
            support_a_x + 20, support_a_y + 30,  # bottom right
            fill="white",
            outline="black"
        )

        canvas.create_oval(
            support_b_x - 20, support_b_y,
            support_b_x + 20, support_b_y + 30,
            fill="white",
            outline="black"
        )
        if load >= 0:
            canvas.create_line(support_a_x, support_a_y + 30, support_a_x, support_a_y + 60, width=2, arrow=tk.LAST)
            canvas.create_line(support_b_x, support_b_y + 30, support_b_x, support_b_y + 60, width=2, arrow=tk.LAST)
        else:
            canvas.create_line(support_a_x, support_a_y + 60, support_a_x, support_a_y + 30, width=2, arrow=tk.LAST)
            canvas.create_line(support_b_x, support_b_y + 60, support_b_x, support_b_y + 30, width=2, arrow=tk.LAST)

        canvas.create_text(support_a_x, support_a_y + 65, text=f"{abs(reaction_a):.2f} N")
        if a != 0:
            canvas.create_text(support_a_x, support_a_y - 30, text=f"{(-moment_a):.2f} Nm")

        canvas.create_text(support_b_x, support_b_y + 65, text=f"{abs(reaction_b):.2f} N")
        if a != length:
            canvas.create_text(support_b_x, support_b_y - 30, text=f"{(moment_b):.2f} Nm")

    elif beam_type == "Cantilever":
        support_a_x = 50
        support_a_y = 130

        canvas.create_rectangle(support_a_x - 25, support_a_y - 50, support_a_x + 25, support_a_y + 50, fill="white",
                                outline="black")
        if load >= 0:
            canvas.create_line(support_a_x, support_a_y + 50, support_a_x, support_a_y + 100, width=2, arrow=tk.LAST)
            canvas.create_text(support_a_x, support_a_y + -60, text=f"{(-moment_a):.2f} Nm")
        else:
            canvas.create_line(support_a_x, support_a_y + 100, support_a_x, support_a_y + 50, width=2, arrow=tk.LAST)
            canvas.create_text(support_a_x, support_a_y + -60, text=f"{(-moment_a):.2f} Nm")

        canvas.create_text(support_a_x, support_a_y + 110, text=f"{abs(reaction_a):.2f} N")

    load_x = 50 + int((400 / length) * a)
    load_y = 120
    if load >= 0:
        canvas.create_line(load_x, load_y, load_x, load_y - 30, width=2, arrow=tk.LAST)
    else:
        canvas.create_line(load_x, load_y - 30, load_x, load_y, width=2, arrow=tk.LAST)

    canvas.create_text(load_x, load_y - 40, text=f"{abs(load):.2f} N")

app = tk.Tk()
app.title("Beam Calculator")

frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

length_label = tk.Label(frame, text="Beam Length (m):")
length_label.grid(row=0, column=0)

length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1)

load_label = tk.Label(frame, text="Applied Load (N):")
load_label.grid(row=1, column=0)

load_entry = tk.Entry(frame)
load_entry.grid(row=1, column=1)

a_label = tk.Label(frame, text="Distance from A to Load (m):")
a_label.grid(row=2, column=0)

a_entry = tk.Entry(frame)
a_entry.grid(row=2, column=1)

beam_type = tk.StringVar()
beam_type.set("Simply Supported")

beam_type_label = tk.Label(frame, text="Select Beam Type:")
beam_type_label.grid(row=5, column=0)

simply_supported_radiobutton = tk.Radiobutton(frame, text="Simply Supported", variable=beam_type, value="Simply Supported")
simply_supported_radiobutton.grid(row=5, column=1)

cantilever_radiobutton = tk.Radiobutton(frame, text="Cantilever", variable=beam_type, value="Cantilever")
cantilever_radiobutton.grid(row=5, column=2)

elasticity_label = tk.Label(frame, text="Modulus of Elasticity (N/m^2):")
elasticity_label.grid(row=3, column=0)

elasticity_entry = tk.Entry(frame)
elasticity_entry.grid(row=3, column=1)

height_label = tk.Label(frame, text="Height of the Beam (m):")
height_label.grid(row=4, column=0)

height_entry = tk.Entry(frame)
height_entry.grid(row=4, column=1)

calculate_button = tk.Button(frame, text="Calculate", command=calculate_beam)
calculate_button.grid(row=6, column=0, columnspan=3)

reaction_a_label = tk.Label(frame, text="Reaction A:")
reaction_a_label.grid(row=7, columnspan=3)

reaction_b_label = tk.Label(frame, text="Reaction B:")
reaction_b_label.grid(row=8, columnspan=3)

max_moment_label = tk.Label(frame, text="Max Bending Moment:")
max_moment_label.grid(row=9, columnspan=3)

max_deflection_label = tk.Label(frame, text="Max Deflection:")
max_deflection_label.grid(row=10, columnspan=3)

stress_label = tk.Label(frame, text="Max Stress:")
stress_label.grid(row=11, columnspan=3)

canvas = tk.Canvas(frame, width=400, height=250)
canvas.grid(row=12, columnspan=3)

shear_force_canvas = tk.Canvas(frame, width=400, height=150)
shear_force_canvas.grid(row=13, columnspan=3)

bending_moment_canvas = tk.Canvas(frame, width=400, height=150)
bending_moment_canvas.grid(row=14, columnspan=3)

app.mainloop()