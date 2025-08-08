import time
import sys
import random
from typing import List, Tuple

"""
This module provides functions to create and display an animated frame
with a circle that moves vertically based on given positions.
"""

try:
    import cv2
    import numpy as np
except ImportError:
    print("\nOpenCV and NumPy are required for animation. Please install them.\n")
    sys.exit(1)

def print_coords_on_frame(frame: np.ndarray, x: int, y: int, a=None) -> np.ndarray:
    """Draws the coordinates on the returned frame."""

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (0, 0, 255)  # Red (B, G, R) for visibility
    font_thickness = 2
    text_position = (10, 30)  # Top-left corner for the text
    text = f"({x}, {y})"
    if a is not None:
        text = f"({x}, {y}, {a})"
    return cv2.putText(frame, text, text_position, font, font_scale, font_color, font_thickness, cv2.LINE_AA)

def draw_frame(frame_width: int, frame_height: int, position: Tuple[int, ...]) -> np.ndarray:
    """Draws a frame with a circle that moves vertically based on the position tuple."""

    circle_center_x = frame_width // 2
    initial_circle_center_y = frame_height // 2
    circle_radius=10

    x = position[0] if len(position) > 0 else 0
    y = position[1] if len(position) > 1 else 0
    a = position[2] if len(position) > 2 else None # not always used
    
    # reate a frame and color it about the x-axis
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
    frame[0:frame_height // 2, 0:frame_width] = [255, 255, 255]  # White (B, G, R)
    frame[frame_height // 2:frame_height, 0:frame_width] = [255, 0, 0]  # Blue (B, G, R)

    # Calculate the new Y position of the circle 
    current_circle_center_y = initial_circle_center_y + (y)

    # ensure the circle stays within the frame boundaries
    current_circle_center_y = max(circle_radius, min(frame_height - circle_radius, current_circle_center_y))
    cv2.circle(frame, (circle_center_x, current_circle_center_y), circle_radius, (0, 0, 0), -1) # Black, filled

    frame = print_coords_on_frame(frame, x, y, a)
    
    return frame

def run_animation(positions: List[Tuple[int, ...]]) -> None:
    """Loops through the positions list to display sub position animation."""

    # Create a window for the animation
    cv2.namedWindow("Animation", cv2.WINDOW_AUTOSIZE)    
    frame_width=600
    frame_height=400
    cv2.resizeWindow("Animation", frame_width, frame_height)
    delay_ms = 15 # frame delay in milliseconds = ~ 66 FPS

    # Loop through the positions and draw each frame
    for p in positions:
        frame = draw_frame(frame_width, frame_height, p)    
        cv2.imshow("Animation", frame) # show frame
        
        # Wait for the specified delay
        time.sleep(delay_ms / 1000.0)
        
        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            sys.exit(0)

    gracefully_exit()

prev_frame = None

def run_crazy_animation(positions: List[Tuple[int, ...]]) -> None:
    global prev_frame

    cv2.namedWindow("Animation", cv2.WINDOW_AUTOSIZE)    
    frame_width=600
    frame_height=400
    cv2.resizeWindow("Animation", frame_width, frame_height)
    delay_ms = 15 

    alpha = 0.80  # feedback blending factor
    hue_shift = 5  # Amount to shift hue per frame
    current_hue = 0

    def shift_hue(frame, shift):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv[..., 0] = (hsv[..., 0].astype(int) + shift) % 180
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    for p in positions:
        frame = draw_frame(frame_width, frame_height, p)
        if prev_frame is not None:
            if random.random() > 0.85:
                frame = cv2.flip(frame, 0)  # Flip vertically
            blended_frame = cv2.addWeighted(frame, 1-alpha, prev_frame, alpha, 0)
        else:
            blended_frame = frame
        current_hue += hue_shift
        blended_frame = shift_hue(blended_frame, current_hue)
        cv2.imshow("Animation", blended_frame)
        prev_frame = blended_frame.copy()
        time.sleep(delay_ms / 1000.0)  # Convert milliseconds to seconds
        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    gracefully_exit()


def gracefully_exit():
    # Wait for a key press to close the window; let user see final frame
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    sys.exit(0)

if __name__ == "__main__":
    positions = [(0, 0, None),
                 (10, 5, None),
                 (5, 10, None),
                 (0, 20, None),
                 (0, 10, None),
                 (10, 5, None),
                 (0, 0, None),
                 (10, 15, None),
                 (0, -10, None),
                 (10, 5, None),
                 (0, 0, None),
                 (5, 10, None),
                 (0, 20, None),
                 (0, 10, None),
                 (10, 5, None),
                 (0, 0, None),
                 (10, 15, None),
                 (0, -10, None),
                 (10, 5, None),
                 (0, 0, None),
                 (10, 5, None)]  # Example positions for testing
    
    run_animation(positions)