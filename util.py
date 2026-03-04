from datetime import datetime


def get_user_command() -> str:
    user_command = input("Type 'win' to enter a win, 'list' to list your wins. Commands: win | list | exit ").strip().lower()
    return user_command

def get_user_win() -> str:
    user_input = input("What did you do to invest in yourself today? ")
    return user_input

def retrieve_wins_for_listing() -> str | None:
    try:
        with open("my_wins.txt") as f:
            content = f.read()
            return content
    except FileNotFoundError:
        return None
        
def list_wins(content) -> None:
    if content is None or content == "":
        print("No wins written yet")
        return
    print(content)
        
def get_formatted_time() -> str:
    current_time: datetime = datetime.now()
    formatted_time = current_time.strftime("%d.%m.%Y %H:%M") #strftime returns the date as str
    return formatted_time

def merge_time_and_win(formatted_time: str, user_win: str) -> str:
    win_record: str = f"{formatted_time} - {user_win}\n" 
    return win_record

def write_to_file(win_record: str) :
    with open("my_wins.txt", "a") as f:
        f.write(win_record)
        
def print_confirmation_win(user_win):
    print(f"You did this: {user_win}, that's a win for the books.")   