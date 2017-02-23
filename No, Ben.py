used_caches = {}
for endpoint in endpoints:
    videos = endpoint.return_video_list()
    caches = endpoint.return_cache_list()
    for video in videos:
        video_in_cache = False
        for cache in caches:
            if video.return_size() <= cache.return_size():
                if cache not in used_caches:
                    used_caches[cache] = video
                else:
                    used_caches[cache].append(video)
                cache.decrement_size(video.return_size())

                break
                    
                    
for i in used_caches.keys():
    output = str(i)
    array = used_caches.get(i)
    for x in array:
        output += " " + str(x)

    print (output)
    
