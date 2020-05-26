# smarthealth-server

## Initial setup

In Git Bash navigate to the project diractory:

```
pip3 install virtualenv             # install virtualenv
virtualenv venv                     # setup a new virtual environment called venv
source venv/Scripts/activate        # activate the new environment
pip3 install -r requirements.txt    # install dependencies
```


## Run 

```
python app.py
```

In the browser navigate to `http://127.0.0.1:5000/` to see the "Hello, world!" message.


## Development

1. Always develop within the virtual environment
2. If you add any new dependencies, make sure to add them to the requirements.txt. You could use `pip freeze > requirements.txt`, not only if you are in the virtual environment, otherwise it will write every package you have installed globally.
3. Basic Git workflow:

    `git status` to see your changed files and in what stage they are.

    Once you have changes you wish to push to the server (aka ready with a ticket) use...

    `git add filename` to add changed/new files to git.  
    `git commit -m "commit message"` to commit added changes to the local HEAD. Try to write a meaningful commit message explaining your changes. This might also include the ticket number.  
    `git pull` to pull and merge any new changes from the server. If you miss this step you changes might overwrite something on the server. So don't!  
    `git push` to push the changes to the server.  

 If you use git in the IDE follow the same workflow.