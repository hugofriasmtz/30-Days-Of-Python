from datetime import datetime

# 1) Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_second = now.second
current_timestamp = now.timestamp()
print("Current components:", current_day, current_month, current_year, current_hour, current_minute, current_second)
print("timestamp", current_timestamp)

# 2) Format the current date using this format: "%m/%d/%Y, %H:%M:%S"
formatted_now = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted now:", formatted_now)

# 3) Today is 15 December, 2025. Change this time string to time.
date_string = "15 December, 2025"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Parsed date_object:", date_object)

# 4) Calculate the time difference between now and new year.
# Next New Year is Jan 1 of next year from 'now'
next_new_year = datetime(year=now.year + 1, month=1, day=1)
time_to_new_year = next_new_year - now
print("Time left for new year:", time_to_new_year)

# 5) Calculate the time difference between 1 January 1970 and now.
epoch_start = datetime(year=1970, month=1, day=1)
time_since_epoch = now - epoch_start
print("Time since 1970-01-01:", time_since_epoch)

# 6) Think, what can you use the datetime module for? Examples
examples = [
	"Time series analysis",
	"To get a timestamp of any activities in an application",
	"Adding posts on a blog"
]
print("Datetime module uses:")
for ex in examples:
	print("-", ex)

