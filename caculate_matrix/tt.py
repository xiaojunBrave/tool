import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera App")
        
        self.video_frame = ttk.Label(root)
        self.video_frame.grid(row=0, column=0, padx=10, pady=10)

        self.capture_button = ttk.Button(root, text="Capture", command=self.capture_image)
        self.capture_button.grid(row=1, column=0, padx=10, pady=10)

        self.cap = cv2.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_frame.imgtk = imgtk
            self.video_frame.configure(image=imgtk)
        self.root.after(10, self.update_frame)

    def capture_image(self):
        ret, frame = self.cap.read()
        if ret:
            filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.jpg")
            cv2.imwrite(filename, frame)
            print(f"Image saved as {filename}")

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()
