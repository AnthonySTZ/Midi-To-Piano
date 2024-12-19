import mido


def read_from_file(filename: str) -> mido.MidiFile:
    return mido.MidiFile(filename)


def show_tracks_infos(midi_file: mido.MidiFile) -> None:
    for i, track in enumerate(midi_file.tracks):
        track: mido.MidiTrack
        track_meta_messages = get_meta_messages_from_track(track)
        print(
            f"Track {i}: {track.name if track.name else 'No Name'} with {len(track)} messages including {len(track_meta_messages)} meta messages"
        )


def get_meta_messages_from_track(track: mido.MidiTrack):
    return list(filter(lambda msg: msg.is_meta, track))


def show_messages_from_track(
    track: mido.MidiTrack, start: int, nb_of_messages: int
) -> None:
    for msg in track[start : start + nb_of_messages]:
        print(msg)


def get_all_tracks_from_midi_file(midi_file: mido.MidiFile) -> list[list[dict]]:
    tracks_messages = []
    tempo: int = get_tempo_from(midi_file)
    for track in midi_file.tracks:
        messages: list[dict] = get_all_notes_from_track(track, midi_file)
        if messages["notes"]:
            messages["tempo"] = tempo
            tracks_messages.append(messages)
    return tracks_messages


def get_tempo_from(midi_file) -> int:
    for track in midi_file.tracks:
        for msg in track:
            if msg.type == "set_tempo":
                return msg.tempo
    return 500000


def get_all_notes_from_track(
    track: mido.MidiTrack, midi_file: mido.MidiFile
) -> list[dict]:
    notes: dict[str, int | list[dict]] = {
        "ticks_per_beat": midi_file.ticks_per_beat,
        "notes": [],
    }
    for msg in track:
        if msg.type == "note_on" or msg.type == "note_off":
            note = {
                "type": msg.type,
                "note": msg.note - 21,
                "offset": (
                    notes["notes"][-1]["offset"] + msg.time
                    if notes["notes"]
                    else msg.time
                ),
            }
            notes["notes"].append(note)
    return notes


def time_to_frames(ticks, tempo, ppqn, fps=24):
    # Convert ticks to seconds
    time_in_seconds = ticks_to_seconds(ticks, tempo, ppqn)
    # Convert seconds to frames
    return int(time_in_seconds * fps)


def ticks_to_seconds(ticks, tempo, ppqn):
    seconds_per_tick = (tempo / 1_000_000) / ppqn
    return ticks * seconds_per_tick
