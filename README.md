
# AI Voice Assistance Pipeline

## Overview

This project is designed to build an end-to-end AI voice assistance pipeline. The system performs the following steps:
1. **Voice-to-Text Conversion**: Records voice input and converts it into text using the Whisper model.
2. **Text Input into LLM**: Sends the text to a Large Language Model (LLM) to generate a response using `OllamaLLM`.
3. **Text-to-Speech Conversion**: Converts the generated response into speech and plays it back.

The pipeline supports Voice Activity Detection (VAD), output restriction to a maximum of two sentences, and allows tunable parameters such as pitch, voice type, and speed for the text-to-speech conversion.

## Requirements

- Python 3.8+
- Whisper for Speech-to-Text
- Ollama for LLM queries (via `langchain-ollama`)
- Edge TTS for Text-to-Speech
- PyAudio for audio recording
- Webrtcvad for voice activity detection

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/rameeskv0/AI_voice_assistance_pipeline.git
   cd AI_voice_assistance_pipeline

2.  **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  ```
3. **Install Required Packages**

Create the requirements.txt file with the following content:

``` 
    whisper
    pyaudio
    wave
    webrtcvad
    edge-tts
    langchain
    langchain-ollama
    ollama
 ```
Then install the dependencies:


```pip install -r requirements.txt```

4. **Download and Set Up Models**

- **Whisper Model**: For higher accuracy, use the large model:

```
import whisper
model = whisper.load_model("large")
```

- **Ollama:** 

   1.Download Ollama from ```ollama.com``` and follow the installation instructions provided on the website.

   2.After installation, use the command prompt to download the llama3 model:
```ollama pull llama3```


## Usage

1. **Record and Process Voice**

    Run the app.py script to start the voice assistant:
```python app.py```
The script will:

- Prompt for a voice query.
- Record the query.
- Convert the recorded audio to text using Whisper.
- Generate a response using the LLM (OllamaLLM).
- Convert the response to speech and play it back.

2. **Interactive Session**

   After playing the audio response, the script will prompt:

- "Ask anything you want:"
- "Do you want to continue (yes/no)?"

- Enter your query and choose to continue or exit based on your preference.

## Code Structure
- app.py: Main script to run the pipeline. Handles recording, processing, and playback.
- models/speech_to_text.py: Contains functions for recording audio and converting speech to text using Whisper.
- models/llm_query.py: Contains functions for querying the LLM using OllamaLLM from langchain-ollama.
- models/text_to_speech.py: Contains functions for converting text to speech using Edge TTS.
- utils/vad.py: Implements Voice Activity Detection.

## Configuration

**Voice-to-Text (Whisper)**
- Model Choice: Using the large model for higher accuracy.
- Audio Settings: Sampling rate of 16 kHz, mono channel. 

**Text-to-Speech (Edge TTS)**
- Voice Options: Customizable parameters such as pitch, voice type (male/female), and speed.

    Command Examples:
   ```edge-tts --voice en-US-JennyNeural --text "Hello, world!" --write-media output/response.mp3 --rate=0% --pitch=0%```


**LLM Query (OllamaLLM)**
- Library: Using langchain-ollama to interface with the LLM.

  - Model: llama3 for generating responses.
     ```
      from langchain_ollama import OllamaLLM
      model = OllamaLLM(model="llama3")
      response = model.invoke(input="capital city of India")
  
## Latency Optimization
  To ensure low latency:

- Use asynchronous processing where possible.
- Optimize the model and audio settings for performance.
- Consider hardware acceleration for large models.

## Troubleshooting
- ModuleNotFoundError: Ensure all dependencies are installed and correctly listed in requirements.txt.
-  Audio Issues: Verify microphone setup and audio file path configurations.


## Acknowledgments
- Whisper: OpenAI Whisper
- Edge TTS: Edge TTS GitHub
- Ollama: Ollama
- LangChain: LangChain
