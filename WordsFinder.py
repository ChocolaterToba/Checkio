def checkio(text, words):
    # Creating a list of all searched words.
    words = [word.lower() for word in words.split(' ') if word]
    text = text.split(' ')
    for a, part in enumerate(text):
        tags = []
        # Searching for word in parts of the text.
        for word in words:
            for i in range(len(part)):
                if part[i:].lower().startswith(word.lower()):
                    tags += [[i, i + len(word)]]
        if tags:
            if len(tags) > 1:
                # Merging tags together so there is no nesting.
                for i in range(len(tags) - 1):
                    for s in range(len(tags)):
                        if tags[s] and tags[i] and s != i:
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
            # Placing tags in parts of the text
            for tag in sorted([item for item in tags if item])[::-1]:
                part = (part[:tag[0]] + '<span>' +
                        part[tag[0]:tag[1]] + '</span>' +
                        part[tag[1]:])
            text[a] = part
    return ' '.join(text)
print(checkio("aaaa", "aa a"))