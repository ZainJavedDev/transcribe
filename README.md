# Audio Transcription Pipeline

Local audio-to-text transcription using OpenAI's open-source [Whisper](https://github.com/openai/whisper) model.

## Setup

Requires Python 3.10+ and [ffmpeg](https://ffmpeg.org/).

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

By default it transcribes `files/audio.wav` with the `base` model. Edit the `__main__` block in `main.py` to change the input file or model size (`tiny`, `base`, `small`, `medium`, `large`).

## Features

- Supports WAV, MP3, FLAC, OGG, M4A, AAC, WMA, WEBM (auto-converts to WAV via pydub/ffmpeg)
- Returns full text + per-segment timestamps as JSON
- Configurable model size for speed vs accuracy tradeoff

## Output example

```json
{
  "full_text": "The stale smell of old beer lingers. It takes heat to bring out the odor. A cold dip restores health and zest. A salt pickle tastes fine with ham. Tacos al pastor are my favorite. A zestful food is the hot cross bun.",
  "segments": [
    {
      "start": 0.0,
      "end": 4.0,
      "text": "The stale smell of old beer lingers."
    },
    {
      "start": 4.0,
      "end": 7.0,
      "text": "It takes heat to bring out the odor."
    },
    {
      "start": 7.0,
      "end": 10.0,
      "text": "A cold dip restores health and zest."
    },
    {
      "start": 10.0,
      "end": 12.0,
      "text": "A salt pickle tastes fine with ham."
    },
    {
      "start": 12.0,
      "end": 15.0,
      "text": "Tacos al pastor are my favorite."
    },
    {
      "start": 15.0,
      "end": 18.0,
      "text": "A zestful food is the hot cross bun."
    }
  ]
}
```