def bingo(selections, boards):
    return None


class BingoBoard:
    def __init__(self, numbers):
        self.rows = numbers
        self.columns = self._create_columns(numbers)

    @staticmethod
    def _create_columns(rows):
        columns = []
        for i in range(len(rows)):
            columns.append([])
            for j in range(len(rows[0])):
                columns[i].append(rows[j][i])
        return columns
