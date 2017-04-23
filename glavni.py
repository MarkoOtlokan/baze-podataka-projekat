
from klase import *
import sys

db = SqliteDatabase('zadatak.db')

#preduzece,radnik,projekat
p=preduzece
r=radnik
pr=projekat
db.connect()

db.create_tables([projekat,radnik,preduzece], safe=True)

def novopreduzece():
    print 'unesi mbpreduzeca,ime,vlasnik,vrednost,adresa,brojradnika'
    mb,i,v,vr,a,b=raw_input().split()
    p.create(mbpreduzeca=str(mb),ime=i,vlasnik=v,vrednost=str(vr),adresa=a,brojradnika=str(b))

def noviradnik():
    print 'unesi mbpreduzeca,mbradnika,ime,prezime,brojtelefona,napomena,plata,adresa,godinazaposlenja, brojprojekata,godisnjiodmori'
    mbp,mbr,i,p,b,n,p,a,g,bp,god=raw_input().split()
    r.create(mbpreduzeca=str(mbp),mbradnika=str(mbr),ime=i,prezime=p,brojtelefona=str(b),napomena=n,plata=str(p),adresa=a,godinazaposlenja=str(g),brojprojekata=str(bp),godisnjiodmori=str(god))

def noviprojekat():
    print 'unesi mbradnika,mbprojekta,mbsefaprojekta,vrednostprojekta'
    mbr,mbp,mbs,vr=raw_input().split()
    pr.create(mbradnika=str(mbr),mbprojekta=str(mbp),mbsefaprojekta=str(mbs),vrednostprojekta=str(vr))

def ispisipreduzeca():
    print 'ime vlasnik mbpreduzeca vrednost adresa brojradnika'
    for pred in p.select():
        print pred.ime, pred.vlasnik,pred.mbpreduzeca,pred.vrednost,pred.adresa,pred.brojradnika
def ispisiradnike():
    print 'ime prezime mbr_radnika brojtelefona plata adresa broj projekata napomena'
    for rad in r.select():
        print rad.ime,rad.prezime,rad.mbradnika,rad.brojtelefona,rad.plata,rad.adresa,rad.brojprojekata,rad.napomena
def ispisiprojekte():
    print 'mbradnika mbprojekta mbsefaprojekta vrednost projekta'
    for pro in pr.select():
        print pro.mbprojekta,pro.mbsefaprojekta,pro.vrednostprojekta

def radniciprvefirme(sifre):
    samooni=r.select().where(r.mbpreduzeca==sifre)
    for rad in samooni:
        print rad.ime,rad.prezime,rad.brojtelefona,rad.plata,rad.adresa,rad.brojprojekata,rad.napomena
def projektiradnika(sifra):
    samooni=pr.select().where(pr.mbradnika==str(sifra))
    for pro in samooni:
        print pro.mbprojekta,pro.mbsefaprojekta,pro.vrednostprojekta

print 'moguce opcije \n ispisi preduzeca \n ispisi radnike \n ispisi projekte \n unesi preduzece \n unesi radnika \n unes projekta \n radnici odredjene firme \n zaduzenje radnika'
while(1):
    unos=raw_input()
    if unos=='ispisi preduzeca':
        ispisipreduzeca()
    if unos=='unesi preduzece':
        novopreduzece()
    if unos=='unesi radnika':
        noviradnik()
    if unos=='unesi projekat':
        noviprojekat()
    if unos=='ispisi radnike':
        ispisiradnike()
    if unos=='ispisi projekte':
        ispisiprojekte()
    if unos=='radnici odredjene firme':
        ispisipreduzeca()
        print 'unesi mbfirme'
        sifre=raw_input()
        radniciprvefirme(sifre)
    if unos=='zaduzenje radnika':
        print 'unesi njegov mbr'
        sifre=raw_input()
        projektiradnika(sifre)
    
