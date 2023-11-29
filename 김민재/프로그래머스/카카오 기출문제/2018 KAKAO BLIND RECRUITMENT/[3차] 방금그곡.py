def convert_time(time):
    H, M = int(time[:2]), int(time[3:])
    return H*60 + M

memo = {
    'C#':'K', 
    'D#':'L', 
    'F#':'M', 
    'G#':'N', 
    'A#':'O', 
}

def convert_note(string):
    final = ''
    i = 0
    while i < len(string):
        if i < len(string)-1 and string[i+1]=='#':
            note = string[i] + string[i+1]
            final += memo.get(note, note)
            i += 2
        else:
            final += string[i]
            i += 1
            
    return final

def solution(m, musicinfos):
    m = convert_note(m)
    
    musics = []
    for info in musicinfos:
        info = info.split(sep=',')
        start, end = convert_time(info[0]), convert_time(info[1])
        if start > end:
            end = 24*60
        title = info[2]
        string = info[3]
        string = convert_note(info[3])
        musics.append([start, end, title, string])

    result = []
    for music in musics:
        start, end, title, string = music
        end = min(24*60, end)
        length = end-start
        total_music = ''
        i = 0
        for t in range(start, end):
            i %= len(string)
            total_music += (string[i])       
            i+=1
        if m in total_music:
            result.append((-length, start, title))
    
    result.sort()
    
    return result[0][2] if result else "(None)"