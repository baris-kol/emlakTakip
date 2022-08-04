from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Barış/Desktop/Emlak Takip/emlak.db'
db = SQLAlchemy(app)

class Konut(db.Model):
    __tablename__ = 'konut'
    __table_args__ = {'sqlite_autoincrement': True}
    konutId = db.Column(db.Integer, primary_key=True)
    konutBaslik = db.Column(db.String(100), unique=True, nullable=False)
    konutDurum = db.Column(db.String(50), nullable=False)
    konutAdres = db.Column(db.String(200), nullable = False)
    konutOdaSayisi = db.Column(db.String(50), nullable = False)
    konutBanyoSayisi = db.Column(db.Integer, nullable = True)
    konutIsınmaTipi = db.Column(db.String(50), nullable = True)
    konutMetreKare = db.Column(db.Integer, nullable = False)
    konutYasi = db.Column(db.Integer, nullable = True)
    konutKatSayisi = db.Column(db.Integer, nullable = True)
    konutBulunduguKat = db.Column(db.Integer, nullable = True)
    konutAidat = db.Column(db.String(50), nullable = True)
    konutFiyat = db.Column(db.String(50), nullable = False)

class Arsa(db.Model):
    __tablename__ = 'arsa'
    __table_args__ = {'sqlite_autoincrement': True}
    arsaId = db.Column(db.Integer, primary_key=True)
    arsaBaslik = db.Column(db.String(100), unique=True, nullable=False)
    arsaDurum = db.Column(db.String(50), nullable=False)
    arsaAdres = db.Column(db.String(200), nullable = False)
    arsaImarDurum = db.Column(db.String(50), nullable = False)
    arsaMetreKare = db.Column(db.Integer, nullable = False)
    arsaTapuDurum = db.Column(db.String(50), nullable = True)
    arsaKaks = db.Column(db.Integer, nullable = False)
    arsaGabari = db.Column(db.Integer, nullable = False)
    arsaFiyat = db.Column(db.String(50), nullable = False)

class isYeri(db.Model):
    __tablename__ = 'isyeri'
    __table_args__ = {'sqlite_autoincrement': True}
    isyeriId = db.Column(db.Integer, primary_key=True)
    isyeriBaslik = db.Column(db.String(100), unique=True, nullable=False)
    isyeriDurum = db.Column(db.String(50), nullable=False)
    isyeriAdres = db.Column(db.String(200), nullable = False)
    isyeriTuru = db.Column(db.String(50), nullable = True)
    isyeriMetreKare = db.Column(db.Integer, nullable = False)
    isyeriBolumVeOdaSayisi = db.Column(db.Integer, nullable = True)
    isyeriAidat = db.Column(db.String(50), nullable = False)
    isyeriIsitma = db.Column(db.String(50), nullable = True)
    isyeriBinaYasi = db.Column(db.Integer,nullable = False)
    isyeriFiyat = db.Column(db.String(50), nullable = False)

@app.route("/")
def index():
    return render_template("index.html")
#deneme
@app.route("/eklemeAlani",methods =['GET','POST'])
def eklemeAlani():
    value = request.form.get("selectedData")
    return render_template("eklemeAlani.html", values = str(value))

@app.route("/listelenmis",methods = ['GET','POST'])
def listelenmis():
    value = request.form.get("selectedList")  
    
    if(value == "Konut"):
        konutlar = Konut.query.all()
        return render_template("index.html",konutList = konutlar, value = value)
    elif(value == "Arsa"):
        arsalar = Arsa.query.all()
        return render_template("index.html",arsaList = arsalar,value = value)
    elif(value == "isYeri"):
        isYerleri = isYeri.query.all()
        return render_template("index.html", isYeriList = isYerleri,value = value)
    
@app.route("/addKonut", methods = ['POST'])
def konutEkle():
    konutBaslik = request.form.get("konutBaslik")
    konutDurum = request.form.get("konutDurum")
    konutAdres = request.form.get("konutAdres")
    isinmaTipi = request.form.get("isinmaTipi")
    konutOdaSayisi = request.form.get("konutOdaSayisi")
    konutBanyoSayisi = request.form.get("konutBanyoSayisi")
    konutMetreKare = request.form.get("konutMetreKare")
    konutBinaYasi = request.form.get("konutBinaYasi")
    konutKatSayisi = request.form.get("konutKatSayisi")
    konutBulunduguKat = request.form.get("konutBulunduguKat")
    konutAidat = request.form.get("konutAidat")
    konutFiyat = request.form.get("konutFiyati")

    yeniKonutKayit = Konut(konutBaslik = konutBaslik,konutDurum = konutDurum,konutAdres = konutAdres,konutOdaSayisi=konutOdaSayisi,konutBanyoSayisi = konutBanyoSayisi,konutIsınmaTipi = isinmaTipi,konutMetreKare = konutMetreKare,konutYasi = konutBinaYasi,konutKatSayisi = konutKatSayisi,konutBulunduguKat = konutBulunduguKat,konutAidat = konutAidat,konutFiyat = konutFiyat)

    db.session.add(yeniKonutKayit)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/addArsa", methods =['POST'])
