# **AUTOMATION PROJECT**

**This project consist of the journey l went through from scratch to place of producing content that looks more professional and ability to set my machine work with github**

## Table of Contents

 - **[PROBLEM 1: OVER REPEATION OF WRITING FILE PATHS](#installation)**
   
 - **[PROBLEM 2: ADDITION OF TEXT IN BLOG CONSECUTIVELY WITH USE OF THE TERMINAL](https://github.com/23W-GBAC/Oscarkyamuwendo/blob/main/post%202.md)**
   
 - **[PROBLEM 3: UPDATING OF CONTENT IN THE LOCAL REPOSITORY TO THE REPOSITORY ON GITHUB](https://github.com/23W-GBAC/Oscarkyamuwendo/blob/main/post%203.md)**


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

 

