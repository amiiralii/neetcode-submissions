class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def col_extractor(board):
            for i in range(len(board)):
                yield [row[i] for row in board]
        
        def sq_extractor(board):
            for i in range(0, len(board), 3):
                sq, sq1, sq2 = [],[],[]
                for row in board[i:i+3]:
                    sq.append(row[0])
                    sq.append(row[1])
                    sq.append(row[2])

                    sq1.append(row[3])
                    sq1.append(row[4])
                    sq1.append(row[5])

                    sq2.append(row[6])
                    sq2.append(row[7])
                    sq2.append(row[8])
                yield sq
                yield sq1
                yield sq2

        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for d in digits:
            for row in board:
                if row.count(d) > 1:
                    return False
            for col in col_extractor(board):
                if col.count(d) > 1:
                    return False
            for sq in sq_extractor(board):
                if sq.count(d) > 1:
                    return False
        return True
        