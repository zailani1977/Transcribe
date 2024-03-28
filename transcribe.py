"""
Transcribes audio from an m4a file to a text transcript.

Args:
    audio_file (str): Path to the input m4a audio file.
    transcript_file (str): Path to the output transcript file.

Raises:
    argparse.ArgumentError: If required arguments are missing.

Example usage:
    python transcribe_audio.py --audio_file audio.m4a --transcript_file transcript.txt
"""

import sys
import argparse
import subprocess
from pydub import AudioSegment
import os
from transformers import pipeline

def convert_to_wav(audio_file):
    """
    Converts an audio file from the m4a format to the wav format using ffmpeg.

    Parameters:
        audio_file (str): The path to the input audio file in m4a format.

    Returns:
        str: The path to the converted audio file in wav format.
    """
    output_file = audio_file.replace('.m4a', '.wav')
    if os.path.isfile(output_file):
        os.remove(output_file)
    subprocess.run(['ffmpeg', '-i', audio_file, output_file], check=True)
    return output_file

def resample_audio(input_file):
    """
    Resamples an audio file to 16 kHz.

    Args:
        input_file (str): The path to the input audio file.

    Returns:
        str: The path to the resampled audio file.

    Raises:
        subprocess.CalledProcessError: If the ffmpeg command fails to run.
    """
    resample_file = input_file.replace('.wav', '_16kHz.wav')
    if os.path.isfile(resample_file):
        os.remove(resample_file)
    subprocess.run(['ffmpeg', '-i', input_file, '-ar', '16000', resample_file], check=True)
    return resample_file

def perform_transcription(audio_file):
    """
    Perform transcription on the given audio file and return the transcribed text.
    
    Args:
        audio_file: A string representing the path to the audio file.
    
    Returns:
        A string containing the transcribed text from the audio file.
    """
    whisper = pipeline("automatic-speech-recognition", model="openai/whisper-large", device="cuda")
    transcription = whisper(audio_file)
    return transcription["text"]

def save_transcript(text, transcript_file):
    """
    Save the given transcript text to the specified transcript file.

    Parameters:
        text (str): The transcript text to be saved.
        transcript_file (str): The path to the file where the transcript will be saved.

    Returns:
        None
    """
    with open(transcript_file, "w") as f:
        f.write(text)

def clean_up_wav_file(file_path):
    """
    Deletes the specified WAV file if it exists.

    Parameters:
        file_path (str): The path to the WAV file to be cleaned up.

    Returns:
        None
    """
    if os.path.exists(file_path):
        os.remove(file_path)
        print("Cleaned up .wav file:", file_path)

def clean_up(file_paths):
    """
    Cleans up the given file paths by calling clean_up_wav_file for each file path.

    :param file_paths: a list of file paths to be cleaned up
    :return: None
    """
    for file_path in file_paths:
        clean_up_wav_file(file_path)

def transcribe_audio(audio_file, transcript_file):
    """
    transcribe_audio function takes in an audio file and a transcript file, 
    converts the audio file to WAV format, resamples the audio, performs transcription, 
    saves the transcription to the specified file, and cleans up temporary files 
    in case of an error during transcription.
    """
    try:
        audio_file = convert_to_wav(audio_file)
        resampled_file = resample_audio(audio_file)
        transcription_text = perform_transcription(resampled_file)
        save_transcript(transcription_text, transcript_file)
        clean_up([audio_file, resampled_file])
        print("Transcription saved to", transcript_file)
    except Exception as e:
        print("Error occurred during transcription:", str(e))
        clean_up([audio_file, resampled_file])

def main():
    parser = argparse.ArgumentParser(description='Transcribe audio from m4a file to text transcript')
    parser.add_argument('audio_file', type=str, help='Path to the input m4a audio file')
    parser.add_argument('transcript_file', type=str, help='Path to the output transcript file')
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print("Error: " + str(e))
        print("Usage: python your_script.py --audio_file <audio_file> --transcript_file <transcript_file>")
        sys.exit(2)

    transcribe_audio(args.audio_file, args.transcript_file)

if __name__ == "__main__":
    main()