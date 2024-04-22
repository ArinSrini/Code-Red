from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import numpy as np
import soundfile as sf
import tenseal as ts

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Dummy storage for sender's binary data (in a real app, this would be a database)
sender_data = None

# YASHE context setup
context = ts.context(ts.SCHEME_TYPE.BGV, poly_modulus_degree=4096, plain_modulus=40961)
secret_key = context.secret_key()
public_key = context.public_key()

# Web form for receiver's private key input
class PrivateKeyForm(FlaskForm):
    private_key = PasswordField('Private Key', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Route for sender to record audio
@app.route('/', methods=['GET', 'POST'])
def record_audio():
    global sender_data

    if request.method == 'POST':
        # Simulate audio recording and conversion to binary data
        audio_data = np.random.randint(0, 2, size=10)  # Example binary data (replace with actual conversion)

        # Apply YASHE encryption
        encrypted_data = context.encrypt(audio_data, public_key)

        # Store encrypted data (in a real app, store in a database associated with sender)
        sender_data = encrypted_data.serialize()

        return redirect(url_for('record_audio'))

    return render_template('record_audio.html')

# Route for receiver to input private key and decrypt data
@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt_audio():
    form = PrivateKeyForm()

    if form.validate_on_submit():
        private_key_str = form.private_key.data
        private_key = ts.keygen(context, private_key_str)

        # Retrieve and decrypt sender's data
        decrypted_data = ts.Ciphertext(context, private_key).deserialize(sender_data)
        decrypted_audio = context.decrypt(decrypted_data, secret_key)

        # Perform audio reconstruction (replace with actual reconstruction process)
        reconstructed_audio = np.random.randint(0, 2, size=10)  # Example reconstruction

        # Save or play reconstructed audio (replace with actual saving or playback)

        flash('Audio decrypted and reconstructed successfully!', 'success')
        return redirect(url_for('decrypt_audio'))

    return render_template('decrypt_audio.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
