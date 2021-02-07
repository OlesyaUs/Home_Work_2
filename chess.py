white_figure_vertical = int(input('Введите позицию белой фигуры по вертикали:'))
white_figure_horizontal = int(input('Введите позицию белой фигуры по горизонтали:'))

black_figure_vertical = int(input('Введите позицию черной фигуры по вертикали:'))
black_figure_horizontal = int(input('Введите позицию черной фигуры по горизонтали:'))

move_vertical = int(input('Куда идем по вертикали?: '))
move_horizontal = int(input('Куда идем по горизонтали?: '))

which_figure = input("Какой фигурой ходим?: ")
if which_figure == "Ладья":
    if move_horizontal == white_figure_horizontal or move_vertical == white_figure_vertical:
        if move_horizontal == black_figure_horizontal:
            print('Вы под ударом')
        elif move_vertical == black_figure_vertical:
            print('Вы под ударом')
        else:
            print('Вы можете ходить безопасно')

    else:
        print("Так ходить нельзя")
kon_vertical = 0
kon_horizontal = 0

if which_figure == "Конь":



