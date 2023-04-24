import dqn
import a2c
import ppo

def get_user_choice():
    print("Please choose which script you'd like to run:")
    print("1. DQN")
    print("2. A2C")
    print("3. PPO")
    choice = input("Enter the number of your choice: ")
    return int(choice)

def run_selected_script(choice):
    if choice == 1:
        dqn.main()
    elif choice == 2:
        a2c.main()
    elif choice == 3:
        ppo.main()
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    user_choice = get_user_choice()
    run_selected_script(user_choice)