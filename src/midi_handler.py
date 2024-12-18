import mido

def read_from_file(filename:str)->mido.MidiFile:
    return mido.MidiFile(filename)

def show_tracks_infos(midi_file:mido.MidiFile) -> None:
    for i, track in enumerate(midi_file.tracks):
        track: mido.MidiTrack        
        track_meta_messages = get_meta_messages_from_track(track)
        print(f"Track {i}: {track.name if track.name else 'No Name'} with {len(track)} messages including {len(track_meta_messages)} meta messages")

def get_meta_messages_from_track(track: mido.MidiTrack):
    return list(filter(lambda msg: msg.is_meta, track))

def show_messages_from_track(track: mido.MidiTrack, start: int, nb_of_messages: int)->None:
    for msg in track[start: start + nb_of_messages]:
        print(msg)

def get_all_notes_from_track(track: mido.MidiTrack)->list[dict]:
    notes: list[dict] = []
    for i, msg in enumerate(track):
        if msg.type == 'note_on':
            note = {'note': msg.note - 21, "offset" : msg.time, "time" : track[i+1].time}
            notes.append(note)
    return notes