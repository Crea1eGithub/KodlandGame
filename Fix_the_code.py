import time
import sys
import turtle
t = turtle.Turtle()

failed = False
try:
    import shelve

    storage = shelve.open("local_storage")
    username = storage.get("username", "")
    on_skulpt = False
except Exception:
    username = ""
    on_skulpt = True
    print("(parece que no puedes usar la libreria shelve y/o estas en skulpt)")
    print("(skelpt es el entorno web que kodland usa para correr en navegador)")
    time.sleep(1)


def wait(seconds):
    time.sleep(seconds)
code_works = "ok, vamos configurando el trazo"

def validate_command(wrong, right1, right2):
    global failed
    print(wrong + "<- Escribe la forma correcta")
    user_code = input("Aqui ->").strip()
    if user_code == right1 or user_code == right2:
        print(code_works)
        return True
    else: 
        
        print("DEV: Uhh")
        wait(1)
        print("DEV: Eso no funciono")
        wait(2)
        print("DEV: creo que tienes que reiniciar el programa")
        wait(2)
        try:
            sys.exit()
        except:
            while True:
                pass

print("𝓗𝓸𝓵𝓪 DIBUJANTE, 𝓫𝓲𝓮𝓷𝓿𝓮𝓷𝓲𝓭𝓸 𝓪𝓵 𝓳𝓾𝓮𝓰𝓸")
wait(2)
print("cargando...[librerias, codigo y fuentes]")
wait(2)
print("librerias... HECHO")
wait(1)
print("codigo...  ERROR")
wait(3)
print("DEV: emm")
wait(1)
print("DEV: porq no carga? XD")
wait(1)
print("Reintentando carga...")
wait(1)
print("Cargando codigo... (reintento #1)")
wait(2)
print("Cargando codigo... (reintento #2)")
wait(2)
print("ERROR: bad input in ALL CODE")
wait(1.5)
print("DEV: Recorcholis, no sabia que mi codigo estaba tan mal")
wait(1)
print("DEV: me ayudas a arreglarlo? :V")
wait(2)
print("(si)")
wait(2)

if username == "":
    print("DEV: Gracias, dime tu nombre para que comencemos!")
    wait(0.5)
    
    # Forzamos un print para “despertar” el input de Kodland
    print("(escribe tu nombre y dale Enter)")
    wait(0.3)
    
    username = input()
    
    if username == "":
        print("DEV: hmm, te llamare aventurero anonimo")
        username = "Aventurero Anonimo"
        wait(1)
        print("DEV: listo?")
    
    if not on_skulpt:
        storage["username"] = username
        print("(Ya dijiste que es ", username, ")")
  
    print('DEV: tu nombre es "', username, '" ?')
   
    if username == "INeedAnswerSheet":
        print("Respuestas #1: t.begin_fill() , t.fill(1)")
        print("Respuestas #2: t.fillcolor('green') ," + 't.fillcolor("green")')
        print("Respuestas #3, 5, 7 y 9: t.fd(160), t.forward(160)")
        print("Respuestas #4, 6 y 8: t.lt(90), t.left(90)")
        wait(2)
        print("DEV: si te equivocas en serio no se que hacer")
        wait(1)
        print("DEV: Listo?")
        username = "TontoDePython"
   
    wait(2)
    print("(si)")
    wait(2)
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
print("(El programa crashea si te equivocas)")
print("")

validate_command("t.beginfil('1')", "t.begin_fill()", "t.fill(1)")
t.begin_fill()
validate_command("t.colorelleno('green')", "t.fillcolor('green')", 't.fillcolor("green")')
t.fillcolor("green")
wait(2)
code_works = "DEV: buen trabajo, ya vas dibujando el cre- ah verdad que no debo spoilear"
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
t.end_fill()
t.up()
t.goto(20, 140)
t.down()
t.color("black")
t.begin_fill()
t.fd(40); t.rt(90); t.fd(40); t.rt(90); t.fd(40); t.rt(90); t.fd(40); t.rt(90)
t.end_fill()
t.up(); t.fd(80); t.down()
t.begin_fill()
t.fd(40); t.rt(90); t.fd(40); t.rt(90); t.fd(40); t.rt(90); t.fd(40); t.rt(90)
t.end_fill()
t.rt(90); t.fd(40)
t.begin_fill()
t.fd(20); t.lt(90); t.fd(20); t.rt(90); t.fd(60); t.rt(90); t.fd(20); t.rt(90)
t.fd(20); t.lt(90); t.fd(40); t.lt(90); t.fd(20); t.rt(90); t.fd(20); t.rt(90)
t.fd(60); t.rt(90); t.fd(20); t.lt(90); t.fd(20); t.rt(90); t.fd(40); t.rt(90)
t.end_fill()
print("DEV: Chau! :D")
wait(600)
print("Aguanta, sigues aca despues de 10 minutos?")
wait(1.5)
print("Vete, esta es la ultima linea del programa")
wait(120)
print("No te dije que te vayas?")
wait(1.5)
print("BIEN, YO MISMO CRASHEARE ESTO")
wait(5)
try:
    sys.exit()
except:
    while True:
        pass
