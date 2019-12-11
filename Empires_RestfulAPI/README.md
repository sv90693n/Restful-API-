#RESTful webservice using Docker

Created a RESTful Web service that displays data of empires in JSON format using two get routes: 
   
* /empires
   
* /empires/{empireid}

* /empires/{empireId}/army

* /empires/{empireid}/army/{armyid}
    
Steps to run RESTful web service:

* Create the project with myapp.py and JSON file in a single folder.
  The templates folder consists of the page.html file which displays the json result on the webpage

* A Docker Image is created by running the following command: -
 "docker build -t empires-image:latest ."

* You can check the image created using "docker images". You will find the image students-image under the list.

* Run the created students-image image inside a container using the following command
  "docker run -d -p 5000:5000 --name empires-container empires-image" 

* Check running docker container by "docker ps"

* App will now be running at the following urls: -
  http://<host_ip_address>:5000

  http://<host_ip_address>:5000/empires

  http://<host_ip_address>:5000/empires/101 --- 101 is the id you wish to search

* http://<host_ip_address>:5000/empires/101/army

* http://<host_ip_address>:5000/empires/101/army/101

* For data in json format: -
* http://<host_ip_address>:5000/empires?type=json

* http://<host_ip_address>:5000/empires/101?type=json

* http://<host_ip_address>:5000/empires/101/army?type=json

* http://<host_ip_address>:5000/empires/101/army/101?type=json
