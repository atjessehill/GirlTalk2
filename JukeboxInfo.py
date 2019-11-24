class JukeboxTrack:

    def __init__(self):
        self.info = None
        self.analysis = None
        self.audio_summary = None

class JukeboxInfo:

    def __init__(self):
        self.service = None
        self.id = None
        self.name = None
        self.title = None
        self.artist = None
        self.url = None
        self.duration = None

class JukeboxAnalysis:

    def __init__(self):

        self.sections = None
        self.bars = None
        self.beats = None
        self.tatums = None
        self.segments = None

class JukeboxSummary:

    def __init__(self):
        self.duration = None