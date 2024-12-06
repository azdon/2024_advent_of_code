
safe_limits = [1, 2, 3]

with open('input/input.txt', 'r') as file:
    
    safe_count = 0
    
    for line in file:
        values = line.split()
        
        safe = True
        increasing = False
        decreasing = False
        
        for i in range(0, len(values) - 1):
            first_val = int(values[i])
            second_val = int(values[i + 1])
            
            if i == 0:
                # Checking if inc or dec
                if first_val > second_val:
                    increasing = True
                
                elif first_val < second_val:
                    decreasing = True
                    
                else:
                    safe = False
                    
                if abs(first_val - second_val) not in safe_limits:
                    safe = False
                
            elif i > 0:
                if first_val == second_val:
                    safe = False 
                
                # Checking if next breaks pattern
                if decreasing and first_val > second_val:
                    safe = False
                
                if increasing and first_val < second_val:
                    safe = False
                    
                if abs(first_val - second_val) not in safe_limits:
                    safe = False
            
        if safe:
            safe_count += 1
            
        print(f'values: {values} are safe: {safe}')
            
        increasing = False
        decreasing = False
        safe = True
            
    print(f"Safe count: {safe_count}")
            
        