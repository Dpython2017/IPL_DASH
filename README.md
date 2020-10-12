# IPL DASHBOARD BACKEND
This is the backend of the dashboard forthe IPL website
Following are the endpoints  available 


 1. You can find top 4 winning teams here: "http://127.0.0.1:8000/match/?season=2016",
 2. Team that won most number of tosses:   "http://127.0.0.1:8000/toss/?season=2016",
 3. Player won maximum Player of the match:"http://127.0.0.1:8000/player-match-api/?season=2016",
 4. Max mattces won by team: "http://127.0.0.1:8000/max-match-api/",
 5. % decided to bat when they won the toss: http://127.0.0.1:8000/bating-api/?season=2016 , 
 6. Highest margin run : "http://127.0.0.1:8000/highest-margin-api/?season=2016",
 7. Highest wicket : "http://127.0.0.1:8000/highest-wicket-api/?season=2016", 
 8. Won toss and won match "http://127.0.0.1:8000/toss-winner/",
 9. location-api : "http://127.0.0.1:8000/location-api/?season=2016",
 
 ## Run the project
 * Clone the project
 * Create virtualenv 
 ```virtualenv venv```
 * Activate the environment
 ``` source venv/bin/activate``` on Mac
 ```venv\Scripts\activate``` on Windows
 * Install dependencies
 ``` pip install -r requirements.txt ```
 * Migrate the db
 ``` python manage.py migrate```
 * Run server
 ``` python manage.py runserver ```
