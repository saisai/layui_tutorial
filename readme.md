

https://stackoverflow.com/questions/49016255/django-display-contents-of-txt-file-on-the-website


…or create a new repository on the command line
echo "# layui_tutorial" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/saisai/layui_tutorial.git
git push -u origin main
                
…or push an existing repository from the command line
git remote add origin https://github.com/saisai/layui_tutorial.git
git branch -M main
git push -u origin main
…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.

 git push --set-upstream origin main
 


django-admin startproject mysite .

python manage.py startapp layui

python manage.py runserver 0.0.0.0:82


python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser


'charmap' codec can't decode byte 0x9d in position 164: character maps to <undefined>
file = open(filename, encoding="utf8")	
https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character

https://stackoverflow.com/questions/28218174/current-directory-os-getcwd-from-within-django-determined-how
