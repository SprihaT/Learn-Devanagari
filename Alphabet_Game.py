#----import-----
import turtle as trtl
from random import randint
import random

#----background setup-----
pear_image = "pear.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("startbg.png")

#introduction
start = input(
    "Welcome to Learn Devanagari, the game designed to teach the hindi alaphabet! Press enter to start. "
)

wn.bgpic("background.png")
wn.addshape(pear_image)

#-----Organizing Letters-----

#dicitonary collection type used to manage complexity
letters = {
    'a': 'अlike the "u" in uh',
    'aa': 'आlike the "a" in father',
    'i': 'इlike the "i" in sit',
    'ii': 'ईlike the "ee" in beep',
    'u': 'उlike the "oo" in book',
    'oo': 'ऊlike the "oo" in moon',
    'ri': 'ॠlike the "r"" in rabbit',
    'e': 'एlike the "ay" in say',
    'ai': 'ऐlike the "e" in pen',
    'o': 'ओlike the "o" in so',
    'au': 'औlike the "aw" in saw',
    'ka': 'कlike the "c" in scab',
    'kha': 'खlike the "c" in cat',
    'ga': 'गlike the "g" in good',
    'gha': 'घlike the "gh" in loghouse',
    'gna': 'ङlike the "ng" in bang',
    'cha': 'चlike the "ch" in match',
    'chha': 'छlike the "ch" in achoo',
    'ja': 'जlike the "j" in jungle',
    'jha': 'झlike the "dgeh" in hedgehog',
    'ta': 'टlike the "t" in stab',
    'thh': 'ठlike the "t" in tub',
    'da': 'डlike the "d" in bird',
    'dh': 'ढlike the "dh" in birdhouse',
    'n': 'णlike the "n" in burn',
    't': 'तlike the "th" in outthink',
    'tha': 'थlike the "th" in thorn',
    'd': 'दlike the "d" in width',
    'dha': 'धlike the "dh" in adhere',
    'na': 'नlike the "n" in panther',
    'pa': 'पlike the "p" in spot',
    'pha': 'फlike the "p" in pot',
    'ba': 'बlike the "bb" in cabbage',
    'bha': 'भlike the "bh" in clubhouse',
    'ma': 'मlike the "m" in matrix',
    'ya': 'यlike the "y" in yum',
    'ra': 'रlike the "r" in rude',
    'la': 'लlike the "l" in luck',
    'va': 'वlike the "v" in van',
    'ha': 'हlike the "h" in horn',
    'sha': 'शlike the "sh" in shellfish',
    'shha': 'षlike the "sh" in shoe',
    'sa': 'सlike the "s" in salty',
}

key_list = []
for key in letters.keys():
  key_list.append(key)

for key in key_list:
  alphabet = letters[key][0]
  wn.addshape(f'{alphabet}.gif')

pear_list = []
chosen_sounds = []


#-----turtle creating function-----
def draw_pears(num_pears, x):
  for pear in range(num_pears):
    active_pear = trtl.Turtle()
    try:
        active_sound = key_list.pop(randint(0, len(key_list) - 1))
        pear_list.append(active_pear)
        active_pear.pu()
        active_pear.sety(75)
        active_pear.setx(x)
        active_pear.shape(pear_image)
        wn.tracer(False)
        active_pear.sety(active_pear.ycor() - 30)
        active_pear.color("white")
        active_pear.write(active_sound, align='center', font=("Arial", 30, "bold"))
        chosen_sounds.append(active_sound)
        active_pear.sety(active_pear.ycor() + 30)
        wn.tracer(True)
        wn.update()
    except ValueError:
      active_pear.ht()
    x += 120

#-----turtles setup-----
draw_pears(5, -280)

letter_display = trtl.Turtle()
letter_display.pu()
letter_display.goto(-10, -200)
question = trtl.Turtle()
question.ht()
question.color('white')
question.pu()
question.goto(-275, -150)
pronunciation = trtl.Turtle()
pronunciation.pu()
pronunciation.ht()
pronunciation.color('white')
pronunciation.goto(-275, -100)

#-----game loop-----
while True:
  try:
    #proceed if there are letters available
    ask_sound = random.choice(chosen_sounds)
    ask_letter = letters[ask_sound][0]
    pause = True
    question.write("Press on the sound that is made by the Hindi letter:",
                   font=("Arial", 15, "bold"))
    letter_display.shape(str(ask_letter) + ".gif")

    correct_pear = pear_list[chosen_sounds.index(ask_sound)]

    def drop_pear(x, y):
      correct_pear.penup()
      correct_pear.clear()
      correct_pear.sety(-125)
      correct_pear.hideturtle()
      pear_list.pop(pear_list.index(correct_pear))
      draw_pears(1, int(correct_pear.xcor()))
      global pause
      pause = False

    while pause:
      correct_pear.onclick(drop_pear)
    pronunciation.clear()
    pronounce = letters[ask_sound][1:]
    pronunciation.write(
        f"Correct! The pronunciation was {pronounce}",
        font=("Arial", 15, "bold"),
    )
    chosen_sounds.pop(chosen_sounds.index(ask_sound))
  except IndexError:
    #end game if there are no letters available
    print("\nCongratulations! You completed the game!")
    question.clear()
    pronunciation.clear()
    letter_display.ht()
    wn.bgpic('endbg.png')
    break
wn.mainloop()
wn.listen()
