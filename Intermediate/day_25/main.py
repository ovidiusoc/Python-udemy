import turtle
import pandas


list_answers = []
x_cor = 0
y_cor = 0
screen = turtle.Screen()
screen.title("US States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

while len(list_answers) < 50:
    answer_state = screen.textinput(title=f"{len(list_answers)}/50 guessed", prompt="What's another state's name")
    guess = answer_state.title()
    all_states = data.state.to_list()
    if guess == 'Exit':
        break
    if guess in all_states:
        list_answers.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(guess)

# removing the states that where guessed
res = [i for i in all_states if i not in list_answers]

states_to_learn = {"state": res}

df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")


# screen.exitonclick()
# def get_louse_click_cor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_louse_click_cor)
# turtle.mainloop()


