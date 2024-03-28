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
- `torch` library with CUDA support
- CUDA capable GPU and CUDA drivers
- FFMPEG codecs

You can install these dependencies using pip:

  pip install librosa
  
  pip install torch torchaudio --extra-index-url https://download.pytorch.org/whl/cu121 --index-url https://download.pytorch.org/whl/cu121/torch_stable -f https://download.pytorch.org/whl/3.10.6/cu121/torch_stable.html
  
  *Note: The value 3.10.6 in "https://download.pytorch.org/whl/3.10.6/cu121/torch_stable.html" should be replaced with your exact Python version.


CUDA drivers:
  https://developer.nvidia.com/cuda-downloads


FFMPEG codecs:
  https://ffmpeg.org/

## License

This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
Let me know if you need any further assistance!
