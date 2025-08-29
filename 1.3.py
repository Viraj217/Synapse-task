import numpy as np

def solve():
    mat = np.array([
            [1,0,0,0,1],
            [1,0,1,1,1],
            [1,1,0,1,1],
            [1,0,1,1,0],
            [0,1,0,1,1]
        ])
    
    m = int(input("Enter an odd number less than or equal to 5: "))
    rows, cols = mat.shape
    frow, fcolumn = 0, 0
    maxi = 0

    for i in range(rows - m + 1):      
        for j in range(cols - 2):  
            sub_mat = mat[i:i+m, j:j+m]   
            total = np.sum(sub_mat)       
            maxi = max(total,maxi)
            if maxi == total:
                frow = rows - ((2*i + m - 1) / 2)
                fcolumn = cols - ((2*j + m - 1) / 2)

    print(maxi)
    print(f"row = {frow}")
    print(f"column = {fcolumn}")
     
solve()