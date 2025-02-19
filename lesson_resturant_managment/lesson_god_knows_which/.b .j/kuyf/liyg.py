def copmuterPower( x, y):
    
    result = 1
    
    while (y > 0):
        if (y%2 == 1):
            result = result * x
        
        else:
            result = result * x
            y = y - 1
        
        return result
    x = int(input("Enter x for x^y :"))
    y = int(input("Enter y for x^y :"))
    print("total : ",(coputerPower(x, y)))
      
      