# ml-project

From powershell run
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

--Set virtual env
python -m venv .env

--To activate env
.env\Scripts\Activate

pip install streamlit

--Create requirement file
pip freeze > requirements.txt

--Run app
streamlit run app2.py

--Create image
docker build -t python-cal-app-zar .

docker run -d -p 8000:8501 python-cal-app-zar:latest

docker container ps or ls to see running containers

docker exec -it cont_name bash : for most lionux based images.

docker exec -it cont_name sh : for lightweight images like alpinees.

docker exec -it cdb827b9a5e9 bash
docker stop cont_id
docker rm cont_id

-- Push image to hub
docker login
docker images
docker tag python-cal-app-zar:latest mobeenzar/python-cal-app:v1.0
docker push mobeenzar/python-cal-app:v1.0

To push a local created branch to remote
git push --set-upstream origin feature-branch

