import math, sys

input = sys.stdin.read()

def ball_game(input):
    input_list = input.splitlines()
    input_list.pop(0)
    player_list_of_lists = []
    
    for item in input_list:
        new_list = item.split()
        player_list_of_lists.append([new_list[0], int(new_list[1]), int(new_list[2])])
    
    for list in player_list_of_lists:
        
        number = int(math.sqrt(sum(((list[1] - list[2])**2, (list[2] - list[2])**2))))
        list.append(number)
    
    nested_lst_of_tuples = [tuple(l) for l in player_list_of_lists]
    
    merge_sort(nested_lst_of_tuples,3)
   
    return_string = ""
    
    for tuples in nested_lst_of_tuples:
        return_string += tuples[0] + "\n"
  
    return return_string
        
def merge_sort(list,index):         

    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        merge_sort(left,index)      
        merge_sort(right,index)       
        a = 0
        b = 0
        c = 0

        while a < len(left) and b < len(right):
            if left[a][index] < right[b][index]:   
                list[c] = left[a]
                a += 1
            else:
                list[c] = right[b]
                b += 1
            c += 1
        while a < len(left):
            list[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            list[c] = right[b]
            b += 1
            c += 1


 
  
print(ball_game(input))
