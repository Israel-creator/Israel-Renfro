Project 1


About the Project/Project Title
This project provides a Python module for creating, reading, updating, and deleting documents in a MongoDB database using object-oriented programming. The module encapsulates MongoDB CRUD operations and makes it easy for other Python scripts to import and reuse the functionality. The database we are using is the same as used in module 3.

Also, the purpose of this project is to develop software for Grazioso Salvare, which is an innovative rescue-animal training company. The motivation behind this project is to increase and grow the company’s ability to find dogs that are available for adoption.

This project involves creating an interactive dashboard for Grazioso Salvare, an international rescue-animal training company, to visualize the Austin Animal Center Outcomes data set. The dashboard includes the following functionalities:
Interactive Filtering Options: Users can filter the data based on rescue types.
Dynamic Data Table: The data table updates based on the selected filter and supports features like sorting and pagination.
Geolocation Chart: Displays the location of selected animals on a map.
Additional Chart: A pie chart shows the distribution of animal breeds.

Functionality
The dashboard provides the following features:
1.	Interactive Filters: Dropdown menu to filter data by rescue type (Water Rescue, Mountain or Wilderness Rescue, Disaster or Individual Tracking).
2.	Data Table: Displays filtered data, allows sorting and pagination, and highlights selected columns.
3.	Geolocation Map: Shows the location of the selected animal.
4.	Pie Chart: Visualizes the distribution of animal breeds.
Screenshots
 
Starting State: 
 
 

 
Water Rescue Filter: 
 
Mountain or Wilderness Rescue Filter: 
 
 
Disaster or Individual Tracking Filter: 
 
Reset State:
 

 
Project Implementation
Step-by-Step Process
1.	Data Retrieval:
o	Utilized a CRUD Python module to connect to the MongoDB database and retrieve data.
o	Transformed the retrieved data into a Pandas DataFrame for easy manipulation.
2.	Dashboard Layout:
o	Set up the JupyterDash instance and defined the layout, including the logo, filters, data table, and charts.
3.	Interactive Components:
o	Implemented a dropdown menu for filtering data based on rescue types.
o	Configured the data table to update dynamically based on the selected filter.
4.	Visualization:
o	Created a pie chart to visualize the distribution of animal breeds.
o	Implemented a geolocation map to show the location of selected animals.
5.	Callbacks:
o	Defined callbacks to link interactive components, ensuring the data table and charts update based on user interactions.
6.	Testing and Deployment:
o	Ran the Jupyter notebook to test the functionality of the dashboard.
o	Took screenshots to document the different states of the dashboard.
Challenges and Solutions
1.	Handling MongoDB ObjectIDs:
o	Issue: The _id field returned by MongoDB caused issues with the data table.
o	Solution: Dropped the _id field from the DataFrame to ensure compatibility with the data table.
2.	Dynamic Updates:
o	Issue: Ensuring that all components (data table, charts) update correctly based on user interactions.
o	Solution: Implemented and tested Dash callbacks to handle dynamic updates efficiently.
3.	Integration of Dash Leaflet:
o	Issue: Integrating Dash Leaflet with the dashboard for the geolocation map.
o	Solution: Utilized the dash_leaflet library and configured the map to display the correct coordinates and tooltips.
Resources
•	MongoDB: MongoDB Documentation
•	Dash: Dash Documentation
•	Plotly: Plotly Documentation
•	Dash Leaflet: Dash Leaflet Documentation
•	JupyterDash: JupyterDash Documentation
Conclusion
This project successfully implements an interactive dashboard for Grazioso Salvare, providing intuitive data visualization and filtering options. The use of MongoDB, Dash, and Plotly ensures a flexible and powerful solution, suitable for analyzing and visualizing rescue animal data. The detailed documentation and screenshots included in this README provide a comprehensive guide for understanding and reproducing the project.
Motivation
The project was developed to demonstrate the use of Python's object-oriented programming principles to interact with MongoDB databases. It provides a reusable, easy-to-understand, and maintainable codebase for database operations.
Getting Started
To get a local copy up and running, follow these simple steps.

Installation

Clone the repository:


Install Python and pip: Ensure you have Python 3.x and pip installed. You can download Python from python.org.

Install the required Python packages:
pip install pymongo



Problems and challenges. 

Contact
Your name: Israel Renfro
