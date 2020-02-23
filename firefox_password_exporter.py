import pyautogui
import time
import clipboard
from math import floor

# Collect all the user input
n_items_str = input('1. Enter the number of passwords: ')
n_items = int(n_items_str)

n_items_visible_str = input('2. Enter the number of items visible at a time: ')
n_items_visible = int(n_items_visible_str)

_ = input('3. Mouse over "First Item Location" and press the ENTER key:')
first_item_location = pyautogui.position()
print("Saved (%d, %d)" % first_item_location)

_ = input('4. Mouse over "Last Item Location" and press the ENTER key:')
last_item_location = pyautogui.position()
print("Saved (%d, %d)" % last_item_location)

_ = input('5. Mouse over "Info Location" and press the ENTER key:')
info_location = pyautogui.position()
print("Saved (%d, %d)" % info_location)

_ = input('6. Mouse over "Website Location" and press the ENTER key:')
website_location = pyautogui.position()
print("Saved (%d, %d)" % website_location)

_ = input('7. Mouse over "Username Copy Button Location" and press the ENTER key:')
username_location = pyautogui.position()
print("Saved (%d, %d)" % username_location)

_ = input('8. Mouse over "Password Copy Button Location" and press the ENTER key:')
password_location = pyautogui.position()
print("Saved (%d, %d)" % password_location)

# Ask before starting the job since it will take over the mouse
eta_total_secs = 2.6 * n_items # 2.6 is just the number of sleeps per entry added together
eta_mins = floor(eta_total_secs / 60)
eta_secs = eta_total_secs % 60
eta_str = '%dm %ds' % (eta_mins, eta_secs) if eta_mins else '%ds' % (eta_secs)
response_str = input("Start collecting %d passwords? Minimum ETA: %s (Y/n): " % (n_items, eta_str))
if response_str in ('n','N'):
	print('Exiting...')
	import sys
	sys.exit()

# This is constant even if firefox is zoomed. 
# Can be found by inspecting the html on the logins page in case it changes later.
scroll_amount = 61

# Now switch the focus to the firefox window for execution
pyautogui.click(first_item_location)

# Open output csv file, add a header line
f = open('firefox_auto_export.csv','w+')
f.write('info,website,username,password\n')

def copy_visible_entry():
	# Triple click to select all for the info string
	pyautogui.click(info_location)
	pyautogui.click(info_location)
	pyautogui.click(info_location)
	time.sleep(0.1)
	pyautogui.hotkey('ctrl','c')
	time.sleep(0.5)
	info = clipboard.paste()
	info = info.strip() # Remove leading and trialing whitespace
	
	# Right click and select all to copy website without visiting url
	pyautogui.rightClick(website_location)
	pyautogui.hotkey('shift','a')
	pyautogui.hotkey('ctrl','c')
	time.sleep(0.5)
	website = clipboard.paste()
	website = website.strip() # Remove leading and trialing whitespace
	
	# Left click the Username Copy button
	pyautogui.click(username_location)
	time.sleep(0.5)
	username = clipboard.paste()

	# Left click the Password Copy button
	pyautogui.click(password_location)
	time.sleep(0.5)
	password = clipboard.paste()

	# Print the parsed information to the command line to report status
	print('----')
	print(info)
	print(website)
	print(username,':', '*'*len(password)) # Mask out password so not printed in plaintext to command line

	# Append the entry to the csv file
	line = ','.join([info, website, username, password]) + '\n'
	f.write(line)

# Do all the first items scrolling down each time
for i in range(n_items - n_items_visible):
	pyautogui.click(first_item_location)
	copy_visible_entry()
	pyautogui.click(first_item_location) # To put the focus back in the menu for scrolling
	pyautogui.scroll(-scroll_amount)
	time.sleep(0.5)
	
# Do the remaining visible items by incrementing the y value of the item location
pixels_per_item = (last_item_location[1] - first_item_location[1]) / (n_items_visible-1)
for item_offset in range(n_items_visible):
	item_location = (first_item_location[0], first_item_location[1] + item_offset*pixels_per_item)
	pyautogui.click(item_location)
	copy_visible_entry()
	time.sleep(0.5)
	print(item_offset)

print('All done!')
# Close output file on completition
f.close()