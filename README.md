# KnxhxMobility
Submission to Knoxville Hackathon 2019


This folder includes files:
CSS: contains the files that decorate our websites.
Data: contains the potholes and garage data files that we used to train our models and develop our algorithms.
Garage: contains the webpage for garage occupation and prediction.
Images: used as martials to build the webpage.
Php: contains the page to link frontside via ajax and backside running python script.
Potholes: contains the webpage for reporting potholes.
Python: 1.py is just for test. Do not open it. dynamic Scheduling is the algorism we developed to address the path scheduling problems. Loadmodel.py is the file that we used to call our model “model.pkl”, which is pretrained using machine learning algorithms.
 

We choose the Mobility, including pothole and parking, as our project for the Knoxville City Hackathon. We design and implement both the pothole and parking using web-based applications.

The whole system works as follow:

We firstly design a home webpage that provides the portals to pothole and the parking services. A normal user could visit the home webpage using a browser through the Internet. 

For the parking service, the client (customer) will be able to see the real-time usage (including vacancy) of four garages. \textbf{Moreover, our system will also provide the estimation of future garage usage}. This will help customers planning their visits to all the areas with reliable reference information.

For the pothole service, there are two use cases for both the customer who reports a pothole and the drivers who will fix the pothole. To report a pothole, the information of location, potholes size, customer contact and a picture (can be used for deep learning in the future) is needed. Our system also provides a dynamic scheduling scheme for the fixing team, which is used to minimize the overall cost that all the reported potholes will cause.

•	Technique details:

Parking:

Our system used linear regression to predict garage usage information in the future. The features that were considered for prediction are garage location, weekday (weekend or not), and history garage vacancy information. With this system, the customer will be able to get the predicated garage usage information of a certain time in the future.

Potholes:

The features that considered for dynamic scheduling are location, pothole size, report date, and the times that a pothole being reported. We assume the more a pothole being reported, the heavier traffic there are near the pothole, and the cost for one pothole will be the during (from reported to fixed) multiply the traffic volume. And the overall cost of a scheduling system will be the sum of all pothole’s cost under that system. We use a greedy algorithm to find the optimal schedule for the drivers to fix the potholes.


