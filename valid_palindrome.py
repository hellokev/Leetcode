class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_isalnum = ''.join(filter(str.isalnum, s))
        rev_str = str_isalnum[::-1]

        if str_isalnum.lower() == rev_str.lower():
            return True
        else:
            return False
