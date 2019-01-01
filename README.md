curl -u 'akif05' https://api.github.com/user/repos -d '{"name":"modern_python"}'
echo "# modern_python" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/akif05/modern_python.git
git push -u origin master

