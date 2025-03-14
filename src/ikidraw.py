"""Module to draw Ikigai circles based on user evaluation.

This module defines the `ikigai_draw` function, which uses the Turtle graphics library to visually represent 
the user's evaluation in the form of overlapping circles, highlighting key areas of their Ikigai.
"""

def ikigai_draw(value_love: float, value_good: float, value_money: float, value_world: float, 
                value_max: float, value_minTrue: float, text_conclusion: str, text_advice: str, 
                your_name: str, test_date: str):
    """Draws Ikigai circles based on user evaluation.

    This function uses the Turtle graphics library to create a visual representation of the user's 
    self-assessment in four key areas (Love, Good At, Paid For, World Needs). It also calculates and 
    displays related values such as Passion, Mission, Vocation, and Profession.

    Args:
        value_love (float): User's evaluation for "What you love."
        value_good (float): User's evaluation for "What you're good at."
        value_money (float): User's evaluation for "What you can be paid for."
        value_world (float): User's evaluation for "What the world needs."
        value_max (float): Maximum possible value for the evaluations.
        value_minTrue (float): Minimum acceptable value for the evaluations.
        text_conclusion (str): Conclusion text to display in the drawing.
        text_advice (str): Advice text to display in the drawing.
        your_name (str): Name of the user.
        test_date (str): Date of the evaluation.
    """
    import turtle

    if __name__ == '__main__':
        import drawdef  # Import for direct testing of this file.
    else:
        from src import drawdef  # Import for use within the main module.

    msg_check_draw = 'Do not forget to check the Ikigai drawing with the results in the pop-up window.'
    print('\n\n', msg_check_draw)

    # CALCULATIONS FOR EVALUATION --------------------------------------------------------
    from statistics import mean

    LWMG = (value_love, value_world, value_good, value_money)
    score_LWMG_avr = mean(LWMG)

    passion = (value_good, value_love)
    value_passion = mean(passion)

    mission = (value_world, value_love)
    value_mission = mean(mission)

    vocation = (value_world, value_money)
    value_vocation = mean(vocation)

    profession = (value_good, value_money)
    value_profession = mean(profession)

    # DRAWING SETTINGS -------------------------------------------------------------------
    turtle.speed(0)  # 0 = fastest, 1 = slowest, 10 = fast.
    turtle.hideturtle()  # Hide the turtle cursor.

    center_righ = -13  # Horizontal centering offset.
    center_down = 16  # Vertical centering offset.
    center_angle = 6  # Initial angle adjustment for centering circles.

    r = 150  # Radius of circles.
    move = 30  # Distance between circles.

    total_center = 10  # Offset for centering text and values.

    dist = 1.2  # Distance multiplier for placing text inside circles.
    under_names = 25  # Distance for placing text below circle labels.
    LR_dist = 375  # Horizontal distance for side text.
    UD_dist = 300  # Vertical distance for side text.

    # Circle labels
    name_love = 'LOVE'
    name_world = 'WORLD'
    name_money = 'PAID FOR'
    name_good = 'GOOD AT'

    name_passion = 'PASSION'
    name_mission = 'MISSION'
    name_vocation = 'VOCATION'
    name_profession = 'PROFESSION'

    # Text for side labels
    text_up_love = 'Improve the environment.'
    text_right_world = 'Increase the part that helps.'
    text_down_money = 'Ask for more money.'
    text_left_good = 'Learn necessary things.'

    # Final text
    text_name = 'IKIGAI - '
    text_final = f'Conclusion:\n - {text_conclusion}\n\nAdvice:\n {text_advice}'

    # DRAWING FILLED CIRCLES -------------------------------------------------------------
    turtle.color('#AAB7B8', '#AAB7B8')  # Set the fill color for circles.
    turtle.penup()
    turtle.home()
    turtle.forward(center_righ)
    turtle.right(90)
    turtle.forward(center_down)
    turtle.left(center_angle)

    for _ in range(4):
        turtle.penup()
        turtle.left(90)
        turtle.forward(move)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

    # OUTLINE FOR CIRCLES ----------------------------------------------------------------
    turtle.color('white')  # Set the outline color for circles.
    turtle.penup()
    turtle.home()
    turtle.forward(center_righ)
    turtle.right(90)
    turtle.forward(center_down)
    turtle.pensize(3)  # Set pen thickness for better visibility.
    turtle.left(center_angle)

    for _ in range(4):
        turtle.penup()
        turtle.left(90)
        turtle.forward(move)
        turtle.pendown()
        turtle.circle(r)

    # LABELING CIRCLES -------------------------------------------------------------------
    turtle.penup()
    turtle.home()

    for ikig_names in (name_love, name_good, name_money, name_world):
        turtle.left(90)
        turtle.forward(dist * r)
        turtle.write(ikig_names, font=('Arial', 14, 'bold'), align='center')
        turtle.back(dist * r)

    # DISPLAYING VALUES ------------------------------------------------------------------
    turtle.home()
    turtle.right(90)
    turtle.forward(under_names)
    turtle.left(90)

    for ikig_ask in (value_love, value_good, value_money, value_world):
        turtle.left(90)
        turtle.forward(dist * r)
        drawdef.color_by_limits(ikig_ask, value_max, value_minTrue)
        turtle.write(ikig_ask, font=('Arial', 18, 'normal'), align='center')
        turtle.back(dist * r)

    # DISPLAYING FINAL SCORE IN CENTER ---------------------------------------------------
    turtle.home()
    turtle.right(90)
    turtle.forward(total_center)
    drawdef.color_by_limits(score_LWMG_avr, value_max, value_minTrue)
    turtle.write(score_LWMG_avr, font=('Arial', 18, 'normal'), align='center')

    # LABELING SIDE VALUES --------------------------------------------------------------
    turtle.home()
    turtle.right(90)
    turtle.forward(total_center)
    turtle.left(45)
    turtle.color('white')

    for side_name in (name_mission, name_passion, name_profession, name_vocation):
        turtle.left(90)
        turtle.forward(dist * r / 2)
        turtle.write(side_name, font=('Arial', 14, 'bold'), align='center')
        turtle.back(dist * r / 2)

    # DISPLAYING SIDE VALUES ------------------------------------------------------------
    turtle.home()
    turtle.right(90)
    turtle.forward(total_center + under_names)
    turtle.left(45)

    for side_values in (value_mission, value_passion, value_profession, value_vocation):
        drawdef.color_by_limits(side_values, value_max, value_minTrue)
        turtle.left(90)
        turtle.forward(dist * r / 2)
        turtle.write(side_values, font=('Arial', 18, 'normal'), align='center')
        turtle.back(dist * r / 2)

    # DISPLAYING TEXT AROUND CIRCLES -----------------------------------------------------
    turtle.home()
    turtle.forward(total_center)
    turtle.right(90)
    turtle.forward(total_center)
    turtle.left(90)
    turtle.color('black')

    for leftright in (text_right_world, text_left_good):
        drawdef.color_by_limits(side_values, value_max, value_minTrue)
        turtle.forward(LR_dist)
        turtle.write(leftright, font=('Arial', 12, 'normal'), align='center')
        turtle.back(LR_dist)
        turtle.left(180)

    turtle.left(90)

    for updown in (text_up_love, text_down_money):
        drawdef.color_by_limits(side_values, value_max, value_minTrue)
        turtle.forward(UD_dist)
        turtle.write(updown, font=('Arial', 12, 'normal'), align='center')
        turtle.back(UD_dist)
        turtle.left(180)

    # DISPLAYING FINAL TEXT -------------------------------------------------------------
    # Name and date (upper-left corner).
    turtle.home()
    turtle.color('black')
    turtle.left(145)
    turtle.forward(450)
    turtle.write(text_name, font=('Arial', 20, 'bold'), align='center')
    turtle.right(145)
    turtle.right(90)
    turtle.forward(50)
    turtle.write(your_name, font=('Arial', 20, 'bold'), align='center')
    turtle.forward(50)
    turtle.write(test_date, font=('Arial', 20, 'bold'), align='center')

    # Conclusion and advice (lower-right corner).
    turtle.home()
    turtle.color('black')
    turtle.left(143)
    turtle.back(500)
    turtle.write(drawdef.max_line_length(text_final, 70), font=('Arial', 8, 'bold'), align='center')

    turtle.exitonclick()


# Run the function for testing purposes if this file is executed directly.
if __name__ == '__main__':
    ikigai_draw(5, 5, 2, 7, 10, 5, 
                'text_conclusion', 'text_advice', 'your_name', 'test_date')
