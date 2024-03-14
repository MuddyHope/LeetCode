class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ""
        length = len(digits)
        for i in digits:
            res += str(i)
        res=int(res)
        print(res)
        res += 1
        res=str(res)
        final_list = []
        for i in res:
            final_list.append(int(i))
        return final_list