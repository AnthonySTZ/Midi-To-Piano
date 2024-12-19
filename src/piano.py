import interface
import midi_handler as midi
import hou_nodes


def run(file_path: str):
    midi_file: midi.mido.MidiFile = midi.read_from_file(file_path)
    tracks = midi.get_all_tracks_from_midi_file(midi_file)

    context = hou_nodes.get_curr_context()
    channel_node = hou_nodes.create_channel_node(context, 88)
    for track in tracks:
        hou_nodes.animate_notes_by_track(channel_node, track, 1010)
    hou_nodes.transfer_chop_to_attrib(hou_nodes.get_selected_node(), channel_node)
