names = ['John', 'Kenny', 'Tom', 'Bob', 'Dilan']

## CREATE YOUR FUNCTION HERE
def sort_names(names): 
    #muta array original
    names.sort()
    
    return names

print(sort_names(names))
