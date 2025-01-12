# Face Recognition Project

This project contains folders for creating Face Recognition Scripts.

## Folder Structure
- **Training Folders**: The training folders are named after the Presidents of Finland. Each folder is expected to contain images of the respective individual.
- **Validation Folder**: Includes two pictures of presidents for testing or validation purposes.
- **Output Folder**: Currently empty and not in use yet. This folder is intended to store the results of the face recognition process.

## Current Status
The project does have the first face recognition script to test face recognition.
**!** The venv folder is not updated in GitHub anymore for the growth of libraries (see dependencies).

## Next Steps
1. **Add a Face Recognition Script**:
   - Implement a script to:
     - Train a model using images in the training folders.
     - Validate the model with images in the validation folder.
     - Save results in the output folder.

2. **Dependencies**:
   - The file faceRecognition.py uses DeepFace library.
   - The instructions to install the libraries in venv:
      - Git Bash:
         a. Get into the virtual environment.
        
         b. bash:
           ```pip install deepface ```

3. **Contribute**:
   - Contributions are welcome to build the face recognition script and improve the project structure.

## Usage Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
  ```bash
  pip install -r requirements.txt
  ```

Feel free to modify it based on your project's specifics!
