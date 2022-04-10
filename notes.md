<!-- ! OS File Structure -->

/ is the root directory

folders are in a hierarchy (a tree)

Files and diretories have <!--!absolute paths
based on the root where each additional level down adds a '/'. <!--!Example /User/bek/Desktop

<!--% The green -->

directory below is a special directory called 'home', which is also known as '~'Tilde. This is the default directory upon open your terminal.

<!--@ PWD (print working directory-->

PWD will tell you the full absolute path of where you are at!

<!--@ CD (Change directory) -->

followed by the <!--$absolute path-->
of the folder will navigate you directly there. Example cd /Users/bek will get me to my bek folder from where ever I am.

<!--@ The dot '.'-->

stands for current directory and dot-dot '..' stands for parent directory. This allows for <!--@ relative navigation-->
'..' dot-dot take you back to the last level.

<!--@ ls stand for 'list'-->

The keyword 'ls' will 'list' the contents of a directory. You can supply options such as '-a' to list all files (including hidden ones), or '-l' for a longer format.

<!--@ mkdir ('make directory'-->

The command 'mkdir' followed by the name of the new directory will create a new child directory inside the current directory. The child

<!--@ 'touch' creates new files-->

The command 'touch' followed by the filename and file-type extension will create a new file of that type.

example: touch favs.txt

<!--@ 'mv' moves or renames files-->

Files can be moved or renamed using the 'mv'('move') keyword, which takes two arguments: the source and the destination.

<!--$ 'rm'removes files files-->

When its gone its gone!!

<!--$ 'rm -rf'removes directories files-->

Directories can also be deleted using the 'rm' keyword, with the added option '-r'('recursive'). You can also use '-f' ('force') to prevent warnings.

<!--# example: rm -rf 'directory'

<!--% Dynamic Typing -->

Python is highly flexible about reassigning variables to different types: boolean to a string to a number to none. This is called dynamic typing since variables can change easily. Other languages like C++, are statically-typed and variables are stuck with their originally-assigned type.
