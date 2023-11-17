import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_snowflake(t, order - 1, size)
        t.left(60)
        koch_snowflake(t, order - 1, size)
        t.right(120)
        koch_snowflake(t, order - 1, size)
        t.left(60)
        koch_snowflake(t, order - 1, size)

def koch_snowflake_flake(t, order, size):
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

def main():
    order = int(input("Кол-во подобий: "))
    size = 300
    window = turtle.Screen()
    window.bgcolor("white")

    snowflake = turtle.Turtle()
    snowflake.speed(1000) # скорость 
    # goto - переместить на x,y
    snowflake.penup();snowflake.goto(-150, 90);snowflake.pendown()
    snowflake.hideturtle() # скрыть стрелочку 


    koch_snowflake_flake(snowflake, order, size)

    window.exitonclick()

if __name__ == "__main__":
    main()