from peewee import *
import sys


db = SqliteDatabase('zadatak.db')

class preduzece(Model):
    mbpreduzeca= CharField()
    ime = CharField()
    vlasnik = CharField()
    vrednost = CharField()
    adresa = CharField()
    brojradnika=CharField()
    class Meta:
        database=db

class radnik(Model):
    mbpreduzeca=ForeignKeyField(preduzece, related_name='radi')
    mbradnika=CharField()
    mbsefa=CharField()
    ime = CharField()
    prezime = CharField()
    brojtelefona = CharField()
    napomena = CharField()
    plata = CharField()
    adresa=CharField()
    godinazaposlenja=CharField()
    brojprojekata=CharField()
    
    class Meta:
        database=db

class projekat(Model):
    mbpreduzeca=ForeignKeyField(preduzece, related_name='bavi se')
    mbprojekta=CharField()
    mbsefa=CharField()
    brojradnika=CharField()
    class Meta:
        database=db

db.connect()

db.create_tables([projekat,radnik,preduzece], safe=True)
preduzece.create(mbpreduzeca='123438',ime='Centar slavija',vlasnik='bratstvo jedinstvo',vrednost='300000',adresa='Topolska 18',brojradnika='3000')
preduzece.create(mbpreduzeca='341241',ime='Senta promet',vlasnik='Cira',vrednost='600000',adresa='Narodno fronta bb',brojradnika='7000')
preduzece.create(mbpreduzeca='178791',ime='Tigar',vlasnik='Miselin',vrednost='9000000',adresa='Sutjeska 25',brojradnika='1500')
preduzece.create(mbpreduzeca='785232',ime='Matijevic',vlasnik='Matijevic',vrednost='900000',adresa='Rumenacki put 29',brojradnika='6000')
preduzece.create(mbpreduzeca='425775',ime='Zastava',vlasnik='Drzava',vrednost='2000000',adresa='Partizanska 12',brojradnika='1000')
