import dot_convert
import cv2
import numpy as np

real_time = True


def main():
    # get the webcam
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        dot_img = dot_convert.convert_image(
            frame, dots=i, dot_size=5, color="black", contrast_factor=1.0
        )
        # Convert PIL Image back to numpy array for OpenCV
        dot_img = np.array(dot_img)
        # Convert RGB to BGR (OpenCV uses BGR)
        dot_img = cv2.cvtColor(dot_img, cv2.COLOR_RGB2BGR)

        # stream the dot image
        cv2.imshow("webcam", dot_img)

        # wait for 100ms
        cv2.waitKey(100)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # release the webcam
    cap.release()


if __name__ == "__main__":
    main()
