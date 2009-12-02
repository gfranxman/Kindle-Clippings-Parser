import re

EOR = "=========="

def records(file_path):
    clip_file = open( file_path, "r" )
    clip_file.seek( 3 ) # skip magic cookie

    record = list()
    for line in clip_file:
        if line.strip() == EOR:
            assert record[2] == '', "Non-blank line expected separating the header from the body of the clipping:%s" % record[2]
            clip = dict()
            match = re.match( r'(.*?)\((.*)\)', record[0] )
            clip['title'], clip['attribution'] =match.groups() 
            clip['attribution'] = clip['attribution'].split( ') (' )

            match = re.match( r'- (\w+) Loc. ([^|]+)\| Added on (\w+), (\w+ \d+, \d+), (\d+:\d+ \w\w)', record[1] )
            clip['type'], clip['location'], clip['dow'], clip['date'], clip['time'] = match.groups()

            clip['body'] = "\n".join( record[3:] )

            yield clip
            record = list() 
        else:
            record.append( line.strip() )

    clip_file.close()



if __name__ == '__main__':
    for n,r in enumerate( records('My Clippings.txt') ):
        print n, r


