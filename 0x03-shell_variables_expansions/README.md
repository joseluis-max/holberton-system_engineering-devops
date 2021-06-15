### Shell Variables and expansions
- Alias : `alias newNama=command`
- USER : `echo "hello $USER"
- PATH : `PATH=$PATH:/action`
- PATHS : `echo $PATH | tr ":" "\n" | wc -l
- GLOBALS VARIABLES : `printenv`
- LOCALS VARIABLES : `set`
- Create local variable :`BETTY:Holberton`
- Create global variable : `export HOLBERTON:Betty`
- Addition : ` echo $(( 128 + $TRUEKNOWLEDGE))`