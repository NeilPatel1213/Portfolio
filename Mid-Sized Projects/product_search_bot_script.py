#Application that takes a subreddit and a product name as GUI inputs and searches for mentions of that product,
#outputting some information about the mention to the desired file

import praw
import PySimpleGUI as sg
import time

#creating the Reddit instance
reddit = praw.Reddit(
    client_id="eBzQjB7cgLDnrpCVkDyCNQ",
    client_secret="YuriJbjJfz-eTNN0WtXMdT30oDIu0A",
    user_agent="<console:READER:1.0",
)

#subreddit decided by GUI input
subreddit_input = sg.popup_get_text("Enter the subreddit you want to search in")

#product decided by GUI input
product_input = sg.popup_get_text("Enter the product you want to search for")

subreddit = reddit.subreddit(subreddit_input) 

#filename to output to decided by GUI input
file_input = sg.popup_get_file("Enter the file to write output to")

file = open(file_input, "a")
file.write("\nSearching in r/" + subreddit_input + " for " + product_input + "\n")
file.write("**********************************************************************************\n")

i = 0 # a variable to count for loops in order to have a progress bar

for submission in subreddit.hot(limit=10):
    sg.one_line_progress_meter("Searching Posts...", i, 5, orientation='h')
    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if product_input in comment_lower:
                file.write("\n" + comment.body)
                file.write("-")
                file.write("written by u/" + str(comment.author) + "\n")
                file.write("-------------------------------------------------------------------------\n")
    i = i + 1




