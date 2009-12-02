import re
import codecs
from pprint import pprint

EOR = u"=========="

def records(file_path):
    clip_file = codecs.open( file_path )
    clip_file.seek( 3 ) # skip magic cookie

    record = list()
    for line in clip_file:
        line = line.decode( 'utf-8' )
        if line.strip() == EOR:
            assert record[2] == '', "Non-blank line expected separating the header from the body of the clipping:%s" % record[2]
            clip = dict()
            match = re.match( r'(.*?)\((.*)\)', record[0] )
            clip['title'], clip['attribution'] =match.groups() 
            clip['attribution'] = clip['attribution'].split( ') (' )

            match = re.match( r'- (\w+) Loc. ([^|]+)\| Added on (\w+), (\w+ \d+, \d+), (\d+:\d+ \w\w)', record[1] )
            clip['type'], clip['location'], clip['dow'], clip['date'], clip['time'] = match.groups()

            clip['body'] = "\n".join( record[3:] )

            # a little tidying
            clip['title'] = clip['title'].strip()
            clip['location'] = clip['location'].strip()

            # yield and reset for next record
            yield clip
            record = list() 
        else:
            record.append( line.strip() )

    clip_file.close()



if __name__ == '__main__':
    from sys import argv
    for n,r in enumerate( records(argv[1] ) ): #'My Clippings.txt') ):
        print n, 
        pprint( r )


