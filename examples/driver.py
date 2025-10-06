from python_package.functions import (sqrt, arcsin, launch_angle_range)
import numpy as np
import matplotlib.pyplot as plt

def constant_ve_v0(ve_v0, tol_alpha):

    """
    Generate and save a plot showing the range of launch angles (in degrees)
    as a function of alpha for a fixed Ve/V0.

    Parameters
    ----------
    ve_v0 : float
        Ratio of escape velocity to terminal velocity.
    tol_alpha : float
        Fractional tolerance applied to alpha values.

    Returns
    -------
    None
        The function saves a plot as a PNG file and prints invalid alpha values.
    """

    # Create an array of alpha values from 0.01 to 3
    a_values = np.linspace(0.01, 3, 500)

    # Initialize lists to hold launch angles and failed alpha values
    min_angle = []
    max_angle = []
    failed_a = []

    # Calculate the max and min launch angles for each alpha value
    for a in a_values:
            try:
                # Compute the max and min launch angles in radians
                angles = launch_angle_range(ve_v0, a, tol_alpha)
                min_rads = (angles[1])
                max_rads = (angles[0])
            
            except ValueError:
                 # Record alpha values that cause a ValueError and append NaN to angles
                 failed_a.append(a)
                 min_angle.append(np.nan)
                 max_angle.append(np.nan)
                 continue
            
            # Convert radians to degrees
            min_deg = min_rads * (180 / 3.14159265359)
            max_deg = max_rads * (180 / 3.14159265359)

            # Store converted angles
            min_angle.append(min_deg)
            max_angle.append(max_deg)     

    # Define save path for the plot
    save_path = 'C:/Users/avake/GOPH419/goph419-f2025-lab01-stAK/figures/constant_ve_v0.png'

    # Creat and save the plot using matplotlib.pyplot
    plt.figure(figsize=(6.5, 4.5))
    plt.plot(a_values, min_angle, label='Minimum Launch Angle')
    plt.plot(a_values, max_angle, label='Maximum Launch Angle')
    plt.xlabel('alpha')
    plt.ylabel('Launch Angle (degrees)')
    plt.title(f'Launch Angle Range at Ve/V0 = {ve_v0}')
    plt.legend(loc='best')
    plt.savefig(save_path)
    plt.close()

    # Print any alpha values that caused a ValueError
    if failed_a:
        print(f"Values of alpha that caused a ValueError: {failed_a}")

def constant_alpha(alpha, tol_alpha):
    
    """
    Generate and save a plot showing the range of launch angles (in degrees)
    as a function of Ve/V0 for a fixed alpha value.

    Parameters
    ----------
    alpha : float
        Fraction of Earth's radius.
    tol_alpha : float
        Fractional tolerance applied to alpha.

    Returns
    -------
    None
        The function saves a plot as a PNG file and prints invalid Ve/V0 values.
    """

    # Create an array of Ve/V0 values from 0 to 5
    ve_v0_values = np.linspace(0, 5, 500)

    # Initialize lists to hold launch angles and failed ve_v0 values
    min_angle = []
    max_angle = []
    failed_ve_v0 = []

    # Calculate the max and min launch angles for each ve_v0 value
    for v in ve_v0_values:
            try:
                # Compute the max and min launch angles in radians
                angles = launch_angle_range(v, alpha, tol_alpha)
                min_rads = (angles[1])
                max_rads = (angles[0])
            
            except ValueError:
                 # Record ve_v0 values that cause a ValueError and append NaN to angles
                 failed_ve_v0.append(v)
                 min_angle.append(np.nan)
                 max_angle.append(np.nan)
                 continue
            
            # Convert radians to degrees
            min_deg = min_rads * (180 / 3.14159265359)
            max_deg = max_rads * (180 / 3.14159265359)

            # Store converted angles
            min_angle.append(min_deg)
            max_angle.append(max_deg)     

    # Define save path for the plot
    save_path = 'C:/Users/avake/GOPH419/goph419-f2025-lab01-stAK/figures/constant_alpha.png'

    # Creat and save the plot using matplotlib.pyplot
    plt.figure(figsize=(6.5, 4.5))
    plt.plot(ve_v0_values, min_angle, label='Minimum Launch Angle')
    plt.plot(ve_v0_values, max_angle, label='Maximum Launch Angle')
    plt.xlabel('Ve/V0')
    plt.ylabel('Launch Angle (degrees)')
    plt.title(f'Launch Angle Range at alpha = {alpha}')
    plt.legend(loc='best')
    plt.savefig(save_path)
    plt.close()

    # Print any ve_v0 values that caused a ValueError
    if failed_ve_v0:
        print(f"Values of Ve/Vo that caused a ValueError: {failed_ve_v0}")

def main():
    """
    Main driver function that generates both plots:
      1. Launch angle vs. alpha for constant Ve/V0.
      2. Launch angle vs. Ve/V0 for constant alpha.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    # Generate plot 1 (constant Ve/V0)
    constant_ve_v0(2, 0.04)

    # Generate plot 2 (constant alpha)
    constant_alpha(0.25, 0.02)

# Execute main function when the script is run
main()