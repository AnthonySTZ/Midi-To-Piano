import hou


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
