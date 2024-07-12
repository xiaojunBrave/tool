import pyrealsense2 as rs
import numpy as np
import cv2
import json
import time

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

# Create an align object
align_to = rs.stream.color
align = rs.align(align_to)

# Create a JSON object to save depth data
depth_data_json = []
click_x = 0
click_y = 0
def show():
    x = click_x
    y = click_y
    print("*****************")
    print(click_x, click_y)
    if x > 0 and y > 0:
         # Draw a circle at the clicked point
         cv2.circle(color_image, (x, y), 1, (0, 255, 0), 2)

         # Retrieve the world coordinates from the depth_data_json
         world_coords = depth_data_json[y][x]
         world_text = f"({world_coords['x']:.4f}, {world_coords['y']:.4f}, {world_coords['z']:.4f})"

         # Display the coordinates on the image
         cv2.putText(color_image, f"Pixel: ({x}, {y})", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
         cv2.putText(color_image, f"World: {world_text}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
         # Show the image with coordinates
    cv2.imshow('Aligned Color Image', color_image)
    # 将图片保存为JPG格式
    save_path = '../tmp/output_image.jpg'
    cv2.imwrite(save_path, color_image)

# Callback function to display coordinates and world coordinates on right-click
def show_coordinates(event, x, y, flags, param):
    global click_x, click_y
    if event == cv2.EVENT_RBUTTONDOWN:
        click_x = 0
        click_y = 0
    elif event == cv2.EVENT_LBUTTONDOWN:
        click_x = x
        click_y = y
    show()

try:
    while True:
        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        aligned_frames = align.process(frames)

        depth_frame = aligned_frames.get_depth_frame()
        color_frame = aligned_frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue

        # Get intrinsics
        intrinsics = depth_frame.profile.as_video_stream_profile().intrinsics

        # Initialize the JSON array with appropriate dimensions
        depth_data_json = [[{} for _ in range(intrinsics.width)] for _ in range(intrinsics.height)]

        # Convert depth frame to numpy array
        depth_image = np.asanyarray(depth_frame.get_data())

        # Convert color frame to numpy array
        color_image = np.asanyarray(color_frame.get_data())

        # Save the depth data to the JSON object
        for y in range(intrinsics.height):
            for x in range(intrinsics.width):
                # Get the depth value in meters
                depth_value = depth_frame.get_distance(x, y)

                # Convert from pixel coordinates to camera coordinates
                point = rs.rs2_deproject_pixel_to_point(intrinsics, [x, y], depth_value)

                # Save the coordinates in the JSON object
                depth_data_json[y][x] = {
                    "x": point[0],
                    "y": point[1],
                    "z": point[2]
                }

        # Set the mouse callback function
        cv2.namedWindow('Aligned Color Image')
        cv2.setMouseCallback('Aligned Color Image', show_coordinates)

        # Display the aligned color image
        show()
        # Break the loop if the 'ESC' key is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break

finally:
    # Stop streaming
    pipeline.stop()

    # Save the JSON object to a file
    with open("depth_data.json", "w") as depth_file:
        json.dump(depth_data_json, depth_file, indent=4)

    print("Depth data saved to depth_data.json")
