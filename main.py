class Video:
    def __init__(self, name, size):
        self._name = name
        self._size = size

    def return_name(self):
        return self._name

    def return_size(self):
        return self._size

class Cache:
    def __init__ (self, size):
        self._videoList = []
        self._size = size

    def add_video(self, video):
        self._videoList.append(video)

    def check_for_video(self,video):
        for i0 in range(len(self._videoList)):
            if self._videoList[i0].returnName()==video.returnName:
               return True
        return False

    def return_size(self):
        return self._size

    def decrement_size(self,number):
        self._size-=self._size-number


class EndPoint:
    def __init__(self,latency):
        self._cacheDict={}
        self._cacheList=[]
        self._videoList=[]
        self._videoRequests={}
        self._latency=latency

    def add_cache(self, cache, latency):
        for i0 in range(len(self._cacheList)):
            if self._cacheDict[self._cacheList[i0]]>latency:
                for i1 in range(len(self._cacheList),i0):
                    self._cacheList[i1+1]=self._cacheList[i1]
                self._cacheList[i0]=cache
                break
        self._cacheDict[cache]=latency

    def add_video(self,video,requests):
        for i0 in range(len(self._cacheList)):
            if self._videoDict[self._videoList[i0]]<requests:
                for i1 in range(len(self._videoList),i0):
                    self._videoList[i1+1]=self._videoList[i1]
                self._cacheList[i0]=video
                break
        self._videoRequests[video]=requests

    def return_total_latency(self):
        latency=0
        for i0 in self._videoList:
            if self.returnLatency(i0)!=-1:
                latency+= self.returnLatency(i0)
            else:
                latency+=self._latency
        return latency

    def return_latency(self, video):
        lowest=-1
        for i0 in range(len(self._cacheList)):
            if self._cacheList[i0].checkForVideo(video):
                if lowest==-1:
                    lowest=self._cacheDict[self._cacheList[i0]]
                elif lowest>=self._cacheDict[self._cacheList[i0]]:
                    lowest=self._cacheDict[self._cacheList[i0]]
        return lowest

class World :
    def __init__(self,cacheList,videoList,endPointList):
        self._cacheList=cacheList
        self._videoList=videoList
        self._endPointList=endPointList


    def return_cache_list(self):
        return self._cacheList

    def return_video_list(self):
        return self._videoList

    def return_endpoint_list(self):
        return self._endPointList


def data_parser(filename):
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

    temp_array = []
    counter = 2

    endpoint_array = []
    for endpoint in range(endpoints):
        for x in range(len(main_file[counter])):
            if (main_file[counter][x] == " ") or (x == (len(main_file[counter])-1)):
                temp_array.append(temp_number)
                temp_number = ""
            else:
                temp_number += main_file[counter][x]

        endpoint_array.append(EndPoint(temp_array[1]))
        counter += 1
        temp_array_2 = []
        for cache in range(int(temp_array[1])):
            for x in range(len(main_file[counter])):
                if (main_file[counter][x] == " ") or (x == (len(main_file[counter])-1)):
                    temp_array_2.append(temp_number)
                    temp_number = ""
                else:
                    temp_number += main_file[counter][x]
            counter += 1
            endpoint_array[endpoint].add_cache(temp_array_2[0], temp_array_2[1])

        temp_array = []

    for lines in range(counter+1, len(main_file)):
        for x in range(len(main_file[lines])):
            if (main_file[lines][x] == " ") or (x == (len(main_file[lines])-1)):
                temp_array.append(temp_number)
                temp_number = ""
            else:
                temp_number += main_file[lines][x]

        endpoint_array[int(temp_array[1])].add_video(temp_array[0], temp_array[2])
        temp_array = []
    world = World(cache_array, video_array, endpoint_array)
    return world


data_parser('C:/Users/Dmitri/Documents/GitHub/GoogleHashCode/me_at_the_zoo.in')