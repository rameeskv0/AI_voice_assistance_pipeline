import os
import edge_tts

async def text_to_speech(text, output_file="output.mp3", voice="en-US-JennyNeural"):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    return output_file

def generate_audio_response(text, output_file="output/output.mp3"):
    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    output_path = loop.run_until_complete(text_to_speech(text, output_file))
    loop.close()
    return output_path
