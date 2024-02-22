class Sudoku:

    def __init__(self):
        self.board = []
        self.info_position = {}

    def check_elements(self, info_position):

        info = {
            "row": info_position["row"], "square": info_position["square"],
            "row_square": self.get_fila_cuadricula(info_position["position"]),
            "position_row_square": self.get_position_fila_cuadricula(info_position["position"]),
            "value": info_position["value"]
        }

        right_column = self.elements_in_columns(info)

        right_row = self.elements_in_row(info)

        right_square = self.elements_in_square(info)

        return right_column and right_row and right_square

    def elements_in_columns(self, info_position):

        right_column = True

        for row in self.board:
            for column_position in range(len(row["columns"])):
                if column_position == info_position["square"]:
                    for row_column in row["columns"][column_position]:
                        if row_column[info_position["position_row_square"]] == info_position["value"]:
                            right_column = False
        return right_column

    def elements_in_row(self, info_position):

        right_row = True

        for row in self.board:
            if row["row"] == info_position["row"]:
                for column in row["columns"]:
                    for element in column[info_position["row_square"]]:
                        if element == info_position["value"]: right_row = False

        return right_row

    def elements_in_square(self, info_position):

        right_square = True

        for row in self.board:
            if row["row"] == info_position["row"]:
                for column_position in range(len(row["columns"])):
                    if column_position == info_position["square"]:
                        for row_column in row["columns"][column_position]:
                            for element in row_column:
                                if element == info_position["value"]: right_square = False
        return right_square


    def join_number(self, info_position) -> object:
        info = {
            "row": info_position["row"], "square": info_position["square"],
            "row_square": self.get_fila_cuadricula(info_position["position"]),
            "position_row_square": self.get_position_fila_cuadricula(info_position["position"]),
            "value": info_position["value"], "board": info_position["board"]
        }
        is_correct = False
        try:
            for row in info["board"]:
                if row["row"] == info["row"]:
                    row["columns"][info["square"]][info["row_square"]][info["position_row_square"]] = info["value"]

            info_position["board"] = info["board"]
            self.info_position = info_position
            is_correct = True
        except Exception as ex:
            print(ex)
        return is_correct

    def set_board(self, board):
        self.board = board

    def get_info_position(self):
        return self.info_position

    def get_fila_cuadricula(self, position):
        return position // 3

    def get_position_fila_cuadricula(self, position):
        return position % 3

