# DataAnalyticsPipeline_ImageRepair

## Environment preparation

-1. Start a new conda environment. The following steps will all be executed in this new conda environment.

-2. RUN >> pip install -r requirements.txt

-3. Install Kafka on your local computer 

-4. Start the kafka service on your local computer. Then, create a topic named "TutorialTopic" for our project. This Kafka topic will be used by our producer and consumers. You could follow this office guide (https://kafka.apache.org/quickstart) 

-5. Set up your local config.ini file. Firstly, copy config_example.ini to config.ini. Then set up your secret variable value in config.ini file.  

## RUN the application

-1. Start a terminal, go to PROJECT_FOLDER/tornado, and RUN >> python main.py, to start our tornado web service.

-2. Start a new terminal, go to PROJECT_FOLDER/database_service, and RUN >> python history.py, to start our history table service.

-3. [TODO] Start a new terminal, go to PROJECT_FOLDER/model_service, and RUN >> python model_service.py, to start our model service.

-4. Start a new terminal, go to PROJECT_FOLDER/test, and RUN >> python test_frontend.py, to fake a HTTP POST request with the image data from the frontend to backend, and tornado will process the POST request.

## Close up 

-1. Close your Kafka service
