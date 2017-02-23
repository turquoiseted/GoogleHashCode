



def main(filename):

    file = open(filename, 'r')
    main_file = file.readlines()

    temp_array = []
    temp_number = ""
    for x in range(len(main_file[0])):
        if (main_file[0][x] == " ") or (x == (len(main_file[0])-1)):
            temp_array.append(temp_number)
            temp_number = ""
        else:
            temp_number += main_file[0][x]

    videos = int(temp_array[0])
    endpoints = int(temp_array[1])
    request_descriptions = int(temp_array[2])
    caches = int(temp_array[3])
    size = int(temp_array[4])

    for x in range(len(main_file[1])):
        if (main_file[1][x] == " ") or (x == (len(main_file[0])-1)):
            temp_array.append(temp_number)
            temp_number = ""
        else:
            temp_number += main_file[1][x]

    videos_sizes = temp_array

    cache_dictionary = {}
    counter = 2
    for endpoint in range(endpoints):
        for x in range(len(main_file[counter])):
            if (main_file[counter][x] == " ") or (x == (len(main_file[0])-1)):
                temp_array.append(temp_number)
                temp_number = ""
            else:
                temp_number += main_file[counter][x]
        endpoint_name = temp_array[0]
        counter += 1
        for cache in range(len(temp_array[1])):
            for x in range(len(main_file[counter])):
                if (main_file[counter][x] == " ") or (x == (len(main_file[0])-1)):
                    temp_array.append(temp_number)
                    temp_number = ""
                else:
                    temp_number += main_file[counter][x]
            counter += 1
            cache_dictionary[temp_array[0]] = temp_array[1]
    requests = []
    for lines in range(counter, len(main_file)):
        for x in range(len(main_file[lines])):
            if (main_file[lines][x] == " ") or (x == (len(main_file[0])-1)):
                temp_array.append(temp_number)
                temp_number = ""
            else:
                temp_number += main_file[lines][x]

            counter += 1
            info_video = temp_array[0]
            info_endpoint = temp_array[1]
            info_requests = temp_array[2]


main('C:/Users/Dmitri/Documents/GitHub/GoogleHashCode/kittens.in')