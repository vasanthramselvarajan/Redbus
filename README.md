# Interactive state bus data analysis

## Project Description

### Overview

The project is a comprehensive bus data aggregation and visualization tool designed to enhance user experience in finding and comparing bus travel options. Using Selenium for data scraping, MySQL for data storage, and Streamlit for visualization, the project provides a user-friendly web application to explore bus details across ten states.

### Objectives

- **Data Collection:** Extract detailed bus information from the RedBus website.
- **Data Storage:** Organize and store the collected data in a structured database.
- **Data Visualization:** Develop an interactive web application to display and filter bus data.

### Components

1. **Data Scraping with Selenium:**
   - **Objective:** Automate the extraction of bus details from the RedBus site.
   - **Details Scraped:**
     - **Bus Name:** The name of the bus service and its type.
     - **Bus Fare:** The cost of the bus ticket.
     - **Departure and Arrival Time:** The scheduled times for departure and arrival.
     - **Travel Duration:** The total time taken for the journey.
     - **Bus Rating:** User ratings of the bus service.
     - **Route Name:** The name of perticular route.
     - **Route Link:** URL of perticular route.

2. **Data Storage with MySQL:**
   - **Objective:** Store and manage the scraped bus data efficiently.
   - **Implementation:** 
     - **Database Schema:** Created tables to organize bus details and their relationships.
     - **State Tables:** Used separate tables for data from different states.
     - **Column Data Types:** Adjusted data types of some columns to better match the data.

3. **Data Visualization with Streamlit:**
   - **Objective:** Create an interactive web application for users to explore bus data.
   - **Features:**
     - **Interactive Filters:**
       - **Route Box:** Filter buses by specific travel routes.
       - **Rating Filter:** Sort or filter buses based on user ratings.
       - **Fare Filter:** Adjust the search results based on ticket fare.
       - **Departure and Arrival Time Filters:** Customize results based on travel times.
     - **Visual Representation:** Present data in table format for easy understanding.

### Process and Methodology

1. **Data Extraction:**
   - Utilized Selenium with Python to automate the extraction of bus data from the RedBus website.
   - Implemented error handling to ensure accuracy.

2. **Data Management:**
   - Created a MySQL database with tables to store various attributes of bus data.

3. **Application Development:**
   - Developed a Streamlit web application to visualize the data.
   - Integrated powerful filters to allow users to customize their search and view results based on their preferences.

### Challenges and Solutions

- **Challenge:** Handling dynamic web content and ensuring data accuracy.
  - **Solution:** Implemented error handling(try, except and excepted condition) and time implementation( time module, implicit time) in Selenium to overcome this challenge.

- **Challenge:** Creating an intuitive user interface with comprehensive filters.
  - **Solution:** Designed and tested multiple UI layouts to enhance user experience.

### Expected Outcomes and Impact

- **Enhanced User Experience:** Users can easily find and compare bus options across ten states with various filters.
- **Interactive Insights:** Visualization of bus data through an accessible web application, providing valuable insights and facilitating informed decision-making.
