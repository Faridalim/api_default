#!/bin/bash

# SETTING

App_folder="api_default"
Git_url="https://github.com/Faridalim/api_default.git"
Port=8000
Name_container="${App_folder}_container"

# DONT CHANGE BELOW IF NOT NECESSARY

echo  "Deploy Start. Bismillah."
echo  ">> $App_folder <<"
echo  "1. Git Pull"
cd $App_folder
git pull origin main
echo  "2. Build Docker Images"
docker build -t $App_folder ./
echo  "3. Stop and Delete Old Container"
docker stop $Name_container && docker rm $Name_container
echo  "3. Run Container"
docker run -d --name $Name_container -p $Port:80 $App_folder
echo  "Alhamdulillah. Build Finished."
