from azure.communication.email import EmailClient
from dotenv import load_dotenv
import os


class EmailSender:
    def __init__(self, message, subject_line):
        self.message = message
        self.subject_line = subject_line

    def send_email(self):
        response = False
        load_dotenv()

        try:
            connection_string = os.getenv("CONNECTION_STRING")
            client = EmailClient.from_connection_string(connection_string)

            email_message = {
                "senderAddress": os.getenv("SENDER_EMAIL"),
                "recipients": {
                    "to": [{"address": os.getenv("RECIPIENT_EMAILS")}],
                },
                "content": {
                    "subject": self.subject_line,
                    "html": self.format_message_to_html(),
                }
            }

            poller = client.begin_send(email_message)
            result = poller.result()
            response = True

        except Exception as ex:
            print(ex)

        return response

    def format_message_to_html(self) -> str:
        message_board = self.message
        html_content = "<html><body style=\"color: purple;\"><table>"

        for row in message_board:
            for i in range(len(row["columns"])):
                html_content += "<tr>"
                for grid in row["columns"]:
                    for value_in_row_of_grid in grid[i]:
                        html_content += f"<td>{value_in_row_of_grid}</td>"
                html_content += "</tr>"

        html_content += "</table></body></html>"
        return html_content
