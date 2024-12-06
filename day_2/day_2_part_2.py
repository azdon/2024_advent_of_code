
safe_limits = [1, 2, 3]

            
def identify_safe_with_1_level_tolerance(values):
    
    safe_count = 0
        
    safe = True
    increasing = False
    decreasing = False
    
    for i in range(0, len(values) - 1):
        first_val = int(values[i])
        second_val = int(values[i + 1])
        
        if i == 0:
            # Checking if inc or dec
            if first_val > second_val:
                decreasing = True
            
            elif first_val < second_val:
                increasing = True
                
            else:
                safe = False
                
            if abs(first_val - second_val) not in safe_limits:
                safe = False
            
        elif i > 0:
            if first_val == second_val:
                safe = False 
            
            # Checking if next breaks pattern
            if increasing and first_val > second_val:
                safe = False
            
            if decreasing and first_val < second_val:
                safe = False
                
            if abs(first_val - second_val) not in safe_limits:
                safe = False
        
    return safe

def parse_lists():
    with open('input/input.txt', 'r') as file:
        safe_count = 0
        for line in file:
            values = line.split()
            at_least_one_sublist_safe = False
            
            for i in range(0, len(values)):
                new_list = list(values)
                new_list.pop(i)
                safe = identify_safe_with_1_level_tolerance(new_list)
                
                print(f"Sublist {new_list} of {values} is safe: {safe}")
                
                if safe:
                    at_least_one_sublist_safe = True
            
            if at_least_one_sublist_safe:
                safe_count +=1
                print(f"Values {values} have at least 1 safe sublist: {at_least_one_sublist_safe}")
                
    return safe_count
            
def run():
    safe_count = parse_lists()
    print(f"Safe count: {safe_count}")
    
run()