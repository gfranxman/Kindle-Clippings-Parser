from clipsite.clippings import parser
from clipsite.clippings import models

def load( filepath ):
    for n, record in enumerate( parser.records( filepath ) ):
        cliptype, is_new = models.ClipType.objects.get_or_create( 
            name__exact = record['type'], 
            defaults = { 'name': record['type'] } )
        print "cliptype", cliptype, is_new
    
        authors = list()
        for author in record['attribution']:
            docsource, is_new = models.DocSource.objects.get_or_create( 
                name__exact = author,
                defaults = { 'name': author } )
            authors.append( docsource )


        doc, is_new = models.Document.objects.get_or_create( name__exact = record['title'], defaults= { 'name': record['title'] } )
        print "doc", doc, is_new
        for author in authors:
            doc.sources.add( author )
            doc.save()
    
        clip, is_new = models.Clip.objects.get_or_create( 
            user__id__exact = 1,
            document__name__exact = doc.name, 
            type__name__exact = cliptype.name, 
            location__exact = record['location'],
            defaults ={ 'user_id': 1, 
                'document': doc,
                'type': cliptype,
                'location': record['location'],
                'body': record['body'],
                },
            )
        print "clip", clip, is_new
        if not is_new:
            clip.body = record['body']
            clip.save()


if __name__ == '__main__':
    from sys import argv
    for f in argv[1:]:
        print "loading", f
        load( f )
