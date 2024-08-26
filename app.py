import os
from models.speech_to_text import record_audio, speech_to_text
from models.llm_query import query_llm
from models.text_to_speech import generate_audio_response
from utils.vad import vad

def main():
    while True:
        print("Ask anything you want:")
        audio_file = record_audio()  # Record audio from microphone

        if vad(audio_file):
            print("Voice detected, processing...")
            text = speech_to_text(audio_file)
            print(f"Query: {text}")

            response = query_llm(text)
            print(f"Response: {response}")

            output_file = generate_audio_response(response)
            print(f"Audio response saved to: {output_file}")
            os.system(f"start {output_file}")
        else:
            print("No voice detected. Please try again.")

        # Ask the user if they want to continue
        continue_prompt = input("Do you want to continue (yes/no)? ").strip().lower()
        if continue_prompt != 'yes':
            print("Exiting the chatbot. Goodbye!")
            break

if __name__ == "__main__":
    if not os.path.exists('output'):
        os.makedirs('output')
    main()
