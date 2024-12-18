import midi_handler as midi

if __name__ == "__main__":
    midi_file: midi.mido.MidiFile = midi.read_from_file("assets\YLIA.mid")
    tracks_messages = []
    for track in midi_file.tracks:
        messages: list[dict] = midi.get_all_notes_from_track(track)
        if messages:
            tracks_messages.append(messages[5])
    print(tracks_messages)