import time

try:
    import shelve

    storage = shelve.open("local_storage")
    username = storage.get("username", "")
    on_skulpt = False
    print()
except Exception:
    username = ""
    on_skulpt = True
    print("(parece que no puedes usar la libreria shelve y/o estas en skulpt)")
    time.sleep(1)


def wait(seconds):
    time.sleep(seconds)
code_works = "ok, vamos configurando el trazo"

def validate_command(broken_code, correct_command1, correct_command2=""):
    print()
    user_code = input(
        '"'
        + broken_code
        + '"         #pon el codigo bien escrito en el input que puse, este no me funciona'
    )
    print("hmm...")
    time.sleep(2)

    if correct_command2 == "":
        if user_code == correct_command1:
            print(code_works)
            return True
    else:
        if user_code == correct_command1 or user_code == correct_command2:
            print(code_works)
            return True

    print(
        "hmm, parece que escribiste algo mal, yo creo que debes cerrar y abrir el programa para reiniciarlo"
    )
    raise SystemExit

print("𝓗𝓸𝓵𝓪 𝓐𝓥𝓔𝓝𝓣𝓤𝓡𝓔𝓡𝓞, 𝓫𝓲𝓮𝓷𝓿𝓮𝓷𝓲𝓭𝓸 𝓪𝓵 𝓳𝓾𝓮𝓰𝓸")
wait(2)
print("cargando...[librerias, codigo y fuentes]")
wait(2)
print("librerias... HECHO")
wait(1)
print("codigo... ")
wait(4)
print("emm")
wait(1)
print("porq no carga? XD")
wait(1)
print("Reintentando carga...")
wait(2)
print("Cargando codigo... (reintento #1)")
wait(3)
print("Cargando codigo... (reintento #2)")
wait(5)
print("ERROR: bad input in ALL CODE")
wait(2)
print("Recorcholis, no sabia que mi codigo estaba tan mal")
wait(1)
print("me ayudas a arreglarlo? :V")
wait(2)
print("(si)")
wait(2)

if username == "":
    print("Gracias, dime tu nombre para que comencemos!")
    username = input()
    if not on_skulpt:
        storage["username"] = username
        print("(Ya dijiste que es ", username, ")")
    
    print("tu nombre es ", username, "?")
    if username == "":
        print("hmm, te llamare aventurero anonimo")
        username = "Aventurero Anonimo"
        print("listo?")
    wait(2)
    print("(si)")
    print("Gracias", username, "!")
else:
    print("...")
    wait(1)
    print("¿Como es que aparece que ya te pregunte tu nombre?")
    wait(1)
    print(
        "Ohh verdad que tu eres",
        username,
        ", se me olvido por un momento, no terminaban de cargar las librerias",
    )

if not on_skulpt:
    storage.close()

wait(0.5)
print()
wait(1)

import turtle

t = turtle.Turtle()


validate_command("t.fil('1')", "t.fill(1)")
t.fill(1)
validate_command(
    "t.colorlapiz('green')", "t.pencolor('green')", 't.pencolor("green")'
)
t.pencolor("green")
wait(2)
code_works = "buen trabajo, ya vas dibujando el cre- ah verdad que no debo spoilear"
validate_command("t.forward", "t.forward(100)", "t.fd(100)")
t.forward(100)
wait(2)
validate_command("t.lefet(90)", "t.left(90)", "t.lt(90)")
t.left(90)
wait(2)
print("Vas bien,", username, ", no lo niego")
wait(2)
validate_command("t.forward", "t.forward(100)", "t.fd(100)")
t.forward(100)
wait(2)
validate_command("t.lefet(90)", "t.left(90)", "t.lt(90)")
t.left(90)
wait(2)
validate_command("t.forward", "t.forward(100)", "t.fd(100)")
t.forward(100)
wait(2)
validate_command("t.lefet(90)", "t.left(90)", "t.lt(90)")
t.left(90)
wait(2)
validate_command("t.forward", "t.forward(100)", "t.fd(100)")
t.forward(100)
wait(2)

print("[SISTEMA]: Contorno de la cabeza completado con éxito.")
