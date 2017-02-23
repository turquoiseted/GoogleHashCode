
from classes from Video

def main(filename, video_name):
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

    cache_array = []
    for cs in range(caches):
        cache_array.append(Cache(size))


    for x in range(len(main_file[1])):
        if (main_file[1][x] == " ") or (x == (len(main_file[0])-1)):
            temp_array.append(temp_number)
            temp_number = ""
        else:
            temp_number += main_file[1][x]

    # store video data into an array of video class
    video_array = []
    for video in range(videos):
        video_array.append(Video(video, temp_array[video]))

    
    cache_dictionary = {}
    counter = 2

    endpoint_array = []
    for endpoint in range(endpoints):
        for x in range(len(main_file[counter])):
            if (main_file[counter][x] == " ") or (x == (len(main_file[0])-1)):
                temp_array.append(temp_number)
                temp_number = ""
            else:
                temp_number += main_file[counter][x]

        endpoint_array.append(Endpoint(temp_array[1]))

        counter += 1
        for cache in range(len(temp_array[1])):
            for x in range(len(main_file[counter])):
                if (main_file[counter][x] == " ") or (x == (len(main_file[0])-1)):
                    temp_array.append(temp_number)
                    temp_number = ""
                else:
                    temp_number += main_file[counter][x]
            counter += 1

            endpoint_array[endpoint].add_cache(temp_array[0], temp_array[1])


    requests = []
    for lines in range(counter, len(main_file)):
        for x in range(len(main_file[lines])):
            if (main_file[lines][x] == " ") or (x == (len(main_file[0])-1)):
                temp_array.append(temp_number)
                temp_number = ""
            else:
                temp_number += main_file[lines][x]

            counter += 1
            endpoint_array[temp_array[1]].add_video(temp_array[0],temp_array[2])
           


main('C:/Users/Dmitri/Documents/GitHub/GoogleHashCode/kittens.in', "Kittens_video")