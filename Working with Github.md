##  Using Obsidian Git for the tech unfamiliar (minimal command line usage)

### Creating an account

Make an account at [github.com](https://github.com/). Create an empty repository.

![[Images/attachments/Pasted image 20221103125806.png]]

### Software installation

Install [git for windows](https://git-scm.com/download/win). 

When installing, make sure to enable the command line PATH, otherwise obsidian git has no means of accessing and automating the backup for you.

![[Images/attachments/Pasted image 20221103125922.png]]

Check if git was installed successfully by opening the command line interface [windows+r , `cmd`, enter ] and inputting `git` and pressing enter.

If successful, it should output something like this.

![[Images/attachments/Pasted image 20221103125937.png]]

If this doesn't appear, refer to [fixing path](Fixing%20PATH.md).

Afterwards, install [github desktop](https://desktop.github.com/). We'll be using github desktop to set up the repository as well as manage credentials.

### Cloning the repository and setting up your credentials
Once in github desktop, select File > Options > Account, and log in to your github account.

![[Images/attachments/Pasted image 20221103130021.png]]

Now, press File > Clone Repository, and select the empty repository you just created. Where you clone this repository doesn't matter, as long as you remember its location.

In the top toolbar once again, select Repository > Open in Command Prompt. Paste `git config --global credential.helper wincred` and press enter. That should set up your credentials.

### Viewing hidden files
In explorer:

- Select View > Options > Change folder and search options.

- Select the View tab and, in Advanced settings, select Show hidden files, folders, and drives and OK.

![[Images/attachments/Pasted image 20221103130030.png]]

### Installing Obsidian.md

Obsidian is not required to edit the files as they are all just markdown files. There are some custom pieces that only work inside of obsidian, but they can be editted in normal markdown as well.

To install Obsidian.md, download installer from [here](https://obsidian.md/), once downloaded follow the installation instructions.

When you first open Obsidian it will ask you if you have a vault already or if you wish to create one. At this time you will want to tell it you have a vault already and to select the repo you downloaded previously as your vault. upon doing so it should just open right up for you.

### Installing the Obsidian Git plugin

Disable safe mode in the community plugins tab if you haven't already. Browse the community plugins and search for `Obsidian Git`. Install and enable it. Open the command palette (ctrl+p) and type `git`, and select commit and push all changes. If this tutorial was followed successfully, you should have received a notification that you just successfully committed and pushed files.

In the obsidian git plugin options, you can set a backup interval, to determine how often automatic backups are made. You can still use the above method to guarantee that important changes are definitely pushed to github however.

If you're accessing your vault through git across multiple devices, the github desktop application can be useful to resolve conflicts, but is otherwise no longer needed, as the obsidian git plugin will have automated the committing and pushing process.