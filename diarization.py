import librosa

def get_audio_segments(audio_path, segment_duration=4):
    y, sr_rate = librosa.load(audio_path, sr=None)

    samples_per_segment = int(segment_duration * sr_rate)
    segments = []

    for start in range(0, len(y), samples_per_segment):
        end = start + samples_per_segment
        segments.append((y[start:end], sr_rate))

    return segments
