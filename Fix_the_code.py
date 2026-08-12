import time

try:
    import shelve

    storage = shelve.open("local_storage")
    username = storage.get("username", "")
    on_skulpt = False
except Exception:
    username = ""
    on_skulpt = True
    print("(parece que no puedes usar la libreria shelve y/o estas en skulpt)")
    time.sleep(1)


def wait(seconds):
    time.sleep(seconds)
code_works = "ok, vamos configurando el trazo"

def validate_command(broken_code, correct_command1, correct_command2=""):
    user_code = input('"' + broken_code + '"         DEV: pon el codigo bien escrito en el input que puse, este no me funciona')
    print("hmm...")
    wait(2)

    if correct_command2 == "":
        if user_code == correct_command1:
            print(code_works)
            return True
    else:
        if user_code == correct_command1 or user_code == correct_command2:
            print(code_works)
            return True

    print("DEV: hmm, parece que escribiste algo mal, yo creo que debes cerrar y abrir el programa para reiniciarlo")

print("𝓗𝓸𝓵𝓪 DIBUJANTE, 𝓫𝓲𝓮𝓷𝓿𝓮𝓷𝓲𝓭𝓸 𝓪𝓵 𝓳𝓾𝓮𝓰𝓸")
wait(2)
print("cargando...[librerias, codigo y fuentes]")
wait(2)
print("librerias... HECHO")
wait(1)
print("codigo... ")
wait(4)
print("DEV: emm")
wait(1)
print("DEV: porq no carga? XD")
wait(1)
print("Reintentando carga...")
wait(2)
print("Cargando codigo... (reintento #1)")
wait(3)
print("Cargando codigo... (reintento #2)")
wait(5)
print("ERROR: bad input in ALL CODE")
wait(2)
print("DEV: Recorcholis, no sabia que mi codigo estaba tan mal")
wait(1)
print("DEV: me ayudas a arreglarlo? :V")
wait(2)
print("(si)")
wait(2)

if username == "":
    print("DEV: Gracias, dime tu nombre para que comencemos!")
    username = input()
    if not on_skulpt:
        storage["username"] = username
        print("(Ya dijiste que es ", username, ")")
    
    print('DEV: tu nombre es "', username, '" ?')
    if username == "":
        print("DEV: hmm, te llamare aventurero anonimo")
        username = "Aventurero Anonimo"
        print("DEV: listo?")
    wait(2)
    print("(si)")
    print("DEV: Gracias", username, "!")
else:
        print("...")
        wait(1)
        print("DEV: ¿Como es que aparece que ya te pregunte tu nombre?")
        wait(1)
        print("DEV: Ohh verdad que tu eres", username,", se me olvido por un momento, no terminaron de cargar las librerias por todos los typos")

if not on_skulpt:
    storage.close()

wait(0.5)
print()
wait(1)

import turtle
t = turtle.Turtle()

validate_command("t.fil('1')", "t.fill(1)")
t.fill(1)
validate_command("t.colorlapiz('green')", "t.pencolor('green')", 't.pencolor("green")')
t.color("#00ff00")
t.pencolor("green")
wait(2)
code_works = "buen trabajo, ya vas dibujando el cre- ah verdad que no debo spoilear"
validate_command("t.walk(160)", "t.forward(160)", "t.fd(160)")
t.forward(160)
wait(2)
validate_command("t.lefet(90)", "t.left(90)", "t.lt(90)")
t.left(90)
wait(2)
print("Vas bien,", username, ", no lo niego")
wait(2)
validate_command("t.move(160)", "t.forward(160)", "t.fd(160)")
t.forward(160)
wait(2)
validate_command("t.lefet(90)", "t.left(90)", "t.lt(90)")
t.left(90)
wait(2)
validate_command("t.f0rward(160)", "t.forward(160)", "t.fd(160)")
t.forward(160)
wait(2)
validate_command("t.lefet(90)", "t.left(90)", "t.lt(90)")
t.left(90)
wait(2)
validate_command("t.walk(160)", "t.forward(160)", "t.fd(160)")
t.forward(160)
wait(2)
print("DEV: Hmm, eso seria el contorno")
wait(3)
print("DEV: vere si ahora si carga")
wait(1)
print("Reintentando carga...")
wait(2)
print("Cargando codigo... (reintento #3)")
wait(2)
print("Codigo... HECHO")
wait(2)
print("Fuentes... HECHO")
wait(3)
print("𝓓𝓲𝓫𝓾𝓳𝓪𝓷𝓭𝓸 𝓒𝓡𝓔𝓔𝓟𝓔𝓡...")
wait(2)
t.speed(0)
t.fill(0)
t.up()
t.goto(20, 140)
t.down()
t.color("black")
t.begin_fill()
t.fd(40)
t.rt(90)
t.fd(40)
t.rt(90)
t.fd(40)
t.rt(90)
t.fd(40)
t.rt(90)
t.end_fill()
t.up()
t.fd(80)
t.down()
t.begin_fill()
t.fd(40)
t.rt(90)
t.fd(40)
t.rt(90)
t.fd(40)
t.rt(90)
t.fd(40)
t.rt(90)
t.end_fill()
t.rt(90)
t.fd(40)
t.begin_fill()
t.fd(20)
t.lt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(20)
t.lt(90)
t.fd(40)
t.lt(90)
t.fd(20)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.rt(90)
t.fd(20)
t.lt(90)
t.fd(20)
t.rt(90)
t.fd(40)
t.rt(90)
t.end_fill()
t.hideturtle()
t.goto(0, -20)
t.write("BIEN HECHO,", username, "!")
