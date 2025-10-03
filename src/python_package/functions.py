def sqrt(x):
    
    if x > 0 and x < 0.25:
        a = 0, sqrt_a = 0
    elif x >= 0.25 and x < 0.75:
        a = 0.5, sqrt_a = 0.70710678
    elif x >= 0.75 and x < 1.25:
        a = 1, sqrt_a = 1
    elif x >= 1.25 and x < 1.75: 
        a = 1.5, sqrt_a = 1.22474487
    elif x >= 1.75 and x < 2.25:
        a = 2, sqrt_a = 1.41421356
    elif x >= 2.25 and x <= 2.5:
        a = 2.5, sqrt_a = 1.58113883
    else:
        raise ValueError("Input must be between 0 and 2.5")
    
    for k in range(1, 20):
        
        fact_k = 1

        for i in range(2, k + 1):
            fact_k *=i 
            
        for j in range(1, k):

            if k == 1:
                prod_k = 1
            else:
                prod_k *= (-0.5 * ((2 * j) - 1))

        coef_k = 0.5 * prod_k / fact_k

        term_k = ((x - a) ** k) / (sqrt_a ** ((2 * k) - 1)) * coef_k

        sum_k += term_k

        sqrt_x = sqrt_a + sum_k

    return sqrt_x

    #use and if statement to check if x is between 0 and 2.5 --> values outside that range should result in an error
    #use taylow series

def arcsin(x):
    
    for n in range(1, 20):

        fact_2n = 1

        for i in range(1, n + 1):
            fact_2n *= 2 * i

        fact_n = 1

        for j in range(1, n + 1):
            fact_n *= j

        denom_n = (n ** 2) * (fact_2n / (fact_n **2))

        numer_n = (2 * x) ** (2 * n)

        term_n = numer_n / denom_n

        sum_n += term_n

        arcsin_x = sum_n * 0.5

    return arcsin_x

# series only converges for a limeted range of values, so output is from 0 to sqrt(2.5). T series will not converge at every point, so we can use base points.
# hard code in these base values for a. Ex. from 0 to 0.75, 0.5 is used (put into 0.5 bins). Therefore the distance between x and a is less than 0.5. So a^0.5 = .... for each of the base values


    )