# ezdw

Version 1

# User Usage

To install something download the .ez file the have created.

Then run the command `sudo ezdw path/to/<file>`

It will then ask you whether you really want to download it and then install it to your system

# Developer Usage

ezdw allows you to set up single file installs.
All you have to do is create a .ez file to allow downloading your app

Creating a .ez
-

The thing you need within the file are as follows. It is case sensitive

 - A name `Name-<name>`
 
 - A version `Version-<version>`
 
 - A license `License-<license, name or link>`
 
 - A main file `Link/to/<file> -main <what it shtould name the file>`
 
 - Other files `Link/to/<file> -f <what it should name the file>`
 
Example .ez
```
Name-tCalc
Version-1.2
License-None
https://raw.githubusercontent.com/dawson270500/tCalc/master/calc -main calc
https://raw.githubusercontent.com/dawson270500/tCalc/master/calc.py -f calc.py
```
SPACES DO MATTER, NO SPACES IN NAME, VERSION OR LICENSE.

What is a 'main' file: This is the file that becomes the command you run, this can really be any format. Its name is the command they run to start it

If you have files other than your main file, they will be in `/usr/src/ezdw/<App Name>`
