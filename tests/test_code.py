import numpy as np

from python_package.functions import (sqrt, arcsin, launch_angle_range)

# Test the launch_angle_range function and print the result
print(f'Computed output: {launch_angle_range(1.5, 0.3, 0.02)}')

def launch_angle_numpy(ve_v0, alpha, tol_alpha):

    """
    Compute the minimum and maximum launch angles (in radians)
    using NumPy's built-in math functions for verification purposes.

    This function mirrors the logic of `launch_angle_range` from the
    custom implementation but uses `np.sqrt` and `np.arcsin` to provide
    a reference for comparison.

    Parameters
    ----------
    ve_v0 : float
        Ratio of escape velocity to terminal velocity. Must be > 0.
    alpha : float
        Fraction of Earth's radius. Must be > 0.
    tol_alpha : float
        Fractional tolerance applied to alpha (0 =<  tol_alpha < 1).

    Returns
    -------
    np.array
        Two-element array containing [max_angle, min_angle] in radians.

    Raises
    ------
    ValueError
        If parameters are invalid or the radicand becomes negative.
    """

    # Validate input parameters
    if ve_v0 <= 0:
        raise ValueError("ve_v0 must be greater than 0")
    if alpha < 0:
        raise ValueError("alpha must be non-negative")
    if tol_alpha < 0 or tol_alpha >= 1:
        raise ValueError("tol_alpha must satisfy 0 <= tol_alpha < 1")
    
    # Calculate upper and lower bounds for alpha
    alpha_max = (1 + tol_alpha) * alpha
    alpha_min = (1 - tol_alpha) * alpha

    # Create a list to hold the calculated launch angles
    phi_range = []

    # Calculate the range of allowable launch angles
    for i in (alpha_min, alpha_max):

        # Calculate the radicand and ensure it is non-negative
        radicand = 1 - ((i / (1 + i)) * (ve_v0 ** 2))
        if radicand < 0:
            raise ValueError("radicand must be non-negative")
        
        # Compute the square root of the radicand using NumPy
        sqrt_radicand = np.sqrt(radicand)

        # Compute the sine and inverse sine of the launch angles using NumPy, then store them
        sin_phi = (1 + i) * sqrt_radicand  
        phi_range.append(np.arcsin(sin_phi))

    # Return the array of [max_angle, min_angle]
    return np.array(phi_range)

# Print the result from the NumPy-based function for comparison
print(f'Expected output: {launch_angle_numpy(1.5, 0.3, 0.02)}')