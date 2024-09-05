target = int(input("Enter a target ="))
def find_combinations(target):
    combinations = ['9']
    
    while True:
        new_combinations = []
        
        for i in combinations:
            number = int(i)
            print(number)
            
            if number % target == 0:
                print(number,"is divisible by",target)
                return
            
            new_combinations.append(i + '0')
            new_combinations.append(i + '9')
        
        combinations = new_combinations

find_combinations(target)
