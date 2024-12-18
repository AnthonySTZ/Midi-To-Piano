import mido

def read_from_file(filename:str)->mido.MidiFile:
    return mido.MidiFile(filename)