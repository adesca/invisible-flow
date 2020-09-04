#  Invisible Flow 

This project aids in the process of data entry and tracking for the Citizens Police Data Project (CPDP), an initiative of the Invisible Institute. The [CPDP](https://cpdp.co/) is an interactive data tool for holding police accountable to the public they serve.
  
This tool cleans and stores data that is scraped from the Civilian Office of Police Accountability ([COPA](https://www.chicagocopa.org/about-copa/mission-history/)) API, which houses all allegations against the Chicago Police Department.


## Local environment setup
To set up this project on your local machine, please follow the rest of this document step by step.

### Install docker
##### Mac or Windows
[Download Docker here](https://www.docker.com/products/docker). 

**[ Note ]** Docker for Windows only supports Windows 10. If you have an earlier version of Windows you'll need to install  [docker toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/)  instead.
##### Linux
On Linux, run  `apt-get install docker`. 

### Install PyCharm
We recommend using PyCharm for your IDE. 
[Download PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac).

### Frontend Setup
Once you've cloned the repository, run the following from your local project folder:
  

      cd frontend
      npm install
  

Let **npm** do its thing. Once complete run:

      npm run build

To make sure that the frontend built successfully, check the `frontend` directory for a new folder named `build` and note that it also updates the `node_modules` folder.

### Download CPDP Database
The `cpdp-apr-5-2019.sql` file is a copy of the CPDP database. It is a large file that can be used to initialize a database locally.

 1. Download the .sql file from this [Dropbox link](https://www.dropbox.com/s/riixbrze6apmcrn/cpdp-apr-5-2019.sql?dl=0).
 2. Place it somewhere you will remember it outside of the project folder.


### Build app with docker

Once the above steps are complete, return to your project's root directory `invisible-flow` and run in your terminal:

    docker build -t invisible_flow:latest .

### Run app locally with docker
The following command can be run as is from the project root directory (i.e. `invisible-flow` - note the dash not underscore) or by replacing `"$(pwd)"` with the absolute path to said directory.

    docker run -t -i -p5000:5000 -e PORT=5000 -v "$(pwd):/app/" invisible_flow:latest

**Note**: When run locally this project outputs `.csv` files to the `invisible-flow/invisible_flow/local_upload` directory.


#### Check if the app is running correctly
 1. When the app is running locally, open `http://0.0.0.0:5000/` in a browser to view.
 2. Click **Initiate Scrape**. This should update the database with data from COPA and may take a few minutes to complete.
 3. After the scape finishes, check that the `invisible_flow_testing` database in the docker container was updated by doing the following:


        docker ps
    
Copy the `CONTAINER ID` from the output of that command (i.e., `274ff13bc055`) and run:
    
	    docker exec -it <INSERT_CONTAINER_ID> bash
	
Something like this will show up in your terminal: 

	    postgres@274ff13bc055:/app$

From there you can access the database running inside of the current docker container by entering: 
	 
	    psql invisible_flow_testing

Try querying:
		
        SELECT * FROM data_officerallegation;
If you see a populated table, you should be all set up!

There are several bash functions included in this project to make running the above commands easier. Run `source scripts` to load them into the current terminal session or add them to your `bashrc` to have them loaded universally.

### Flask Database Migrations 
1. Make desired change to the SQLAlchemy models in `invisible_flow/copa`.    
    
2. Follow the steps in the previous section to enter your locally running Docker container, then change into the `invisible_flow` directory: `cd invisible_flow`.  
  
3. To generate a migration file, run the following command in the container with a descriptive filename:  `flask db migrate -m '<desired_name_of_new_migration_file>'` 

4. A new migration file named after the message above and prepended with a hash string will appear in the `invisible_flow/migrations/versions` directory. (i.e., `99asldjrqwo_desired_name_of_new_migration_files_.py`)    
    
5. The entity changes you implemented earlier should appear in the `upgrade()` function in the new migration file.     
    
6. **IMPORTANT** Look over the autogenerated file to make sure it is correct. Sometimes Flask doesn't pick up on all changes (especially type changes).    
    
7. Once the file is in a good place return to your locally running Docker container and apply the changes by running `flask db upgrade` or rebuilding the container.   
    
8. Open up your local database to check that your desired changes worked.    
    
9. **IMPORTANT** Commit the file along with other code changes.


### Tests 
##### Running Backend Tests:  
Backend tests should be run while the app is running locally. Open up a new terminal window and execute:

    docker ps
    
Copy the `CONTAINER ID` from the output of that command (i.e., `274ff13bc055`) and run:
    
	docker exec -it <INSERT_CONTAINER_ID> bash
	
Something like this will show up in your terminal:

    postgres@274ff13bc055:/app$  

You can then run: 

    pytest tests  
      
  
To run the tests with a certain test focused, mark the focused test with `@pytest.mark.focus` and then run `pytest tests -m focus` in the running instance of your docker container.

##### Running Frontend Tests:  
* To run the tests execute `npm run test`

### Help

 If you need help with anything, feel free to contact a team member.
