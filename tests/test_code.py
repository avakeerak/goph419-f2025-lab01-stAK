import numpy as np

from python_package.functions import (sqrt, arcsin, launch_angle_range)

print(launch_angle_range(2, 0.25, 0.02))

def launch_angle_numpy(ve_v0, alpha, tol_alpha):

    if ve_v0 <= 0:
        raise ValueError("ve_v0 must be greater than 0")
    if alpha < 0:
        raise ValueError("alpha must be non-negative")
    if tol_alpha < 0 or tol_alpha >= 1:
        raise ValueError("tol_alpha must satisfy 0 <= tol_alpha < 1")
    
    alpha_max = (1 + tol_alpha) * alpha
    alpha_min = (1 - tol_alpha) * alpha

    launch_angles = []

    for i in (alpha_max, alpha_min):

        radicand = 1 - ((i / (1 + i)) * (ve_v0 ** 2))
        if radicand < 0:
            raise ValueError("radicand must be non-negative")
        
        sqrt_radicand = np.sqrt(radicand)

        sin_phi = (1 + i) * sqrt_radicand
        
        launch_angles.append(np.arcsin(sin_phi))

    return np.array(launch_angles)

print(launch_angle_numpy(2, 0.25, 0.02))