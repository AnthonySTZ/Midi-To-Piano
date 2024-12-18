import midi_handler as midi

if __name__ == "__main__":
    midi_file: midi.mido.MidiFile = midi.read_from_file("assets\YLIA.mid")
    messages: list[dict] = midi.get_all_notes_from_track(midi_file.tracks[3])
    print(messages[0:5])
    # midi.show_messages_from_track(midi_file.tracks[3], 17, 10)