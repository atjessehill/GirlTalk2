# class SpotifyPiece:
#     def __init__(self):
#         self.next = None
#         self.prev = None
#
# class SpotifyTrack:
#     def __init__(self):
#         self.href = None
#         self.id = None
#         self.name = None
#         self.uri = None
#         self.duration = None
#         self.explicit = None
#         self.artists = []
#
# class SpotifyArtist:
#     def __init__(self):
#         self.id = None
#         self.name = None
#
# class SpotifyAudio:
#
#     def __init__(self):
#         self.meta = SpotifyAudioMeta()
#         self.bars = []
#         self.beats = [] #
#         self.tatums = []
#         self.sections = []
#         self.segments = []
#
# class SpotifyAudioMeta:
#
#     def __init__(self):
#         analyzer_version = None
#         analyzer_platform = None
#         # val analyzer_version: String,
#         # val platform: String,
#         # val detailed_status: String,
#         # val status_code: Int,
#         # val analysis_time: Double,
#         # val input_process: String
#
# class SpotifyAudioTrack:
#
#     def __init__(self):
#         self.duration = None
#         self.loudness = None
#         self.tempo = None
#         self.time_signature = None
#         self.key = None
#         self.mode = None
#
# class SpotifyAudioBar:
#
#     def __init__(self):
#         self.start = None
#         self.duration = None
#         self.confidence = None
#
#
# class SpotifyAudioBeat:
#
#     def __init__(self):
#         self.start = None
#         self.duration = None
#         self.confidence = None
#
#
# class SpotifyAudioTatum:
#
#     def __init__(self):
#         self.start = None
#         self.duration = None
#         self.confidence = None
#
#
# class SpotifyAudioSection:
#     def __init(self):
#         self.start = None
#         self.duration = None
#         self.confidence = None
#         self.loudness = None
#         self.tempo = None
#         self.tempo_confidence = None
#         self.key = None
#         self.key_confidence = None
#         self.mode = None
#         self.mode_confidence = None
#         self.time_signature = None
#         self.time_signature_confidance = None
#
# class SpotifyAudioSegment:
#     def __init__(self):
#         self.start = None
#         self.duration = None
#         self.confidence = None
#         self.loudness_start = None
#         self.loudness_max_time = None
#         self.loudness_max = None
#         self.pitches = None
#         self.timbre = None


class SpotifyPiece:
    def __init__(self):
        self.next = None
        self.prev = None
        self.which = None


class SpotifyAudioSection(SpotifyPiece):
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

        SpotifyPiece.__init__(self)


class SpotifyAudioSegment(SpotifyPiece):
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

        SpotifyPiece.__init__(self)


class SpotifyAudioTatum(SpotifyPiece):
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

        SpotifyPiece.__init__(self)


class SpotifyAudioBeat(SpotifyPiece):
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

        SpotifyPiece.__init__(self)


class SpotifyAudioBar(SpotifyPiece):
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

        SpotifyPiece.__init__(self)

