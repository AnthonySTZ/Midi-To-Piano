import os
import sys


def run() -> None:
    plugin_path = os.environ["HOUDINI_PIANO_PLUGIN_PATH"]

    sys.path.insert(0, plugin_path)

    from importlib import reload
    import hou_nodes as nodes
    import midi_handler as midi
    import interface
    import piano

    reload(nodes)
    reload(midi)
    reload(interface)
    reload(piano)


run()
