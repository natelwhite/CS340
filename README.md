# Animal Shelter Database Dashboard
- This project was created to simplify the task of finding rescue animals within a database. 
# Necessary Installs
- [Python 3.6+](https://www.python.org/downloads/)
- [Jupyter Notebook Interface](https://docs.jupyter.org/en/stable/install/notebook-classic.html)
- [MongoDB](https://www.mongodb.com/docs/manual/installation/)
# Getting Started
- Clone this repository and then import the data for MongoDB:
	- This data comes from The Austin Animal Center located in Austin, Texas: [DOI](https://doi.org/10.26000/025.000001)
	- Note that the environment variables: `MONGO_USER`, `MONGO_PASS`, `MONGO_PORT`, and `MONGO_HOST` must be set accordingly before running this command as-is.
```bash
git clone https://github.com/nlwhite/CS340.git
cd CS340
mongoimport --username="${MONGO_USER}" --password="${MONGO_PASS}" \
--port=${MONGO_PORT} --host=${MONGO_HOST} \
--db=AAC  --collection=animals --authenticationDatabase=admin \
--file=./aac_shelter_outcomes.csv --type=csv --headerline
```
- To start the application, open the Jupyter Notebook and click 'Run'.
- If the app started successfully, the exact http address is printed near the bottom.
	- This url may be accessed by any computer logged into the same wifi as the computer that ran the application. Please ensure the wifi is secure and cannot be accessed by unknown users.
	- By default, the application is launched on port 33229. If this port is already in use, either change the port (line 25 of the Jupyter Notebook) or end the process currently running on that port. 
# Usage
- When first loading the page, the user is greeted with:
	- a datatable that holds 1000 records,
	- a pie-chart with sectors of animal breeds,
	- and an interactive map that indicates where the first animal in the database is located.
- The user has three radio buttons to their disposal for filtering the animal data. These are the types of rescue animals as profiled by Grazioso Salvare. The exact filtering criterion is outlined as follows:
	- Water
		- Breeds: Labrador Retriever Mix, Chesapeake Bay Retriever, Newfoundland
		- Sex: Intact Female
		- Age: 26-156 weeks
	- Mountain/Wilderness
		- Breeds: German Shepherd, Alaskan Malamute, Old English Sheepdog, Siberian Husky, Rottweiler
		- Sex: Intact Male
		- Age: 26-156 weeks
	- Disaster/Individual Tracking
		- Breeds: Doberman Pinscher, German Shepherd, Golden Retriever, Bloodhound, Rottweiler
		- Sex: Intact Male
		- Age: 20-300 weeks
- Lastly, there is one last button for removing the filters named, 'Reset'
