import midi_handler as midi

if __name__ == "__main__":
    midi_file: midi.mido.MidiFile = midi.read_from_file("assets\YLIA.mid")
    print(midi_file)