import cv2
import numpy as np
from pybullet_envs.bullet.kukaCamGymEnv import KukaCamGymEnv
import pybullet as p

# Create the KukaCamGymEnv environment with rendering enabled
env = KukaCamGymEnv(renders=True, isDiscrete=False)

# Initialize the video writer
width, height = 640, 480
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

# Run the simulation and save the rendered frames as a video
num_steps = 100
for step in range(num_steps):
    action = env.action_space.sample()
    _, _, done, _ = env.step(action)

    # Get the rendered image
    _, _, rgba_img, _, _ = p.getCameraImage(width, height, renderer=p.ER_BULLET_HARDWARE_OPENGL)
    frame = np.array(rgba_img)

    # Convert the image to the format expected by OpenCV
    frame = frame[:, :, :3]
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write the frame to the video
    out.write(frame)

    if done:
        env.reset()

# Release the video writer
out.release()
env.close()