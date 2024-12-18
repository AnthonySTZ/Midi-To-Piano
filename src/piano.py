import midi_handler as midi
import hou_nodes

def run():
    midi_file: midi.mido.MidiFile = midi.read_from_file("C:\\Disque E\\Prog\\python_midi\\assets\\YLIA.mid")
    tracks = midi.get_all_tracks_from_midi_file(midi_file)

    context = hou_nodes.get_curr_context()
    hou_nodes.create_channel_node(context, 88)



run()