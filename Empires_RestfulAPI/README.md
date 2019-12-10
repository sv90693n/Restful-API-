#RESTful webservice using Docker

Created a RESTful Web service that displays data of empires in JSON format using two get routes: 
   
* /empires
   
* /empires/empireId
    
Steps to run RESTful web service:

* Create the project with myapp.py and JSON file in a single folder.
  The templates folder consists of the page.html file which displays the json result on the webpage

* A Docker Image is created by running the following command: -
 "docker build -t empires-image:latest ."

* You can check the image created using "docker images". You will find the image students-image under the list.

* Run the created students-image image inside a container using the following command
  "docker run -d -p 5001:5000 --name empires-container empires-image" 

* Check running docker container by "docker ps"

* App will now be running at the following address: -
  http://0.0.0.0:5000/empires
  
* For specific Id use the following url
  http://0.0.0.0:5000/empires/101 --- 101 is the id you wish to search

* http://0.0.0.0:5000/empires/101/army

* http://0.0.0.0:5000/empires/101/army/101
