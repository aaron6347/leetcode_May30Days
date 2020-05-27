"""day22_sort_characters_by_frequency.py
    Created by Aaron at 23-May-20"""
class Solution:
    def frequencySort(self, s: str) -> str:
        # app1
        # c1, c2 = Counter(s), {}
        # for k,v in c1.items():
        #     c2.setdefault(v, []).append(k*v)
        # return "".join(["".join(c2[i]) for i in range(len(s), -1, -1) if i in c2])

        # app2
        # s_set = set(s)
        # table = []
        # for val in s_set:
        #     table.append((val, s.count(val)))
        # table.sort(key = lambda x: x[1], reverse = True)
        # return ''.join(map(lambda x: x[0] * x[1], table))

        # app3
        # return "".join([char * times for char, times in collections.Counter(str).most_common()])

        # app4
        result = ''
        bucket = [None for i in range(len(s) + 1)]
        hash_map = {}
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        for key, value in hash_map.items():
            if bucket[value] is None:
                bucket[value] = []
            bucket[value].append(key)
        for i in reversed(range(len(bucket))):
            if bucket[i] is not None:
                for char in bucket[i]:
                    result += char * i
        return result

run=Solution()
a="tree"
print(run.frequencySort(a))
# app1 use Counter to count frequency and then use frequency as key and value with character*value, lastly join all in reversed order of number
# app2 use set to find all character, save tuple of character and frequency in list, sort it in reverse order
# app3 use Counter most_common function to get and sort
# app4 bucket sort