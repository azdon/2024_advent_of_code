import math

# proess input list
def construct_input_lists(path:str):
    input_list_1 = []
    input_list_2 = []

    file = open(path, 'r')
    for line in file:
        
        inputs = line.rstrip().split(" ")

        input_list_1.append(int(inputs[0]))
        input_list_2.append(int(inputs[3]))

    # print(input_list_1)
    # print(input_list_2)

    assert len(input_list_1) == len(input_list_2)
    return input_list_1, input_list_2


def determine_list_distances(input_list_1, input_list_2):
    sorted_list_1 = sorted(input_list_1)
    sorted_list_2 = sorted(input_list_2)
    
    # print(sorted_list_1)
    
    result = []
    for i in range(0, len(sorted_list_1)):
        element_1 = sorted_list_1[i]
        element_2 = sorted_list_2[i]
        
        difference = abs(element_1 - element_2)
        
        # print(f"element 1: {element_1}, element 2: {element_2}, difference: {difference}")
        result.append(difference)
    
    # print(result)
    return result, sorted_list_1, sorted_list_2


def calculate_total_distance(result):
    total_distance = sum(result)
    return total_distance


def calculate_similarity_score(sorted_list_1, sorted_list_2):
    # map of number -> frequency in list 2
    number_frequency_map = {}
    
    # populate unique numbers from list 1 (left list)
    for item in sorted_list_1:
        number_frequency_map[item] = -1
        
    # iterate through both lists to get frequency
    for i in range (0, len(sorted_list_1)):
        number_to_count = sorted_list_1[i]
        counter = 0
        if number_frequency_map[number_to_count] == -1:
            for item in sorted_list_2:
                if item == number_to_count:
                    counter += 1
                    
        number_frequency_map[number_to_count] = counter
        
    # calculate similarity score
    similarity_score = 0
    for num in sorted_list_1:
        num_occurences_in_right_list = number_frequency_map[num]
        subscore = num * num_occurences_in_right_list
        
        similarity_score += subscore
        
    return similarity_score
            
        

def run():
    list1, list2 = construct_input_lists(path='input/input.txt')

    result, sorted_list_1, sorted_list_2 = determine_list_distances(list1, list2)
    
    total_difference = calculate_total_distance(result)
    
    print(f"Total distance is: {total_difference}")
    
    similarity_score = calculate_similarity_score(sorted_list_1, sorted_list_2)
    
    print(f"Similarity score is: {similarity_score}")

run()