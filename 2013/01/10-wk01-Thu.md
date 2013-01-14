##toolslearn
 Making Zsh your default shell

If the shell is listed in /etc/shells you can use the chsh command to change your default shell without root access. If you installed Zsh from the official repositories, it should already have an entry in /etc/shells.

Change the default shell for the current user:

    $ chsh -s $(which zsh)

Note: You have to log out and log back in, in order to start using Zsh as your default shell.

After logging back in, you should notice Zsh's prompt, which by default looks different from Bash's. However you can verify that Zsh is the current shell by issuing:

    $ echo $SHELL

Tip: If you are replacing bash, you may want to move some code from ~/.bashrc to ~/.zshrc (e.g. the prompt and the aliases) and from ~/.bash_profile to ~/.zprofile (e.g. the code that starts your X Window System).


##change the font of putty, my the symbol seeable

TODO:
learn the linux trees


##R+RStudio+knitr : used to compile Rmd(md)file
R for statistical computing
R studio for R
knitr for dynamic show infomation

Rmd file can generate the graph and md file.
I can use vim write Rmd file, then use R to generate the html file and md file
then I can use [Pandoc](http://johnmacfarlane.net/pandoc/) change it into letex and use [MikTEX](miktex.org) to transfer to pdf. or latex file is also not aproblem.
and the pdf file can be the final document.


##solved how to share mouse and keyboard in two or more computers
use [Synergy](www.synergy-foss.org)

##writing markdown files in windows use vim is the best
but I can preview the file in markdownpad, and change it into the html file.

##markdown-here is a awesome tool
when use the web editor edit files, I can use the markdown-here to toggle the text into formated article.


##must have my own opinion!!!!!!!
what is better: I can use my own mouse, and I can use zsh
and if close the door, maybe you never lost things, but you will never get things in.
躬自厚而薄责于人，则远怨矣:as now, can only do charge others little, can not afford charge myself.
一以贯之


##multi-markdown
[multi-markdown](http://fletcherpenney.net/multimarkdown/)
