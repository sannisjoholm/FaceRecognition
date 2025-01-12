from deepface import DeepFace

# Always start by venv in the console $ source venv/Scripts/activate
# This script requires: Python >=3.7

backends = [
  'opencv', 
  'ssd', 
  'dlib', 
  'mtcnn', 
  'fastmtcnn',
  'retinaface', 
  'mediapipe',
  'yolov8',
  'yunet',
  'centerface',
]

alignment_modes = [True, False]



# Stream your webcam or videos (5 sec)
#DeepFace.stream(db_path = "C:/User/Sefik/Desktop/database")

# This verifies, that two images are about the same person. Set those two images in the path.

obj = DeepFace.verify(
  img1_path = "validation/Niinisto4.jpg", 
  img2_path = "training/Niinisto/Niinisto1.jpg",
  detector_backend = backends[0],
  align = alignment_modes[0],
)
#print(obj)



# This will find similar images from your db by the picture. Set the image path and the database path.

dfs = DeepFace.find(
  img_path = "validation/Niinisto4.jpg", 
  db_path = "training/", 
  detector_backend = backends[1],
  align = alignment_modes[0],
)
print(dfs)

# Sometimes, you need embedding vectors directly. Face recognition models create those multidimensional vectors of the images.
"""
embedding_objs = DeepFace.represent(
  img_path = "img.jpg", 
  detector_backend = backends[2],
  align = alignment_modes[0],
)

"""

# Facial attribute analysis
"""
demographies = DeepFace.analyze(
  img_path = "img4.jpg", 
  detector_backend = backends[3],
  align = alignment_modes[0],
)
"""

#face detection and alignment
"""
face_objs = DeepFace.extract_faces(
  img_path = "img.jpg", 
  detector_backend = backends[4],
  align = alignment_modes[0],
)
"""


# Face detection analysis
"""
img_path = "validation/Untitled.jpg"
results = DeepFace.analyze(img_path=img_path, actions=['emotion', 'age', 'gender', 'race'])

# Access the first element of the results (if it's a list)
if isinstance(results, list):  # Check if results is a list
    results = results[0]  # Get the first dictionary in the list

# Printed results
print("\n")
print("\n")
print("\n--- Analysis Results ---")
print(f"Age: {results['age']}")
print(f"Dominant Gender: {results['dominant_gender']}")
print(f"Dominant Emotion: {results['dominant_emotion']}")
print(f"Dominant Race: {results['dominant_race']}")

print("\n--- More Detailed Information ---")
angry = results['emotion']['angry']
disgust = results['emotion']['disgust']
fear = results['emotion']['fear']
happy = results['emotion']['happy']
sad = results['emotion']['sad']
neutral = results['emotion']['neutral']
print(f"\nEmotions:")
print(f"angry: {angry:.2f}")
print(f"disgust: {disgust:.2f}")
print(f"fear: {fear:.2f}")
print(f"happy: {happy:.2f}")
print(f"sad: {sad:.2f}")
print(f"neutral: {neutral:.2f}")


#print("Emotions:", results['emotion'])
print("\n")
asian = results['race']['asian']
indian = results['race']['indian']
black = results['race']['black']
white = results['race']['white']
middle_eastern = results['race']['middle eastern']
latino_hispanic = results['race']['latino hispanic']
print(f"Races:")
print(f"asian: {asian:.2f}")
print(f"indian: {indian:.2f}")
print(f"black: {black:.2f}")
print(f"white: {white:.2f}")
print(f"middle eastern: {middle_eastern:.2f}")
print(f"latino hispanic: {latino_hispanic:.2f}")
print("\n")
print("\n")
#print("Races:", results['race'])
"""

