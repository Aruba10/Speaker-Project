from diarization import get_audio_segments
from asr import convert_speech
from captioning import generate_caption

audio_path = "audio/test.wav"

print("\n🔊 AI Speaker Captioning Running...\n")

segments = get_audio_segments(audio_path)

speaker_toggle = 1

for i, (segment, sr_rate) in enumerate(segments):
    filename = f"temp_{i}.wav"

    text = convert_speech(segment, sr_rate, filename)

    caption = generate_caption(f"Speaker {speaker_toggle}", text)

    print(caption)

    speaker_toggle = 2 if speaker_toggle == 1 else 1

print("\n✅ Done\n")
