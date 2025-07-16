import whisper

def transcribe_voice(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result['text']

def parse_command(text):
    if "rewrite" in text:
        return {"action": "rewrite", "style": "poetic"}  # basic parser
