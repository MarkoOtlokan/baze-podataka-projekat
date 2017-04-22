from peewee import *
import sys


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
    mbradnika=CharField()
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

db.connect()

db.create_tables([projekat,radnik,preduzece], safe=True)
preduzece.create(mbpreduzeca='12',ime='Centar slavija',vlasnik='bratstvo jedinstvo',vrednost='300000',adresa='Topolska 18',brojradnika='3000')
preduzece.create(mbpreduzeca='34',ime='Senta promet',vlasnik='Cira',vrednost='600000',adresa='Narodno fronta bb',brojradnika='7000')
preduzece.create(mbpreduzeca='17',ime='Tigar',vlasnik='Miselin',vrednost='9000000',adresa='Sutjeska 25',brojradnika='1500')
preduzece.create(mbpreduzeca='78',ime='Matijevic',vlasnik='Matijevic',vrednost='900000',adresa='Rumenacki put 29',brojradnika='6000')
preduzece.create(mbpreduzeca='42',ime='Zastava',vlasnik='Drzava',vrednost='2000000',adresa='Partizanska 12',brojradnika='1000')

radnik.create(mbpreduzeca='12',mbradnika='21',ime='Misa',prezime='Nisa',godisnjiodmori='20',brojtelefona='0631287023',napomena='nema',plata='50000',adresa='Janak veselinovica bb',godinazaposlenja='1990',brojprojekata='2')

radnik.create(mbpreduzeca='12',mbradnika='20',ime='Marko',prezime='Maravic',godisnjiodmori='20',brojtelefona='063128112',napomena='nema',plata='70000',adresa='Janak veselinovica 22',godinazaposlenja='1995',brojprojekata='1')

radnik.create(mbpreduzeca='12',mbradnika='14',ime='Dimitrije',prezime='Mandic',godisnjiodmori='20',brojtelefona='06312872133',napomena='nema',plata='30000',adresa='Janak veselinovica 55',godinazaposlenja='2015',brojprojekata='3')

radnik.create(mbpreduzeca='34',mbradnika='88',ime='Misa',prezime='Pavlovic',godisnjiodmori='20',brojtelefona='0651287023',napomena='nema',plata='80000',adresa='Janak veselinovica 99',godinazaposlenja='2000',brojprojekata='2')

radnik.create(mbpreduzeca='34',mbradnika='99',ime='Lazar',prezime='Ilic',godisnjiodmori='20',brojtelefona='0612387023',napomena='nema',plata='80000',adresa='Janak veselinovica 1',godinazaposlenja='2005',brojprojekata='4')

projekat.create(mbradnika='21',mbprojekta='122',mbsefaprojekta='21',vrednostprojekta='20000')
projekat.create(mbradnika='21',mbprojekta='1234',mbsefaprojekta='21',vrednostprojekta='80000')
projekat.create(mbradnika='12',mbprojekta='122',mbsefaprojekta='21',vrednostprojekta='20000')
projekat.create(mbradnika='14',mbprojekta='122',mbsefaprojekta='21',vrednostprojekta='20000')
projekat.create(mbradnika='14',mbprojekta='1234',mbsefaprojekta='21',vrednostprojekta='80000')
projekat.create(mbradnika='14',mbprojekta='1',mbsefaprojekta='14',vrednostprojekta='200')
projekat.create(mbradnika='88',mbprojekta='77',mbsefaprojekta='88',vrednostprojekta='950000000')
projekat.create(mbradnika='88',mbprojekta='66',mbsefaprojekta='88',vrednostprojekta='20000')
projekat.create(mbradnika='99',mbprojekta='77',mbsefaprojekta='88',vrednostprojekta='950000000')
projekat.create(mbradnika='99',mbprojekta='77',mbsefaprojekta='88',vrednostprojekta='20000')
projekat.create(mbradnika='99',mbprojekta='12',mbsefaprojekta='99',vrednostprojekta='200')
