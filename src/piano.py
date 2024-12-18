import midi_handler as midi
import hou_nodes

def run():
    midi_file: midi.mido.MidiFile = midi.read_from_file("C:\\Disque E\\Prog\\python_midi\\assets\\YLIA.mid")
    tracks_messages = []
    for track in midi_file.tracks:
        messages: list[dict] = midi.get_all_notes_from_track(track)
        if messages:
            tracks_messages.append(messages)

    context = hou_nodes.get_curr_context()
    hou_nodes.create_channel_node(context, 88)



run()