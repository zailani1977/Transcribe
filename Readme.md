# Transcribe Audio

This Python script transcribes audio files using a deep learning model. It takes in an m4a audio file and a transcript file, converts the audio file to WAV format, resamples the audio, performs transcription and saves the transcription to the specified file.

## Usage

To use this script, simply run the following command:
python transcribe.py <audio_file> <transcript_file>

Replace `<audio_file>` with the path to the audio file you want to transcribe, and `<transcript_file>` with the path to the file where you want to save the transcription.

## Dependencies

This script requires the following dependencies:

- Python 3.x
- `librosa` library
- `torch` library
- CUDA drivers

You can install these dependencies using pip:
pip install librosa torch

## License

This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
Let me know if you need any further assistance!