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
