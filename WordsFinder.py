def checkio(text, words):
    words = [word.lower() for word in sorted(words.split(' '), key = len)
             if word]
    text = text.split(' ')
    for a, part in enumerate(text):
        tags = []
        for i, word in enumerate(words):
            if word.lower() in part.lower():
                index = part.lower().find(word)
                tags += [[index, index + len(word)]]
        if tags:
            if len(tags) > 1:
                for i in range(len(tags) - 1):
                    for s in range(i + 1, len(tags)):
                        if tags[s] and tags[i]:
                            print(tags[i], tags[s])
                            if ((tags[i][0] <= tags[s][0] and
                                 tags[i][1] >= tags[s][1])):
                                tags[s] = 0
                            elif (tags[i][0] >= tags[s][0] and
                                  tags[i][1] <= tags[s][1]):
                                tags[i] = tags[s][:]
                                tags[s] = 0
                            elif tags[i][1] in range(tags[s][0] + 1, tags[s][1]):
                                tags[i][1] = tags[s][1]
                                tags[s] = 0
                            elif tags[i][0] in range(tags[s][0], tags[s][1]):
                                tags[i][0] = tags[s][0]
                                tags[s] = 0
            for tag in sorted([item for item in tags if item])[::-1]:
                part = (part[:tag[0]] + '<span>' +
                        part[tag[0]:tag[1]] + '</span>' +
                        part[tag[1]:])
            text[a] = part
    return ' '.join(text)
print(checkio("aaaa", "aa a"))