# Face Recognition

# What is this?

This is a little software that can be trained to detect a face using a camera (webcam for example).

# How to use?

1. Clone this repo.

    ```terminal
    git clone https://github.com/seevoid/face-recognition-OpenCV.git

1. Activate virtual env.
    - on Windows :
        ```terminal
        ./face_rec_env/Scripts/activate

3. Install the required libraries.

    - using pip :

        ```terminal
        pip install -r requirements.txt

4. Record a dataset of the face you want to detect.

    ```terminal
    python face_rec.py

5. Train the ML model

    ```terminal
    python trainer.py

6. Play with the software :)

    ```terminal
    python face_recognitnion.py

# License 

MIT