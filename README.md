# GM-Assignment
This chatbot is designed to tell the capital and population of various countries. 

# Inside it
It consists of following files

data/nlu.yml contains training examples for the NLU model
data/stories.yml contains training stories for the Core model
actions.py contains the implementation of a custom FormAction
config.yml contains the model configuration
domain.yml contains the domain of the assistant
# How to use
It can run on local host or connected with rasa-x or other channels like facebook, telegram or any website
You can test the example using the following steps:

Train a Rasa model containing the Rasa NLU and Rasa Core models by running:

rasa train

The model will be stored in the /models directory as a zipped file.

Run an instance of duckling on port 8000 by either running the docker command

docker run -p 8000:8000 rasa/duckling


or installing duckling directly on your machine and starting the server.

Test the assistant by running:

rasa run actions&
rasa shell -m models --endpoints endpoints.yml
