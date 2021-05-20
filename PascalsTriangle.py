class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        
        ourList = [[], []]
        ourList[0] = [1]
        ourList[1] = [1, 1]

        
        for i in range(1, numRows - 1):

            ourList.append([]) # create another empty list
            nxt = i + 1

            ourList[nxt].append(1)
            p = 1

            for j in range(i):
                ourList[nxt].append(ourList[i][j] + ourList[i][p])
                p += 1

            ourList[nxt].append(1)

        return ourList                
                
       
