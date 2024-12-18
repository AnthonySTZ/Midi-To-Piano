import mido

def read_from_file(filename:str)->mido.MidiFile:
    return mido.MidiFile(filename)

def show_tracks_infos(midi_file:mido.MidiFile) -> None:
    for i, track in enumerate(midi_file.tracks):
        track_meta_messages = get_meta_messages_from_track(track)
        print(f"Track {i}: {track.name if track.name else 'No Name'} with {len(track)} messages including {len(track_meta_messages)} meta messages")

def get_meta_messages_from_track(track: mido.midifiles.tracks.MidiTrack):
    return list(filter(lambda msg: msg.is_meta, track))