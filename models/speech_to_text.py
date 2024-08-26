import whisper
import pyaudio
import wave

def record_audio(output_file="output/input.wav", record_seconds=5, sampling_rate=16000):
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sampling_rate,
                    input=True,
                    frames_per_buffer=1024)

    print("Recording...")
    frames = []

    for _ in range(0, int(sampling_rate / 1024 * record_seconds)):
        data = stream.read(1024)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sampling_rate)
        wf.writeframes(b''.join(frames))

    return output_file

def speech_to_text(audio_file):
    model = whisper.load_model("small.en")
    result = model.transcribe(audio_file, language="en", verbose=False)
    text = result['text']
    return text.strip()
