class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0

        dic = collections.Counter(nums)
        # print(dic)

        for i in dic:
            if 0 < dic[i] < 2:
                return -1
            while dic[i] != 0:
                # print(dic)
                if (dic[i] % 3 == 0) or ((dic[i]-2 != 0) and ((dic[i]-2) % 3 == 0)):
                    res += int((dic[i]-2) // 3)
                    dic[i] = 2
                    # print('enter 1')
                elif ((dic[i]-4 != 0) and ((dic[i]-4) % 3 == 0)):
                    res += int((dic[i]-4) // 3)
                    dic[i] = 4
                    # print('enter 2')
                elif dic[i] % 2 == 0:
                    res += int(dic[i] // 2)
                    dic[i] = 0
                    # print('enter 3')
                else:
                    # print('enter 4')
                    return -1
                # print(res)
        
        return res