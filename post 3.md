# **POST 3**

## **PROBLEM: UPDATING OF CONTENT IN THE LOCAL REPOSITORY TO THE REPOSITORY ON GITHUB**
I encountered a challenge with laptop when trying to add/update text on github from my local repostory  ussing the terminal.

## SOLUTION
  	
In summary, l discovered that l had to first create a public key locally on my machine and then add it to among the keys on github so that l can access to add, edit/update and push my content to github 


### STEP 1 ( How l created a public key)


To create a public key using the terminal, you can use the ssh-keygen command. Here are the steps:

**Open your terminal.**

Use the following command to generate a new SSH key pair. You will be prompted to provide a location for the key and an optional passphrase.

	bash
	ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

**Explanation of options:**

	-t rsa: Specifies the type of key to create (RSA).
	-b 4096: Specifies the number of bits in the key (4096 bits is recommended for stronger security).
	-C "your_email@example.com": Adds a label/comment to the key, typically your email address.
Press Enter to accept the default file location (usually ~/.ssh/id_rsa) or provide a custom path.

If you want to add a passphrase for extra security, enter a passphrase when prompted. You can also leave it blank if you don't want a passphrase.

**Note:** Even if you leave it blank, it's generally a good idea to use a passphrase for added security.

Once the key pair is generated, you'll see a message indicating the location of the public and private keys.

	vbnet
	
	Your public key has been saved in /path/to/your/home/.ssh/id_rsa.pub.
	Your private key has been saved in /path/to/your/home/.ssh/id_rsa.

Now you have successfully created an SSH key pair. The public key is stored in the file with the .pub extension (e.g., id_rsa.pub). You can share this public key with services like GitHub, GitLab, or others where you need to authenticate using SSH keys. The private key (id_rsa) should be kept secure and not shared.

**To display the content of your public key, you can use the following command:**

	bash
	
	cat ~/.ssh/id_rsa.pub
Copy the output and use it wherever you need to add your public key.


### **STEP 2 ( In this step, l got a copy of the repostory onto my computer by carrying ou git clone)**


To clone a repository from GitHub (or any Git repository) using the terminal, follow these steps:

**Open your terminal.**

Navigate to the directory where you want to clone the repository. For example:

	bash
	
	cd /path/to/destination/directory
Get the clone URL from the GitHub repository, but it is better to use SSH URL

**If you are using SSH, you can use the SSH URL:**

	bash
	
	git clone git@github.com:username/repository.git
 
 ### **STEP 3 ( This is a step where we now send/update our content to the github account )**

 To send content from a cloned repository to GitHub, you'll typically follow these steps:

**Navigate to the Local Repository:**
Open your terminal and navigate to the local directory of the cloned Git repository.

	bash
	
	cd /path/to/cloned/repository
	Check the Status:
It's a good practice to check the status of your local repository to see which files have been modified, added, or deleted.

	bash
	
	git status
	Add and Commit Changes:
If you've made changes to your files, add them to the staging area and commit the changes:

	bash
	
	git add .
	git commit -m "Your commit message here"
	Push Changes to GitHub:

Finally, push your changes to the GitHub repository. If you cloned the repository using HTTPS, you might be prompted to enter your GitHub credentials.

	bash

	git push origin master
 Then you are able to find your content on git hub
	 
	
