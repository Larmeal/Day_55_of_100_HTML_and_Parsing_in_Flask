from flask import Flask
import random

random_ = random.randint(0, 9)
print(random_)

app = Flask(__name__)

@app.route("/")
def guess():
    return "<h1> Guess a number between 0 and 9 </h1>"\
        "<img src=https://media1.giphy.com/media/5zoxhCaYbdVHoJkmpf/giphy.gif?cid=ecf05e47fehg0rmds79i3duxier345spp9rga8vl1b36dxgn&rid=giphy.gif&ct=g>"


@app.route("/<int:random_number>")
def correct_number(random_number):
    if random_number < random_:
        return "<h1> Too low!, try again </h1>"\
            "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"

    elif random_number > random_:
        return "<h1> Too high!, try again </h1>"\
            "<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    
    elif random_number == random_:
        return "<h1> You found me!</h1>"\
            "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"





if __name__ == "__main__":
    app.run(debug=True)

