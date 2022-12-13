



from algs.insertion_sort import insertion

def bucket_sort(data, drawdata, speed):
    # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket 
    max_value = max(data)
    size = max_value/len(data)

    # Create n empty buckets where n is equal to the length of the input list
    buckets_list= []
    for x in range(len(data)):
        buckets_list.append([]) 

    # Put list elements into different buckets based on the size
    for i in range(len(data)):
        j = int (data[i] / size)
        if j != len (data):
            buckets_list[j].append(data[i])
        else:
            buckets_list[len(data) - 1].append(data[i])

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(data)):
        insertion(buckets_list[z],drawdata,speed)
        print(buckets_list)
            
    