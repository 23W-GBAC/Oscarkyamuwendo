 # POST 2
 ## **PROBLEM: ADDITION OF TEXT IN BLOG CONSECUTIVELY WITH USE OF THE TERMINAL**
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
	**Insert Mode:**
	
Used for inserting or editing text.
	- Press i in Normal Mode to enter Insert Mode.
	**Visual Mode:**
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
