import hou
import midi_handler as midi


def get_curr_context():
    selected_nodes = hou.selectedNodes()
    if not selected_nodes:
        raise ValueError("No nodes selected")
    return selected_nodes[0].parent()


def create_channel_node(context, number_of_notes):
    chopnet = context.createNode("chopnet")
    channel_node = chopnet.createNode("channel")
    create_channel_notes(channel_node, number_of_notes)
    return channel_node


def create_channel_notes(channel_node, number_of_notes):
    channel_node.parm("numchannels").set(number_of_notes)
    for i in range(number_of_notes):
        channel_node.parm("name" + str(i)).set("note_" + str(i))


def animate_notes_by_track(channel_node, track, start_frame):
    ticks_per_beat = track["ticks_per_beat"]
    tempo = track["tempo"]
    notes = track["notes"]
    for note in notes:
        parm = channel_node.parm("value" + str(note["note"]) + "x")
        note_frame = (
            midi.time_to_frames(note["offset"], tempo, ticks_per_beat) + start_frame
        )
        note_type = 1 if note["type"] == "note_on" else 0
        set_keyframe(parm, note_frame - 1, 1 - note_type)
        set_keyframe(parm, note_frame, note_type)


def set_keyframe(parm, frame, value):
    key = hou.Keyframe()
    key.setFrame(frame)
    key.setValue(value)
    parm.setKeyframe(key)
