
from urx import URRobot
import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
import rtde_receive

save_dir = 'C:\\Users\\Administrator\\Desktop\\collect\\'
rtde = None
lines = []
class CameraApp:
    def __init__(self, root):
        self.num = 1
        self.root = root
        self.root.title("Camera App")

        self.video_frame = ttk.Label(root)
        self.video_frame.grid(row=0, column=0, padx=10, pady=10)

        self.capture_button = ttk.Button(root, text="Capture", command=self.capture_image)
        self.capture_button.grid(row=1, column=0, padx=10, pady=10)

        self.cap = cv2.VideoCapture(2)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_frame.imgtk = imgtk
            self.video_frame.configure(image=imgtk)
        self.root.after(100, self.update_frame)

    def capture_image(self):
        ret, frame = self.cap.read()
        if ret:
            filename = save_dir + str(self.num) + ".jpg"
            cv2.imwrite(filename, frame)
            print(f"Image saved as {filename}")
            tcp_pose = rtde.getActualTCPPose()
            lines.append(str(tcp_pose) + ",")
            # 打开一个txt文件用于写入
            with open(save_dir + "output.txt", "w", encoding="utf-8") as file:
                for line in lines:
                    file.write(line + "\n")
            self.num += 1

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()


if __name__ == "__main__":
    server_ip = '192.168.1.77'
    rtde = rtde_receive.RTDEReceiveInterface("192.168.1.77")
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()