def arsaEkle():
    arsaBaslik = request.form.get("arsaBaslik")
    arsaDurum = request.form.get("arsaDurum")
    arsaAdres = request.form.get("arsaAdres")
    arsaImarDurum = request.form.get("arsaImarDurum")
    arsaMetreKare = request.form.get("arsaMetreKare")
    arsaTapuDurum = request.form.get("arsaTapuDurum")
    arsaKaks = request.form.get("arsaKaks")
    arsaGabari = request.form.get("arsaGabari")
    arsaFiyat = request.form.get("arsaFiyat")

    yeniArsaKayit = Arsa(arsaBaslik = arsaBaslik, arsaDurum = arsaDurum, arsaAdres = arsaAdres, arsaImarDurum = arsaImarDurum, arsaMetreKare = arsaMetreKare, arsaTapuDurum = arsaTapuDurum, arsaKaks = arsaKaks, arsaGabari = arsaGabari, arsaFiyat = arsaFiyat)

    db.session.add(yeniArsaKayit)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/addIsYeri", methods = ['POST'])
def isYeriEkle():
    isYeriBaslik = request.form.get("isYeriBaslik")
    isYeriDurum = request.form.get("isYeriDurum")
    isYeriAdres = request.form.get("isYeriAdres")
    isYeriTuru = request.form.get("isYeriTuru")
    isYeriMetreKare = request.form.get("isYeriMetreKare")
    isYeriBolumVeOda = request.form.get("isYeriBolumVeOda")
    isYeriIsınma = request.form.get("isYeriIsınma")
    isYeriBinaYasi = request.form.get("isYeriBinaYasi")
    isYeriAidat = request.form.get("isYeriAidat")
    isYeriFiyati = request.form.get("isYeriFiyati")
    yeniIsYeriKayit = isYeri(isyeriBaslik = isYeriBaslik,isyeriDurum = isYeriDurum, isyeriAdres = isYeriAdres, isyeriTuru = isYeriTuru, isyeriMetreKare = isYeriMetreKare, isyeriBolumVeOdaSayisi = isYeriBolumVeOda, isyeriAidat = isYeriAidat, isyeriIsitma = isYeriIsınma, isyeriBinaYasi = isYeriBinaYasi, isyeriFiyat = isYeriFiyati)

    db.session.add(yeniIsYeriKayit)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/updateKonut/<string:id>")
def updateKonutData(id):
    value = "Konut"
    konutData = Konut.query.filter_by(konutId = id).first()
    if(konutData.konutDurum == "Satılık"):
        konutData.konutDurum = "Satıldı"
    elif(konutData.konutDurum == "Satıldı"):
        konutData.konutDurum = "Satılık"
    elif(konutData.konutDurum == "Kiralık"):
        konutData.konutDurum = "Kiralandı"
    elif(konutData.konutDurum == "Kiralandı"):
        konutData.konutDurum = "Kiralık"
    print("Kiralama/Satılma Durumu")
    db.session.commit()
    konutlar = Konut.query.all()
    return render_template("index.html",konutList = konutlar, value = value)

@app.route("/updateArsa/<string:id>")
def updateArsaData(id):
    value = "Arsa"
    arsaData = Arsa.query.filter_by(arsaId = id).first()
    if(arsaData.arsaDurum == "Satılık"):
        arsaData.arsaDurum = "Satıldı"
    elif(arsaData.arsaDurum == "Satıldı"):
        arsaData.arsaDurum = "Satılık"
    elif(arsaData.arsaDurum == "Kiralık"):
        arsaData.arsaDurum = "Kiralandı"
    elif(arsaData.arsaDurum == "Kiralandı"):
        arsaData.arsaDurum = "Kiralık"

    db.session.commit()
    arsalar = Arsa.query.all()
    return render_template("index.html",arsaList = arsalar,value = value)

@app.route("/updateisYeri/<string:id>")
def updateisYeriData(id):
    value = "isYeri"
    isYeriData = isYeri.query.filter_by(isyeriId = id).first()
    if(isYeriData.isyeriDurum == "Satılık"):
        isYeriData.isyeriDurum = "Satıldı"
    elif(isYeriData.isyeriDurum == "Satıldı"):
        isYeriData.isyeriDurum = "Satılık"
    elif(isYeriData.isyeriDurum == "Kiralık"):
        isYeriData.isyeriDurum = "Kiralandı"
    elif(isYeriData.isyeriDurum == "Kiralandı"):
        isYeriData.isyeriDurum = "Kiralık"

    db.session.commit()
    isYerleri = isYeri.query.all()
    return render_template("index.html", isYeriList = isYerleri,value = value)

@app.route("/deleteKonut/<string:id>")
def deleteKonutData(id):
    value = "Konut"
    konutData = Konut.query.filter_by(konutId = id).first()
    db.session.delete(konutData)
    db.session.commit()
    konutlar = Konut.query.all()
    return render_template("index.html",konutList = konutlar, value = value)

@app.route("/deleteArsa/<string:id>")
def deleteArsaData(id):
    value = "Arsa"
    arsaData = Arsa.query.filter_by(arsaId = id).first()
    db.session.delete(arsaData)
    db.session.commit()
    arsalar = Arsa.query.all()
    return render_template("index.html",arsaList = arsalar,value = value)

@app.route("/deleteisYeri/<string:id>")
def deleteisYeriData(id):
    value = "isYeri"
    isYeriData = isYeri.query.filter_by(isyeriId = id).first()
    db.session.delete(isYeriData)
    db.session.commit()
    isYerleri = isYeri.query.all()
    return render_template("index.html", isYeriList = isYerleri,value = value)

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)