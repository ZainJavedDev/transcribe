
import json
import whisper
from pydub import AudioSegment
from pathlib import Path


def load_audio(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    ext = path.suffix.lstrip(".").lower()
    if ext not in {"wav", "mp3", "flac", "ogg", "m4a", "wma", "aac", "webm"}:
        raise ValueError(f"Unsupported format: .{ext}")

    # Non-wav formats: convert to wav via pydub
    if ext != "wav":
        audio = AudioSegment.from_file(file_path, format=ext)
        wav_path = path.with_suffix(".tmp.wav")
        audio.export(wav_path, format="wav")
        return str(wav_path)

    return file_path


def transcribe(file_path: str, model_size: str = "base") -> list[dict]:
    wav_path = load_audio(file_path)
    model = whisper.load_model(model_size)
    result = model.transcribe(wav_path, verbose=False)

    segments = [
        {
            "start": round(seg["start"], 2),
            "end": round(seg["end"], 2),
            "text": seg["text"].strip(),
        }
        for seg in result["segments"]
    ]
    return {"full_text": result["text"].strip(), "segments": segments}


if __name__ == "__main__":

    model = "base"
    audio_file = "files/audio.wav"

    print(f"Transcribing: {audio_file} (model: {model})")
    result = transcribe(audio_file, model)

    print(json.dumps(result, indent=2, ensure_ascii=False))
