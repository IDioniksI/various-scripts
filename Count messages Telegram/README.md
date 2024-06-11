## The script counts the number of messages in the telegram dialog
### <center>Brief instructions</center>
The script counts the number of messages in the telegram dialog

To execute the script, you must first export the dialog in .json format, this can be done in the official
Telegram Desktop application (go to the dialog -> three dots -> export chat history -> in the window, 
select the json format (all checkmarks can be removed) ). Next, in the script, you need to write the path to our file in
the "file_path" variable, most of all it will be called result.json, and then just run the script, and the result will 
be displayed in the terminal.
The main goal is to count the number of messages sent by a certain person, in addition, it will count how many of these 
messages were voice messages, as well as stickers