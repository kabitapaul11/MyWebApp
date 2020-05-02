
### Deploying simple Flask app through Google App Engine
**Bike sharing - Prediction of casual riders**
**Team Members**
- Kabita Paul
- Zach Serapin
- Edward Park 
- Jeremiah Canty


### Steps
- Create github repo
- clone it to your Google Cloud Console project  git clone [[ssh path]]
- run main.py python file. python main.py
- view in browser
- deploy app $ gcloud app deploy
- Browse app $ gcloud app browse
- you can view logs with this command $ gcloud app logs tail -s default 
- Install Locust load testthrough cli command $ sudo python3 -m pip install locustio
- Run locust load test $locust
- Run Locoust in cli. command : $ locust -f locustfile.py --no-web --host https://flask-gae-ml-autoscale-273601.uc.r.appspot.com -c 10 -r 1
