
# Face Recognition Project

This project contains folders for creating Face Recognition Scripts.

## Folder Structure
- **Training Folders**: The training folders are named after the Presidents of Finland. Each folder is expected to contain images of the respective individual.
- **Validation Folder**: Includes two pictures of presidents for testing or validation purposes.
- **Output Folder**: Currently empty and not in use yet. This folder is intended to store the results of the face recognition process.

## Current Status
The project currently includes a basic face recognition script for testing purposes.

### Features:
1. **Basics**:
   - Face verification
   - Face detection
   - Generating face vectors
   - Facial attribute analysis
2. **Self-built Analysis**:
   - Face detection analysis
     - Score listing for easier readability

### Note
The `venv` folder is no longer updated in the repository to reduce its size. Dependencies must be installed separately (see below).

## Next Steps
1. **Add a Face Recognition Script**:
   - Implement a script to:
     - Train a model using images in the training folders.
     - Validate the model with images in the validation folder.
     - Save results in the output folder.

## Usage Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Update the `faceRecognition.py` file:
   - The script uses the `DeepFace` library.
   - To install `DeepFace`, activate the virtual environment and run:
     ```bash
     pip install deepface
     ```
4. Check the file for your use, do the modifications
5. run file
   ```bash
   python faceRecognition.py  
   ```

Feel free to modify this project to suit your specific needs!
