class employee():
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("destructor called")
def create_obj():
    print("creating object...")
    obj1=employee()
    print("funtion end...")
    return obj1
print("Calling create_object() function...")
obj1=create_obj()
print("program end...")
