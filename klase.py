from peewee import *

db = SqliteDatabase('zadatak.db')

class preduzece(Model):
    mbpreduzeca=PrimaryKeyField()
    ime = CharField()
    vlasnik = CharField()
    vrednost = CharField()
    adresa = CharField()
    brojradnika=CharField()
    class Meta:
        database=db

class radnik(Model):
    mbpreduzeca=ForeignKeyField(preduzece,  db_column='mbpreduzeca')
    mbradnika=PrimaryKeyField()
    ime = CharField()
    prezime = CharField()
    brojtelefona = CharField()
    napomena = CharField()
    plata = CharField()
    adresa=CharField()
    godinazaposlenja=CharField()
    brojprojekata=CharField()
    godisnjiodmori=CharField()

    class Meta:
        database=db

class projekat(Model):
    mbradnika=ForeignKeyField(radnik, db_column='mbradnika')
    mbprojekta=CharField()
    mbsefaprojekta=CharField()
    vrednostprojekta=CharField()
    class Meta:
        database=db                                                                                                                                                 

class imovinafirme(Model):
    mbpreduzeca=ForeignKeyField(preduzece,  db_column='mbpreduzeca')
    vrednost=CharField()
    naziv=CharField()

class javnenabavke(Model):
    mbpreduzeca=ForeignKeyField(preduzece,  db_column='mbpreduzeca')
    vrednost=CharField()
    naziv=CharField()
    datum=CharField()

class imovinaradnika(Model):
    mbpreduzeca=ForeignKeyField(preduzece,  db_column='mbpreduzeca')
    vrednost=CharField()                                                                                                                                            
    naziv=CharField()
