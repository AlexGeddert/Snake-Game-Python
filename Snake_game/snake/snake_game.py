'''
Projektarbeit "Snake" Karl T. und Alex G.
Created on 02.03.2020

@author: Student
'''

import turtle   # Bildbeschreibungssprache
import time     # für den delay 
import random   # Zufallsgenerator für das Essen

delay = 0.1     # Zeitverzögerung

# Punktestand
score = 0
high_score = 0

# Spielfenster erstellen

wn = turtle.Screen() #wn = window
wn.title("Snake Game by Karl und Alex") # Titel d. Spiels
wn.bgcolor("lightblue") # Hintergrundfarbe    
wn.setup(width=800, height=600) # Höhe / Breite
wn.tracer(0) # verhindert Bildupdates

# Snake "Kopf"
head = turtle.Turtle()
head.speed(0) # 0 = schnellstmögliche Animationsgeschwindigkeit
head.shape("square") # Form, auch möglich sind: classic, arrow, turtle, circle oder triangle
head.color("green") # Farbe
head.penup() # turtle import "hebt den Stift an"
head.goto(0,0) # in der Mitte beginnen
head.direction = "stop" # keine Anfangsrichtung

# nom nom nom
food = turtle.Turtle()
food.speed(0) 
food.shape("turtle") 
food.color("red") 
food.penup() 
food.goto(0,100) 

segments = []

# Punkteanzeige (Python spezifisch mit "pen")
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle() # Verstecke "turtle" ???
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 18, "normal"))

# Funktionen
def go_up():
    if head.direction != "down": # Bewege dich nicht entgegengesetzt
        head.direction ="up"
    
def go_down():
    if head.direction != "up":
        head.direction ="down"
    
def go_left():
    if head.direction != "right":
        head.direction ="left"
    
def go_right():
    if head.direction != "left":
        head.direction ="right"

def move():
    if head.direction == "up":  # Wenn "aufwärts"
        y = head.ycor()         # --> dann y + 20
        head.sety(y + 20)
        
    if head.direction == "down": # Wenn "abwärts"
        y = head.ycor()              # --> dann y - 20
        head.sety(y - 20)
        
    if head.direction == "left":   # Wenn "links"
        x = head.xcor()              # --> dann x - 20
        head.setx(x - 20)
        
    if head.direction == "right": # Wenn "rechts"
        x = head.xcor()         # --> dann x + 20
        head.setx(x + 20)

# Tastenbelegung
wn.listen()
wn.onkeypress(go_up, "w") # Pfeiltasten = "Up"
wn.onkeypress(go_down, "s") # Pfeiltasten = "Down"
wn.onkeypress(go_left, "a") # Pfeiltasten = "Left"
wn.onkeypress(go_right, "d") # Pfeiltasten = "Right"

# Hauptspielschleife
while True:
    wn.update()

    # Kollisionsabfrage mit dem Rand
    if head.xcor()>380 or head.xcor()<-380 or head.ycor()>280 or head.ycor()<-280: # Wenn Kopf außerhalb vom Rand
        time.sleep(1)   # dann friere ein für eine Sekunde
        head.goto(0,0)  # bewege dich zur Ausgangsposition
        head.direction = "stop"  # verwerfe die Richtung
        
    # Verwerfe die Segmente nach Kollision
        for segment in segments:
            segment.goto(1000, 1000) # Segmente werden außerhalb des Bildes verschoben da sie in Python nicht gelöscht werden können
        
    # Verwerfe die Segmentliste
        segments.clear()         # erst ab Python 3 möglich (clear)

    # Zurücksetzen des Punktestandes wenn man verliert
        score = 0
        
    # Setze die Verzögerung zurück
        delay = 0.1
        
        pen.clear() 
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))
        
    # Kollisionsabfrage mit dem Essen
    if head.distance(food) < 20: # wenn kopf mit essen kollidiert
        x = random.randrange(-380, 380, 20) 
        y = random.randrange(-280, 280, 20)
        food.goto(x, y) # bewege "nom nom nom" an eine zufällige Stelle

        # Körperteil hinzufügen
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("purple")
        new_segment.penup()
        segments.append(new_segment) 

    # verkürze die "Verzögerung" sobald man Essen einsammelt
        delay -= 0.001

    # Punktzahl erhöhen
        score += 10
        
        if score > high_score:
            high_score = score
            
        pen.clear() # lösche alten Punktestand sobald sich die Punkte erhöhen
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))

    # bewege die Endsegmente zuerst, in umgekehrter Reihenfolge
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # bewege Segment "0" dahin wo der Kopf ist
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        
    move()
    
    # Kollisionsabfrage mit den Körpersegmenten
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
    # Verwerfe die Segmente nach Kollision
            for segment in segments:
                segment.goto(1000, 1000)
            
    # Verwerfe die Segmentliste
            segments.clear()
    
    # Zurücksetzen des Punktestandes wenn man mit sich selbst kollidiert
            score = 0
        
    # Setze die Verzögerung zurück
            delay = 0.1
        
            pen.clear() 
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "normal"))
    
    time.sleep(delay) # verlangsamt die Zeit um den "delay"


wn.mainloop() # verhindert Schließen des Fensters

