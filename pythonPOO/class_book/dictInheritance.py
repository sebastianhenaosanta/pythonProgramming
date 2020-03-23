class LongNameDict(dict):
    def longest_key(self):
        longest = None
        print(len(longest))
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest
    

    
        