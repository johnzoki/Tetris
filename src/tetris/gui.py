import tkinter as tk

# from tetris import Board, NextQueue

def button_click():
    gui.destroy()

# NOCH VON WO ANDERS HER IMPORTIEREN
queue = [1, 2, 3]
queue_piece_count = len(queue)

grid_size = 25
piece_space = 4 * grid_size
border_bezzel = grid_size

main_width = 10 * grid_size
main_height = 20 * grid_size
placeholder_width = 2 * border_bezzel + piece_space
placeholder_hight = placeholder_width
queue_width = 2 * border_bezzel + piece_space
queue_hight = 2 * border_bezzel + queue_piece_count * piece_space

#create main window
gui = tk.Tk()
gui.title("The New New Tetris")
gui.geometry("950x700")
#gui.resizable(False, False)
gui['bg']='#856ff8'

# placeholder x1, x2, y1, y2
placeholder_border_x1 = border_bezzel
placeholder_border_y1 = 2 * border_bezzel
placeholder_border_x2 = placeholder_border_x1 + placeholder_width
placeholder_border_y2 = placeholder_border_y1 + placeholder_hight

# main x1, x2, y1, y2
main_border_x1 = placeholder_border_x2 + border_bezzel
main_border_y1 = 2 * border_bezzel
main_border_x2 = main_border_x1 + main_width
main_border_y2 = main_border_y1 + main_height

# queue x1, x2, y1, y2
queue_border_x1 = main_border_x2 + border_bezzel
queue_border_y1 = 2 * border_bezzel
queue_border_x2 = queue_border_x1 + queue_width
queue_border_y2 = queue_border_y1 + queue_hight

canvas_width = border_bezzel + queue_border_x2
canvas_height = 2 * border_bezzel + main_border_y2

# Create a Canvas widget
main_canvas = tk.Canvas(gui, width=canvas_width, height=canvas_height)
main_canvas.pack()

# Create borders on the canvas
placeholder_border = main_canvas.create_rectangle(placeholder_border_x1, placeholder_border_y1, placeholder_border_x2, placeholder_border_y2)
main_border = main_canvas.create_rectangle(main_border_x1, main_border_y1, main_border_x2, main_border_y2)
queue_border = main_canvas.create_rectangle(queue_border_x1, queue_border_y1, queue_border_x2, queue_border_y2)

# Create grid in main
for x in range(0, main_width, grid_size):
    main_canvas.create_line(
        main_border_x1 + x, main_border_y1, main_border_x1 + x, main_border_y2, 
        fill="lightgray",
        dash = (2, 4)
    )

for y in range(0, main_height, grid_size):
    main_canvas.create_line(
        main_border_x1, main_border_y1 + y, main_border_x2, main_border_y1 + y, 
        fill="lightgray",
        dash = (2, 4)
    )

# Create a button
button = tk.Button(gui, text="Close window", bg='#856ff8', fg='black', command=button_click)
button.pack()

#run
gui.mainloop()