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
    
while(1):
    unos=raw_input()
    if unos=='unesi preduzece':
        novopreduzece()
    if unos=='unesi radnika':
        noviradnik()
    if unos=='unesi projekat':
        noviprojekat()
