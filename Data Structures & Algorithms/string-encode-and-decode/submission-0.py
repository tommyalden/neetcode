class Solution:
    def encode(self, strs: List[str]) -> str:
        output = ''
    
        for string in strs: output += string + '.,.'
        return output

    def decode(self, s: str) -> List[str]:
        return s.split('.,.')[0:-1]
