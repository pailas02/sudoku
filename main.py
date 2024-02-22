from flask import Flask, request, jsonify
from SudokuSolution import Sudoku
from EmailSend import EmailSender

app = Flask(__name__)
data_send_email = {
    'message': None,
    'subject': "Sudoku board is loaded"
}


@app.route('/sudoku', methods=['POST'])
def sudoku():
    board_info = request.get_json()
    sudoku = Sudoku()
    sudoku.set_board(board_info["board"])

    if sudoku.check_elements(board_info):
        response = {
            "message": "Number can fit"
        }
        if sudoku.join_number(board_info):
            response["message"] = "Number filled in"
            board_info = sudoku.get_info_position()
            data_send_email['message'] = board_info["board"]
            response["message"] = notification(data_send_email)
    else:
        response = {
            "message": "El dato no se puede ubicar, cambie de posición"
        }
    return jsonify(response), 400 if response["message"] == "Number can't fit" else 200


def notification(data_send_email):
    azure = EmailSender(data_send_email['message'], data_send_email['subject'])
    if azure.send_email():
        response = {
            "message": "envio de "
        }
    return response


if __name__ == '__main__':
    app.run(debug=True)
