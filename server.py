from flask import Flask, request, jsonify
import librosa
import numpy as np

app = Flask(__name__)

@app.route('/process_audio', methods=['POST'])
def process_audio():
    try:
        # Check if the POST request contains the 'audio' file
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400

        audio_file = request.files['audio']

        # Check if the audio file is empty
        if audio_file.filename == '':
            return jsonify({'error': 'No audio file selected'}), 400

        # Check if the file format is WAV
        if audio_file.mimetype != 'audio/wav':
            return jsonify({'error': 'Unsupported audio format. Please upload a WAV file'}), 400

        # Save the audio file to a temporary location
        audio_file_path = 'temp_audio.wav'
        audio_file.save(audio_file_path)

        # Load the audio file and extract the audio data
        audio_data, sr = librosa.load(audio_file_path, sr=None)

        # Perform processing on the audio data (replace this with your processing logic)
        # For demonstration purposes, we'll just compute the mean of the audio samples
        audio_mean = np.mean(audio_data)

        # Return the result
        return jsonify({'audio_mean': audio_mean}), 200

    except Exception as e:
        return jsonify({'error': f'Error processing audio: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
