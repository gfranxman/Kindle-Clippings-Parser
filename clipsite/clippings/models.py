from django.db import models

class DocSource( models.Model ):
    name = models.CharField( max_length=100, unique=True )


class Document( models.Model ):
    name = models.CharField( max_length=100, unique=True )

    sources = models.ManyToManyField( DocSource )
    cr_date = models.DateTimeField( auto_now_add=True)


class ClipType( models.Model ):
    name = models.CharField( max_length=50, primary_key=True )


class Clip( models.Model ):
    user = models.ForeignKey( 'auth.User', null=True, )
    document = models.ForeignKey( Document )
    type = models.ForeignKey( ClipType )

    cr_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField( max_length=20 )
    body = models.TextField(null=True, blank=True)

    record = models.TextField(null=True, blank=True)

