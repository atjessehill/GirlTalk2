
remixer = None
player = None
driver = None
track = None

paper = None
tiles = []
selectedTile = None



def createTiles(qtype):

    tiles = []
    qlist = track.analysis[qtype]

    for i in qlist:
        tiles.append(createTile(i, qlist[i]))
    return tiles

def fetchAnalysis(trid):

    calls remixer.remixTrack()


    # ex: parent = 'sections', child = 'bars
def connectQuanta(track, parent, child):

    last = 0
    qparents = track.analysis[parent]
    qchildren = track.analysis[child]

    for qparent in qparents:
        qparent.children = [] # TODO add .children to classes

        for j in range(last, len(qchildren)):
            qchild = qchild[j]
            if (qchild.start >= qparent.start) and (qchild.start < qparent.start + qparent.duration):
                    qchild.parent = qparent
                    qchild.indexInParent = len(qparent.children)
                    qparent.children.append(qchild)
                    last = j
            elif (child.start > qparent.start):
                break





def preprocessTrack(track):
    # jremix.js 58
    types = ['sections', 'bars', 'beats', 'tatums', 'segments']


    # track is of type JukeboxTrack
    # track.analysis is of type JukeboxAnalysis which has lists of segments, bars, etc.
    for type in types: # for each sections, bars, etc.
        for j in range(0, len(track.analysis[type])): # for each item in ex: track.analysis['sections']

            qlist = track.analysis[type] # entire list of type track.analysis['sections']
            # j = parseInt(j) # iterating through

            # TODO what is q and where does it get .track/.which
            # it is like it is creating a linked list
            # In JS, you can add variables to an object, like .track
            # TODO add variables to spotifyInfo
            q = qlist[j] #q is of type
            q.track = track
            q.which = j

            if j > 0:
                q.prev = qlist[j-1]

            else:
                q.prev = None

            if j < qlist.length - 1:
                q.next = qlist[j+1]
            else:
                q.next = None

    connectQuanta(track, 'sections', 'bars')

def populate_spotify_classes():

    analysis = data from spotify

    for i in analysis['sections']:
        sections.append(SpotifyAudioSection(i))

    for i in analysis['bars']:
        bars.append(SpotifyAudioBar(i))

    for i in analysis['beats']:
        beats.append(SpotifyAudioBeat(i))

    for i in analysis['tatums']:
        tatums.append(SpotifyAudioTatum(i))

    for i in analysis['segments']:
        segments.append(SpotifyAudioSegment(i))


def init():

    # $("#play").click(
    #     function() {
    #         if (driver.isRunning()) {
    #             driver.stop();
    #         } else {
    #             driver.setAutobot(false);
    #             driver.start();
    #         }
    #     }
    # );

    # Line 1180
    # var context = getAudioContext();
    # remixer = createJRemixer(context, $);
    # player = remixer.getPlayer();
    # driver = Driver(player)
    # processParams();
