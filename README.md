
# Face Recognition Project

This project contains folders for creating Face Recognition Scripts.

## Folder Structure
- **Training Folders**: The training folders are named after the Presidents of Finland. Each folder is expected to contain images of the respective individual.
- **Validation Folder**: Includes two pictures of presidents for testing or validation purposes.
- **Output Folder**: Currently empty and not in use yet. This folder is intended to store the results of the face recognition process.

## Current Status
The scores and metrics displayed (such as emotions, age, and race percentages) are not yet accurate <br>and should be considered as placeholders or initial outputs during testing phases.
<br>Future work will involve refining the accuracy of these predictions through improvements in the algorithm, dataset quality, and model training processes.

### Features:
1. **Basics**:
   - Face verification
   - Face detection
   - Generating face vectors
   - Facial attribute analysis
2. **Self-built Analysis**:
   - Face detection analysis
     - Score listing for easier readability

### PDF Output (You can see the Output File in the output folder of the project)


<div>
  <img src="https://github.com/user-attachments/assets/e10eca5f-c73f-4fd0-8861-f034b9ce83f5" alt="Analysis Results" width="400">
</div>


### Note
The `venv` folder is no longer updated in the repository to reduce its size. Dependencies must be installed separately (see below).

## Next Steps
1. **Add a Face Recognition Script**:
   - Implement a script to:
     - Find the persons from the images.

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
5. Use the virtual environment
6. Install required libraries found in the script
   - deepface, fpdf
7. Run file
   ```bash
   python faceRecognition.py  
   ```

Feel free to modify this project to suit your specific needs!
