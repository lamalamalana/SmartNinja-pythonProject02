#   flask je knjižnica za čim bolj enostavno ustvarjanje spletne strani
#   ima svoje zakonitosti
#   vse kar bomo naredli s flaskom bi lahko naredli tud s pure python, ampak bi blo velik dela
#   za instalirat flask rabimo pip - potem bomo to tud na strežniku rabli, zato to dodamo v file "requirements.txt"
#   v requirements bi dali tud druge knjižnice ki bi jih rabli

#  to spodaj je zelo simpl program
import flask
from flask import Flask #   iz knjižnice flask importamo class Flask

app = Flask(__name__)   #   naredi se objekt iz classa Flask in se mu da ime "app" - na ta standardni način naredimo aplikcaijo za flask


@app.route("/") #   @ je dekorator, nismo tega jemali - ampak tu definiramo, da je osnovna stran vedno "/" ( = to je vedno index page oz homepage)
def index():    #   funkcija index(), ki vrne spodnji string
#   return "Pozdravljen svet!"
#    --> tole zgori smo uporabli za inicialni primer, potem smo rekli, da za spletne strani seveda vračamo html ipd
    return flask.render_template('index.html', heading="Pozdravljen svet!")
#   če bi napisali samo render_template('index.html') kaže samo statičen HTML, flask ne rabiš za statičen page
#   flask uporabiš za dinamično vsebino (inputi itd)
#   zato recimo dodaš parameter body (to je samo ime spremenljivke, pol smo spremenili v heading) in to spremenljivko izpišemo v HTML v dvojne zavite oklepaje - zadeve postanejo povezane

#   kakršnkoli program bi v tem indexu napisali, bi se zagnal v localhostu
#   - podobno kot smo prej gledali v konzolo, lahko to gledamo zdaj v browserju

#   če hočemo novo podstran:

@app.route("/stetje")
def stetje():
    out = ''
    for i in range(10):
        out += str(i) + '<br/>'
    return out

if __name__ == "__main__":  #če ta fajl poganjamo kot glavni fajl, naj se aplikacija zažene v direktni
    app.run()

#   na tej točki smo dali run in vrže ven na koncu Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
#   http://127.0.0.1 je naš računalnik in 5000 je port
#   to zalaufa http strežnik na našem kompu

#   MVC - model view controller
#   logiko programske kode razdelimo na tri dele - model, view in controller
#   logika je, da imamo v vsakem od teh delov ustrezno logiko tistemu delu
#   model = reprezentacija naših podatkov
#   preko model bomo imeli nek class, kjer bomo prikazovali podatke, kako jih bomo shranjevali v bazo in jih iz baze brali
#   view = prikazovanje spletne strani
#   v viewu se bo skrbelo za to, da se HTMLji sestavijo v neko celoto in se pošljejo nazaj uporabniku
#   controller = vezni člen med model in view
#   je osrednji del, kamor letijo naši requesti
#   to, kar smo tu naredli je v bistvu naš controller, requesti letijo sem
#   nekateri delajo controller tud kr v modelu

#   kako deluje view? view naredimo v isti direktorij kot main.py, requirements.txt mora tud bit tam
#   narediš nov direktorij v tem root folder kjer smo zdej, in se imenuje templates (glej trenutno strukturo)

#   za shranjevanje statičnih fajlov ki jih bomo uporabljali v projektu naredimo še en direktorij "static"
#   to so običajno slike, CSS fajli ...
