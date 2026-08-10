class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        j = 0
        i = 0
        temp = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                else:
                    temp = 0
                    while j < len(abbr) and abbr[j].isdigit():
                        temp = temp*10 + int(abbr[j])
                        j+=1
                    
                i += temp

            else:
                if word[i] != abbr[j]:
                    return False
                
                i+=1
                j+=1
        
        return i == len(word) and j == len(abbr)
