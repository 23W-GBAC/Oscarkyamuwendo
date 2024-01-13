# **AUTOMATION PROJECT**

**This project consist of the journey l went through from scratch to place of producing content that looks more professional and ability to set my machine work with github**

## Table of Contents
 - **[PROBLEM 1: OVER REPEATION OF WRITING FILE PATHS](#installation)**
 - **[PROBLEM 2: ADDITION OF TEXT IN BLOG CONSECUTIVELY WITH USE OF THE TERMINAL](#installation)**
 - **[PROBLEM 3: UPDATING OF CONTENT IN THE LOCAL REPOSITORY TO THE REPOSITORY ON GITHUB](#usage)**


# POST 1 
## **PROBLEM 1: OVER REPEATION OF WRITING FILE PATHS**
   I had a problem of writing file paths which some consisted of long filenames like repositories and this could make me take long time to access a file in a sub folder from other many sub folders 


## SOLUTION
I had to initiate auto completion of file names on my terminal on my mac


### STEP 1: Install a shell and one them is ZSH SHELL
To install Zsh (Z Shell), you can follow these general steps. The process might vary slightly depending on 
     your operating system.

- **For Linux: Ubuntu/Debian-based systems:**
		Open a terminal.

**Run the following command to install Zsh:**

		sudo apt-get update
		sudo apt-get install zsh
	
After installation, you can start Zsh by typing zsh and pressing Enter.

	
- **For macOS:**
Zsh is pre-installed on macOS. You can check the installed version by typing zsh --version in the terminal.

      To start Zsh, simply type zsh and press Enter.

- **For Windows:**
Using Windows Subsystem for Linux (WSL):
If you don't have WSL installed, follow the instructions on the official Microsoft documentation to set up WSL.

Open the terminal in your WSL instance.

Run the following command to install Zsh:

	bash
		Copy code
		sudo apt-get update
		sudo apt-get install zsh
After installation, you can start Zsh by typing zsh and pressing Enter.


During the installation process, make sure to select the zsh package from the package list.

After installation, you can start Zsh by running the Cygwin terminal and typing zsh and pressing Enter.

**Customization (Optional):**
	Once Zsh is installed, you may want to customize it further using frameworks like Oh My Zsh or Prezto.
        These frameworks provide additional features, themes, and plugins. You can find installation instructions 
	on their respective GitHub repositories:

	Oh My Zsh
	Prezto
Keep in mind that the installation steps may change, so it's always a good idea to refer to the official documentation 							or the respective GitHub repositories for the most up-to-date information.

### STEP 2. Install command: (this l did by running the command below on my terminal)
	For Mac
	brew install zsh-autosuggestions

### STEP 3. Activating the auto suggestions
      
	To activate the autosuggestions,l added the following at the end of your .zshrc
	to open .zshrc type vim .zshrc in your terminal

       source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh

### STEP 4. Final step
At last l closed the terminal and opened it again then next was magic happening on my termminal where l got suggestipns of 						commands which had written before and this helped me to save time l would spend on typing 

 
 # POST 2
 ## PROBLEM: ADDITION OF TEXT IN BLOG CONSECUTIVELY WITH USE OF THE TERMINAL
I had to add text in my blog several times but without updating it daily my main blog at the github account

## SOLUTION
  	I used VIM as a tool to help me edit text in my blog and save it locally on my machine several times using 
        the terminal and then push it once on github 
### STEP 1
        I had to first have home brew on my mac and then install then vim respectively following the commands below
	Open Terminal (you can find it using Spotlight with Cmd + Space and typing "Terminal").

If you don't have Homebrew installed, you can install it by running the following command:

      bash
	 "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Once Homebrew is installed, you can install Vim with the following command:

### STEP 2
	bash
	Copy code
	brew install vim
After the installation is complete, you can run Vim by typing vim in the Terminal.

## BASIC COMMANDS OF VIM THAT EASED MY CONTENT CREATION
**Normal Mode:**
	
Default mode for navigation and manipulation.
	- Press Esc to enter Normal Mode.
	Insert Mode:
	
Used for inserting or editing text.
	- Press i in Normal Mode to enter Insert Mode.
	Visual Mode:
		Used for selecting and manipulating text.
	Press v in Normal Mode to enter Visual Mode.
**Navigation:**
	Move cursor:
	h: Move left
	j: Move down
	k: Move up
	l: Move right
**Word-wise navigation:**
	
	w: Move to the beginning of the next word
	b: Move to the beginning of the previous word
	e: Move to the end of the current word
**Line-wise navigation:**
	
	0: Move to the beginning of the line
	^: Move to the first non-blank character of the line
	$: Move to the end of the line
	G: Move to the end of the file
	gg: Move to the beginning of the file
	:<line_number>: Move to a specific line number
	Editing:
**Inserting text:**
	
	Press i to enter Insert Mode before the cursor
	Press I to enter Insert Mode at the beginning of the line
	Press a to enter Insert Mode after the cursor
	Press A to enter Insert Mode at the end of the line
	Press o to open a new line below the current line
	Press O to open a new line above the current line
**Deleting text:**
	
	x: Delete the character under the cursor
	dd: Delete the entire line
	D: Delete from the cursor position to the end of the line
	dw: Delete from the cursor position to the end of the word
	db: Delete from the cursor position to the beginning of the word
	Saving and Quitting:
	Save:
	
	:w: Save changes
**Quit:**
	
	:q: Quit (if no changes were made)
	:q!: Quit without saving changes
	:wq or ZZ: Save and quit
	Visual Mode:
	Selecting text:
	v: Enter Visual Mode (character-wise)
	V: Enter Visual Mode (line-wise)
	Ctrl + v: Enter Visual Mode (block-wise)
	Copy and Paste:
**Copy (yank):**
	
	yy: Copy the current line
	y$: Copy from the cursor position to the end of the line
	yw: Copy from the cursor position to the end of the word
**Cut (delete):**
	
	dd: Cut (delete) the current line
	dw: Cut (delete) from the cursor position to the end of the word
**Paste:**
	
	p: Paste after the cursor
	P: Paste before the cursor
