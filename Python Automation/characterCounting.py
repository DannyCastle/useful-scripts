import pprint

message = 'The quick brown fox jumped over the lazy dog.'
count = {}

for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1

pprint.pprint(count)
