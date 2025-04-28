
# Calories Insight

Calories Insight is a Streamlit application that uses Google's Gemini AI to analyze images of food, estimate the total calories, and provide a detailed nutritional breakdown.

"Upload a food image — Get calorie count, item breakdown, and health insights!"




## Features

- Upload food images (jpg, jpeg, png).

- Analyze food items using Gemini 1.5 Pro model.

- Receive:

    - Calorie count per item

    - Healthiness assessment

    - Percentage breakdown: Carbs, Fats, Sugars, Proteins, Fibers, Others

- Beautiful interactive UI built with Streamlit.


## 🛠️ Tech Stack

- **Python** 3.10

- **Streamlit** for the web UI

- **google-generativeai** for accessing Gemini models

- **python-dotenv** for environment variable management


## 📦 Installation

1. 📥 Clone the Repository
Clone the GitHub repository to your local system to get the source code.

```sh
git clone https://github.com/kjoseshalu/Calories-Insight.git
cd Calories-Insight

```

This command copies the repository files to your machine and changes the current directory to the project folder.

2. 🐍 Create a Virtual Environment

Create an isolated Python environment using conda to manage dependencies easily.
```sh
conda create -p venv python=3.10 -y
```
-p venv creates a virtual environment in a folder named venv.
python=3.10 specifies the Python version.
-y auto-confirms the environment creation.

3. ⚡ Activate the Virtual Environment

Activate the environment you just created.
```sh
conda activate venv/
```
This ensures all the packages are installed and run within the isolated environment.

4. 📦 Install Required Dependencies
Install all the Python libraries specified in requirements.txt.
```sh
pip install -r requirements.txt
```
This step is crucial to ensure the app runs without missing any dependencies.

5. 🔐 Create a .env File
Create a .env file in the root directory of your project and add your Google API Key.
```sh
GOOGLE_API_KEY=your-api-key

```
This file is used to securely store sensitive credentials.
🔑 You need a valid API key from [Google AI Studio](https://makersuite.google.com/) .

6. 🚀 Run the Streamlit App
Start the application using Streamlit.

```sh
streamlit run app.py
```
7. 🌐 Open the App in Your Browser
Open the following URL in your browser:
```sh
http://localhost:8501
```
This is the default address where Streamlit apps run locally.

    
## Output

[📄 View the PDF Guide](https://github.com/kjoseshalu/Calories-Insight/blob/main/Calories-%20Insight-Ouptut.pdf)


