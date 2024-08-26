import webrtcvad
import wave

def vad(audio_file):
    vad = webrtcvad.Vad(1)
    wf = wave.open(audio_file, 'rb')
    sample_rate = wf.getframerate()


    if sample_rate not in [8000, 16000, 32000, 48000]:
        raise ValueError("Unsupported sample rate: {}".format(sample_rate))

    frame_duration_ms = 30
    frame_length = int(sample_rate * (frame_duration_ms / 1000.0))
    frames = wf.readframes(frame_length)

    if len(frames) != frame_length * wf.getsampwidth():
        raise ValueError("Frame length doesn't match the expected length.")

    return vad.is_speech(frames, sample_rate)
