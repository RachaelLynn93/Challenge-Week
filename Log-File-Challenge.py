import datetime
def log_activity(message):
    # 1. Get the current date and time
    # .strftime() formats it so it looks clean, e.g., "2026-04-01 15:30:00"
    current_time = datetime.datetime.now() .strftime("%Y-%m-%d %H:%M:%S:")
    
    # 2. Format the exact string we want to write to the file
    # The \n at the end acts as an invisible "Enter" key to start a new line
    log_entry 
    = f"[{current_time}] {message}\n"
    
    # 3. Open the file in 'a' (append) mode
    # 'a' ensures we add to the bottom of the file instead of erasing what's already there 
    with open("challenge_log.txt", "a") as log_file:
        log_file.write(log_entry)
        
    print(f"Logged successfully: {message}")
    
# --- Testing the Function with your actual progress! ---

# A list of the specific challenges we tackled
completed_tasks = [
    "Mastered string slicing: Reverse a String",
    "Applied regex and normalization: Palindrome Checker",
    "Built a manual loop algoritm: Find the Max Number", 
    "Used modulo math for divisibility: Prime Number Checker",
    "Handled ASCII wrap-around logic: Ceasar Cipher Encoder",
    "Validated user input with flags: Password Strength Checker"
]

# Loop through our list and log each one
for task in completed_tasks:
    log_activity(task)
    
# Optional: Adding a custom manual entry at the end
user_note = input("\nEnter a custom log note (or press Enter to skip): ")
if user_note:
    log_activity(f"User Note: {user_note}")
    