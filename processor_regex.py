import re

def classify_with_regex(log_message):
    regex_patterns = {
      r"User (User\d+|\d+) logged (in|out)": "User Action",
      r"Backup (started|ended) at .*": "System Notification",
      r"Backup completed successfully.": "System Notification",
      r"Backup failed with error: .*": "System Notification",
      r"System updated to version .*": "System Notification",
      r"Disk cleanup completed successfully.": "System Notification",
      r"Disk cleanup failed with error: .*": "System Notification",
      r"System reboot initiated.": "System Notification",
      r"System shutdown initiated.": "System Notification",
      r"System update initiated.": "System Notification",
      r"Account with ID .* created by .*": "User Action",
      r"Account with ID .* deleted by .*": "User Action",
      r"Account with ID .* updated by .*": "User Action",
      r"Account with ID .* locked by .*": "User Action",
      r"Account with ID .* unlocked by .*": "User Action",
      r"Account with ID .* disabled by .*": "User Action",
      r"Account with ID .* enabled by .*": "User Action",
      r"Account with ID .* added to group .* by .*": "User Action",
      r"Account with ID .* removed from group .* by .*": "User Action",
      r"Account with ID .* added to role .* by .*": "User Action",
      r"Account with ID .* removed from role .* by .*": "User Action",
      r"Account with ID .* added to policy .* by .*": "User Action",
      r"Account with ID .* removed from policy .* by .*": "User Action"
  }

    for pattern, label in regex_patterns.items():

      if re.search(pattern, log_message, re.IGNORECASE):

        return label

    return None

if __name__ == "__main__":
    print(classify_with_regex("User User123 logged in."))