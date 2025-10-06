import numpy as np

def sqrt(x):

    """
    Approximates the square root of x using a Taylor series expansion
    around a nearby base point 'a' within the range (0, 2.5].

    Parameters
    ----------
    x : float
        Input value for which the square root is to be approximated.
        Must be between > 0 and <= 2.5.

    Returns
    -------
    float
        Approximation of the square root of x.

    Raises
    ------
    ValueError
        If x is outside the range (0, 2.5].
    """
    
    # Choose a base point 'a' and its corresponding square root depending on the value of x to ensure the series converges
    if x > 0 and x < 0.75:
        a = 0.5
        sqrt_a = 0.70710678
    elif x >= 0.75 and x < 1.25:
        a = 1
        sqrt_a = 1
    elif x >= 1.25 and x < 1.75: 
        a = 1.5
        sqrt_a = 1.22474487
    elif x >= 1.75 and x < 2.25:
        a = 2
        sqrt_a = 1.41421356
    elif x >= 2.25 and x <= 2.5:
        a = 2.5
        sqrt_a = 1.58113883
    else:
        raise ValueError("Input must be between 0 and 2.5")
    
    # Initialize the sum and sum of previous term for the Taylor series expansion
    sum_k = 0
    prev_sum = 0

    # Set a tolerance level for convergence
    tolerance  = 1 * 10**-8
    
    # Compute series terms up to k = 100 or until series converges
    for k in range(1, 100):
        
        # Compute factorial of k
        fact_k = 1

        for i in range(2, k + 1):
            fact_k *=i 

        # Compute the coefficient for the k-th term        
        prod_k = 1

        for j in range(1, k):

            prod_k *= (-0.5 * ((2 * j) - 1))

        coef_k = 0.5 * prod_k / fact_k

        # Compute the k-th term of the Taylor series
        term_k = ((x - a) ** k) / (sqrt_a ** ((2 * k) - 1)) * coef_k

        # Update the cumulative sum for the series
        sum_k += term_k

        # Compute the current approximation of sqrt(x)
        sqrt_x = sqrt_a + sum_k
        
        # Check for convergence and stop if within tolerance
        if abs(sqrt_x - prev_sum) <= tolerance * abs(sqrt_x):
            break

        # Update the previous sum for the next iteration
        prev_sum = sum_k

    # Return the approximated square root of x
    return sqrt_x

def arcsin(x):

    """
    Approximate arcsin(x) using a converging series representation from Borwein and Chamberland (2007).
    Calls upon the sqrt(x) function defined above.

    Parameters
    ----------
    x : float
        Input value for which arcsin(x) will be approximated.

    Returns
    -------
    float
        Approximation of arcsin(x).
    """

    # Set a tolerance level for convergence
    tolerance  = 1 * 10**-8

     # Initialize the sum and sum of previous term
    sum_n = 0

    prev_sum = 0
    
    # Compute series terms up to n = 100 or until series converges
    for n in range(1, 100):

        # Compute factorial of 2n
        fact_2n = 1
        n2 = n * 2

        for i in range(1, n2 + 1):
            fact_2n *= i

        # Compute factorial of n
        fact_n = 1

        for j in range(1, n + 1):
            fact_n *= j

        # Compute the numerator and denominator for the n-th term
        denom_n = (n ** 2) * (fact_2n / (fact_n **2))

        numer_n = (2 * x) ** (2 * n)

        # Compute the n-th term of the series
        term_n = numer_n / denom_n

        # Update the cumulative sum for the series
        sum_n += term_n

        # Compute the current approximation of arcsin(x)
        arcsin_x2 = sum_n * 0.5

        arcsin_x = sqrt(arcsin_x2)

        # Check for convergence and stop if within tolerance
        if abs(arcsin_x - prev_sum) <= tolerance * abs(arcsin_x):
            break

        # Update the previous sum for the next iteration
        prev_sum = arcsin_x

    # Return the approximated arcsin(x)
    return arcsin_x


def launch_angle_range(ve_v0, alpha, tol_alpha):

    """
    Compute the minimum and maximum launch angles (in radians)
    for a rocket given the velocity ratio, the target maximum altitude as a fraction of Earth's radius,
    and the tolerance for maxmimum altitude.
    Calls upon the sqrt(x) and arcsin(x) functions defined above.

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
        
        # Compute the square root of the radicand 
        sqrt_radicand = sqrt(radicand)

        # Compute the sine and inverse sine of the launch angles, then store them
        sin_phi = (1 + i) * sqrt_radicand
        
        phi_range.append(arcsin(sin_phi))

    # Return the array of [max_angle, min_angle]
    return np.array(phi_range)


