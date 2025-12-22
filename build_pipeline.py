# Write a function:
# build_pipeline(operation_names)
# where operation_names is a list of strings.
# The function must return a new function that applies a sequence of operations to a single input value,in the given order.
# Each string in operation_names represents an operation
# If an unknown operation name is encountered, an error must be raised.
# Calling the returned function should apply all operations sequentially and return the final result.


def build_pipeline(operation_names):
    
    def double(x):
        return x * 2
    def square(x):
        return x * x
    def triple(x):
        return x * 3
    
    operations = {
        "double": double,
        "square": square,
        "triple": triple 
        }
    
    for name in operation_names:
        if name not in operations:
            raise KeyError(f"Unknown operation: {name}")
    
    def pipeline(value):
        result = value
        
        for name in operation_names:
            result = operations[name](result)
        
        return result
    return pipeline 

pipeline_1 = build_pipeline(["double", "triple", "square"])
print(pipeline_1(3)) 

other_pipeline = build_pipeline(["square", "double"])
print(other_pipeline(2))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
