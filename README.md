# AlgoCompare

![Logo](public/favicon-32x32.png)

**AlgoCompare** is a web application designed to help you visualize and compare the performance of various sorting algorithms. Whether you're a student learning about algorithm complexity or a developer looking to optimize your code, AlgoCompare provides an intuitive interface to understand how different sorting techniques perform under the hood.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
  - [Backend Setup (Python)](#backend-setup-python)
  - [Frontend Setup (Vue.js)](#frontend-setup-vuejs)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Visualize Sorting Algorithms:** Watch how Bubble Sort, Merge Sort, Quick Sort, and Radix Sort operate on arrays in real-time.
- **Performance Comparison:** Compare the time taken by each sorting algorithm to understand their efficiencies.
- **Interactive Interface:** Generate random arrays with customizable parameters and perform linear searches to see how algorithms handle target searches.
- **Responsive Design:** Built with Vue.js and Tailwind CSS for a seamless experience across devices.

## Demo
![Screenshot 2024-09-25 201259](https://github.com/user-attachments/assets/5cedc084-f1b8-4f30-bca6-11369fbe18ff)
![Screenshot 2024-09-25 201239](https://github.com/user-attachments/assets/d0179cbb-17fe-4a63-bb5c-613abc8f45e4)

Visit the live demo [here](https://algocompare.onrender.com).

## Installation

Follow the steps below to set up AlgoCompare on your local machine.

### Backend Setup (Python)

1. **Clone the Repository**

   Open your terminal and run:

   ```bash
   git clone https://github.com/safegergis/AlgoCompare.git
   ```

   Navigate to the project directory:

   ```bash
   cd AlgoCompare/backend
   ```

2. **Create a Virtual Environment**

   A virtual environment isolates project dependencies. Run:

   ```bash
   python -m venv venv
   ```

   This creates a folder named `venv` in your backend directory.

   > **Note:** If you encounter an error related to `python` not being recognized, ensure Python is installed and accessible from your system's PATH.
   >
   > **Note:** If you do not have `venv` installed, you can install it by running `pip install virtualenv`.

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
   python server.py
   ```

   The backend server should now be running, typically on `http://127.0.0.1:5000/`.

### Frontend Setup (Vue.js)

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

   The frontend should now be accessible, typically on `http://localhost:3000/`.

## Usage

1. **Access the Application**

   Open your web browser and navigate to `http://localhost:3000/`.

2. **Input Array**

   - Enter a comma-separated list of numbers you wish to sort.
   - Alternatively, generate a random array by clicking the "Generate Random Array" button and setting your desired parameters.

3. **Select Target (Optional)**

   Enter a target number for linear search to find its indices in the sorted array.

4. **Sort Array**

   Click the "Sort Array" button to visualize and compare the performance of different sorting algorithms.

5. **View Results**

   - **Sorting Time Comparison:** View a bar chart comparing the time taken by each algorithm.
   - **Sorted Arrays:** See the sorted results for Bubble Sort, Merge Sort, Quick Sort, and Radix Sort.
   - **Linear Search:** Find the indices of the target number in the sorted array and see the time taken for the search.

6. **Clear Results**

   Use the "Clear" button to reset all inputs and results.

## API Endpoints

### `POST /sort`

Sorts the given array using various algorithms and performs a linear search.

- **Request Body:**

  ```json
  {
    "array": [64, 34, 25, 12, 22, 11, 90],
    "target": 22
  }
  ```

- **Response:**

  ```json
  {
    "bubble_sort": {
      "sorted_array": [11, 12, 22, 25, 34, 64, 90],
      "time_taken": 5.123
    },
    "merge_sort": {
      "sorted_array": [11, 12, 22, 25, 34, 64, 90],
      "time_taken": 3.456
    },
    "quick_sort": {
      "sorted_array": [11, 12, 22, 25, 34, 64, 90],
      "time_taken": 2.789
    },
    "radix_sort": {
      "sorted_array": [11, 12, 22, 25, 34, 64, 90],
      "time_taken": 1.234
    },
    "linear_search": {
      "found": [2],
      "time_taken": 0.567
    }
  }
  ```

> **Note:** The backend server restricts access to `https://algocompare.onrender.com`. Ensure your frontend is configured correctly to communicate with the backend.

## Technologies Used

### Frontend

- **[Vue.js](https://vuejs.org/):** JavaScript framework for building user interfaces.
- **[Tailwind CSS](https://tailwindcss.com/):** Utility-first CSS framework for styling.
- **[Chart.js](https://www.chartjs.org/):** JavaScript charting library for data visualization.
- **[TypeScript](https://www.typescriptlang.org/):** Typed superset of JavaScript.

### Backend

- **[Flask](https://flask.palletsprojects.com/):** Lightweight WSGI web application framework.


Please ensure your code follows the project's code style and passes all linting checks.

## License
