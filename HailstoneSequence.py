def hailstone(a):
    n = int(a)
    count = 0
    while n > 1:
        if n % 2 == 0:
            N = n /2
            print(N)
            n = N
            count += 1
        else:
            B = 3 * n + 1
            print(B)
            n = B
            count += 1
    print("It has gone over the loop ",count," times.")
        
         