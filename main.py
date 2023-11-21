import os
import yagmail
from time import sleep
from dotenv import load_dotenv

load_dotenv()
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

print("\033[1;33m" + "[Info] Send E-mails Automatically" + "\033[0m")
print("\033[1;33m" + "  ||   Sending Bulk Mail Using A Text File" + "\033[0m" + "\n")
def sending_of_mails(file_name: str, document: str) -> str:
    """This function takes a mailing list from a text file and sends an attachment with default content"""
    with open(f"{file_name}.txt") as file:
        EMAILS = [EMAIL.rstrip() for EMAIL in file]
    for COUNTER, ITEMS in enumerate(EMAILS):
        receiver = ITEMS
        body = "EDIT FOR CONVENIENCE"
        filename = f"{document}.pdf"

        try:
            yag = yagmail.SMTP(MY_EMAIL, PASSWORD)
            yag.send(
                to=receiver,
                subject="EDIT FOR CONVENIENCE",
                contents=body,
                attachments=filename,
            )
            print(
                "\033[0;32m" + f"☑️ Successful Delivery! -> {COUNTER + 1}" + "\033[0m"
            )
            sleep(3)

        except Exception as ex:
            print("\033[0;31m" + str(ex) + "\033[0m")
    return "\033[0;34m" + "Operation Completed!" + "\033[0m"


if __name__ == "__main__":
    print(sending_of_mails("emails", "YOUR_ATTACHED_DOCUMENT"))
