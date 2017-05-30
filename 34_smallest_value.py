smallest_value = None
print 'BEFORE processing : ',smallest_value
for value in [9,2,4,6,8,5,9,3,7,1,0.3,2,0.01,0.5]:
    # Here, "is" is the replica of "=="
    if smallest_value is None:
        smallest_value = value
    elif value < smallest_value:
        smallest_value = value
    print smallest_value, value
print 'AFTER processing : ',smallest_value
