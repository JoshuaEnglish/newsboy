"""offsite.py

Interface for Dropbox and potentially other off-site storage
"""

import dropbox
import os
import code

with open(os.path.expanduser("~/.dropbox_token"), "r") as fp:
    DROPBOX_ACCESS_TOKEN = fp.read()

dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
for entry in dbx.files_list_folder('').entries:
    print(entry.name)

code.interact('Dropbox Playground', local={'d': dbx})
