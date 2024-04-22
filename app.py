from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired
import wave
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Dummy storage for sender's binary data (in a real app, this would be a database)
sender_binary_data = None

# Web form for receiver's private key input
class PrivateKeyForm(FlaskForm):
    private_key = PasswordField('Private Key', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Function to convert audio file to binary and save as a text file
def convert_audio_to_binary_and_save_as_text(audio_file_path, text_file_path):
    # Open the audio file
    audio_file = wave.open(audio_file_path, 'rb')

    # Get the audio data
    frames = audio_file.readframes(-1)
    audio_data = np.frombuffer(frames, dtype=np.uint8)

    # Convert audio data to binary string
    binary_data = ''.join(format(x, '08b') for x in audio_data)

    # Save binary data as text in the specified file
    with open(text_file_path, 'w') as text_file:
        text_file.write(binary_data)

    # Close the audio file
    audio_file.close()

# Function to reconstruct audio from binary data stored in a text file
def reconstruct_audio_from_text_file(text_file_path, output_audio_path):
    # Read binary data (as text) from text file
    with open(text_file_path, 'r') as text_file:
        binary_data = text_file.read()

    # Convert binary data back to audio data
    reconstructed_audio_data = np.array([int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8)], dtype=np.uint8)

    try:
        # Determine audio parameters from the original audio file (audio.wav)
        original_audio_file = wave.open('audio.wav', 'rb')
        params = original_audio_file.getparams()
        original_audio_file.close()

        # Write the reconstructed audio data to a new WAV file
        reconstructed_audio_file = wave.open(output_audio_path, 'wb')
        reconstructed_audio_file.setparams(params)  # Set parameters based on original audio
        reconstructed_audio_file.writeframes(reconstructed_audio_data.tobytes())
        reconstructed_audio_file.close()

        print("Reconstructed audio saved as '{}'".format(output_audio_path))
    except Exception as e:
        print("Error during audio reconstruction:", e)

# Route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for sender to record audio and convert to binary
@app.route('/sender', methods=['GET', 'POST'])
def sender():
    global sender_binary_data

    if request.method == 'POST':
        # Simulate audio recording (replace with actual audio recording logic)
        audio_file_path = 'audio.wav'
        text_file_path = 'sender_binary.txt'

        # Convert audio to binary and save as text file
        convert_audio_to_binary_and_save_as_text(audio_file_path, text_file_path)

        # Read binary data from text file (for demonstration)
        with open(text_file_path, 'r') as text_file:
            sender_binary_data = text_file.read()

        return redirect(url_for('sender'))

    return render_template('sender.html')

# Route for receiver to input private key and reconstruct audio from binary data
@app.route('/receiver', methods=['GET', 'POST'])
def receiver():
    form = PrivateKeyForm()

    if form.validate_on_submit():
        private_key_str = form.private_key.data

        # Check if sender binary data is available
        if sender_binary_data:
            # Reconstruct audio from binary data and save to file
            output_audio_path = 'reconstructed_audio.wav'
            reconstruct_audio_from_text_file(sender_binary_data, output_audio_path)

            flash('Audio reconstructed successfully!', 'success')
            return redirect(url_for('receiver'))

    return render_template('receiver.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
