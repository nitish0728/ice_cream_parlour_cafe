# ice_cream_parlour_cafe
This project is a straightforward web application for running a cafe with an ice cream shop. The program manages seasonal flavor options, ingredient inventory, customer flavor suggestions, and allergy issues using Flask for the backend and SQLite for the database. HTML, CSS, and JavaScript are used to construct the frontend.
## Project Structure

/ice_cream_parlour_cafe /static /css styles.css/js script.js/templates index.htmlapp.pyREADME.md
## Getting Started 
### Prerequisites - Python 3.x - pip 
### Installation
 1. Clone the repository: ```bash git clone https://github.com/your-username/ice_cream_parlor_cafe.git cd ice_cream_parlor_cafe


 2.Install the required dependencies:
 pip install -r requirements.txt


3. Start the Flask server
    python app.py  


File Descriptions
app.py
This file contains the backend logic for managing flavors, ingredients, customer suggestions, and the cart using Flask and SQLite.

templates/index.html
This file contains the HTML structure of the application.

static/css/styles.css
This file contains the CSS styles for the application.

static/js/script.js
This file contains the JavaScript code for interacting with the backend APIs and updating the frontend dynamically.

API Endpoints
GET /flavors
Fetch all flavor offerings.

POST /flavors
Add a new flavor offering.

GET /ingredients
Fetch all ingredients in the inventory.

POST /ingredients
Add a new ingredient to the inventory.

POST /suggestions
Submit a customer flavor suggestion or allergy concern.

GET /cart
Fetch all items in the cart.

POST /cart
Add an item to the cart.


Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.