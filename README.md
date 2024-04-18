
# Code Red

This project includes tools and scripts for audio preprocessing, waveform modeling, and scrambling using Python modules and utilities.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains several components for working with audio data:

- **Audio_Functions.py**: Python module providing functions for audio preprocessing and feature extraction.
- **Audio_Scrambler.py**: Script for audio scrambling using encryption techniques.
- **Audio waveform modelling.ipynb**: Jupyter notebook demonstrating audio preprocessing and waveform modeling.
- **Audio Functions.ipynb**: Jupyter notebook showcasing examples of functions from `Audio_Functions.py`.
- **a2m.ipynb**: Jupyter notebook detailing the process of converting audio to binary and reconstruction.

## Project Structure

```
├── Audio_Functions.py      # Python module for audio preprocessing
├── Audio_Scrambler.py       # Script for audio scrambling
├── Audio waveform modelling.ipynb   # Jupyter notebook for audio preprocessing
├── Audio Functions.ipynb    # Jupyter notebook with examples of audio functions
├── a2m.ipynb                # Jupyter notebook for audio to binary conversion (MAIN FILE - USE THIS)
├── output2.wav              # Output audio file generated by recording script
└── README.md                # Project README file
```

## Setup and Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/ArinSrini/Code-Red.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Recording Audio

Use `Audio_Scrambler.py` to record audio and save it as a WAV file (`output2.wav`):

```bash
python Audio_Scrambler.py
```

### Audio Preprocessing and Modeling

Explore `Audio waveform modelling.ipynb` and `Audio Functions.ipynb` for examples and techniques related to audio preprocessing and feature extraction.

### Audio Scrambling

Use `Audio_Scrambler.py` to apply scrambling techniques to audio data. Modify the script to incorporate encryption methods like YASHE (BGV) for secure audio transmission or storage.

## Examples

Check out the Jupyter notebooks (`Audio waveform modelling.ipynb` and `Audio Functions.ipynb`) for detailed examples of audio preprocessing and feature extraction using `Audio_Functions.py`.


## Waveform Modelling

### Contents of `a2m.ipynb`

The `a2m.ipynb` notebook (`audio to binary conversion`) is the main file for the audio conversion process, where audio data is processed, converted into binary format, and reconstructed back from binary to audio. Here's an overview of what you'll find inside `a2m.ipynb`:

1. **Audio Loading and Preprocessing**:
   - Loading audio data from WAV files using libraries like `wave` and `numpy`.
   - Preprocessing steps such as downsampling, normalizing, or applying transformations like PCM-DM (Pulse Code Modulation - Delta Modulation) or Mel Frequency Cepstral Coefficients (MFCC).

2. **Audio to Binary Conversion**:
   - Converting the preprocessed audio data into binary representation.
   - This could involve encoding the audio samples into a binary format suitable for storage or transmission.

3. **Binary to Audio Reconstruction**:
   - Reconstructing audio from binary data.
   - Decoding the binary data back into audio samples and generating a WAV file.

4. **Visualization and Analysis**:
   - Visualizing the audio waveform, spectrogram, or other features before and after conversion.
   - Analyzing the quality and fidelity of the reconstructed audio compared to the original.

5. **Integration with Audio Functions**:
   - Utilizing functions from `Audio_Functions.py` for specific audio processing tasks within the conversion and reconstruction pipeline.

### Key Functions and Processes in `a2m.ipynb`

- **Audio Loading and Playback**:
  - Loading audio data using `wave` module.
  - Playing back audio samples to verify integrity.

- **Preprocessing**:
  - Applying preprocessing techniques (e.g., normalization, feature extraction) using functions from `Audio_Functions.py`.

- **Conversion to Binary**:
  - Converting audio samples into binary representation, potentially using techniques like quantization or encoding.

- **Reconstruction from Binary**:
  - Decoding binary data back into audio samples and generating a new WAV file.

- **Visualization and Analysis**:
  - Visualizing audio features, waveform, and spectrogram for comparison and analysis.

### Usage Recommendations

1. **Execute and Explore**:
   - Run each cell in `a2m.ipynb` sequentially to execute the audio conversion and reconstruction process.
   - Explore the intermediate steps and visualizations to understand the transformations applied to the audio data.

2. **Customization and Extension**:
   - Modify parameters and functions in `a2m.ipynb` to customize the audio processing pipeline according to specific requirements.
   - Integrate additional audio processing techniques or encryption methods (like YASHE) for advanced applications.

3. **Documentation and Sharing**:
   - Document key findings, observations, and insights within the notebook.
   - Share the notebook (`a2m.ipynb`) along with results to collaborate and demonstrate the audio processing workflow.
   - Convert the notebook (`a2m.ipynb`) file into python file and import it to your scrambler.py file which uses Homomorphic Encryption (BGV - YASHE).

## Contributing

Contributions to this project are welcome! Please fork the repository, make your changes, and submit a pull request for review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
