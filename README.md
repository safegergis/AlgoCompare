## Setup Instructions

### Backend Setup (Python)

Follow these steps to set up the Python backend:

1. **Clone the Repository**

   Open your terminal and run:

   ```bash
   git clone https://github.com/safegergis/AlgoCompare.git
   ```

   Navigate to the project directory:

   ```bash
   cd my-project/backend
   ```

2. **Create a Virtual Environment**

   A virtual environment isolates project dependencies. Run:

   ```bash
   python -m venv venv
   ```

   This creates a folder named `venv` in your backend directory.

   > **Note:** If you encounter an error related to `python` not being recognized, ensure Python is installed and accessible from your system's PATH.
   > **Note:** If you do not have venv installed, you can install it by running `pip install virtualenv`

3. **Activate the Virtual Environment**

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

   After activation, your terminal prompt will prefix with `(venv)` indicating the virtual environment is active.

4. **Upgrade pip**

   It's good practice to ensure `pip` is up-to-date:

   ```bash
   pip install --upgrade pip
   ```

5. **Install Backend Dependencies**

   Install the required Python packages using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   > **Note:** If `requirements.txt` is missing, ensure it's created by listing all necessary packages or consult the project maintainer.

6. **Start the Backend Server**

   Run the main application:

   ```bash
   python main.py
   ```

   The backend server should now be running, typically on `http://127.0.0.1:8000/`.

### Frontend Setup (Vue.js)

Follow these steps to set up the Vue.js frontend:

1. **Install Frontend Dependencies**

   Use `npm` to install all required packages:

   ```bash
   npm install
   ```

   > **Tips:**
   >
   > - Ensure you have a stable internet connection.
   > - If you encounter permission issues, consider using a Node version manager like `nvm`.

2. **Start the Frontend Development Server**

   Launch the Vue.js development server:

   ```bash
   npm run dev
   ```
