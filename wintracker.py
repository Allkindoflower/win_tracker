from logger import log
import util
import time

 
def main():
    while True:
        user_command = util.get_user_command()
        if user_command == "win":
            user_win = util.get_user_win()
            #log("Fetched win")
            formatted_time = util.get_formatted_time()
            #log("Fetched time")
            win_record = util.merge_time_and_win(formatted_time, user_win)
            #log("Constructed win with timestamp")
            util.write_to_file(win_record)
            #log("Written to file")
            util.print_confirmation_win(user_win)
            #log("Win confirmed!")
        elif user_command == "list":
            content = util.retrieve_wins_for_listing()
            #log("Fetched contents")
            util.list_wins(content)
            #log("Wins listed!")
        elif user_command == "exit":
            print("See you soon!")
            time.sleep(1)
            raise SystemExit(0)
        else:
            print("I don't understand that command.")
      
main()

    
