# CTFd API endpoint
HOST = "http://xxxxx:7000/"

# CTFd API token
API_TOKEN = "ctfd_ad730c2aa781b24501ac790bc5aa4"

# How frequently to check for new solves
POLL_PERIOD = 10

TELE_TOKEN  = ""

CHAT_ID = ""

# Available template variables are:
# User Name (if individual mode) / Team Name (if team mode): {user_name}
# Challenge Name: {chal_name}
FIRST_BLOOD_ANNOUNCE_STRING = "🔪🩸 First Blood for challenge *{chal_name}* goes to *{user_name}*! {emojis}"

# To be used with announce_all_solves
SOLVE_ANNOUNCE_STRING = "🍻 *{user_name}* just solved *{chal_name}*! {emojis}"

# Whether or not to announce all solves as well as first bloods
ANNOUNCE_ALL_SOLVES = True

# Category Emojis (if any)
CATEGORY_EMOJIS = {
    "web": [":globe_with_meridians:"],
    "crypto": [":sob::closed_lock_with_key:"],
    "pwn": [":bug:"],
    "rev": [":rewind:"],
    "forensics": [":mag:"],
    "osint": [":detective:"],
    "blockchain": [":white_large_square::chains:"],
    "misc": [":jigsaw:"],
}
