# Language Classification by Naive Bayes
This is a simple web application for language classification using Flask and a Naive Bayes classifier. The application allows users to input text, and it will predict whether the text is in English, Slovak, or Czech. Additionally, it displays a bar chart showing the predicted probabilities for each language.
![image](https://github.com/SubhScripter/Language_Classifier_NB/assets/142106447/3790930a-79ce-48f5-9885-bc116ede70ff)
## Features
- **Text Input**: Users can enter text into a text area on the web page.
- **Prediction**: After clicking the "Go!" button, the application will predict the language of the entered text.
- **Language Labels**: The predicted language is displayed with a corresponding color (red for English, blue for Slovak, and black for Czech).
- **Reset**: Users can reset the input area by clicking the "Reset" button.
- **Probability Chart**: A bar chart is displayed below the text area, showing the predicted probabilities for each language.

## Technologies Used

- **Flask**: The web application is built using the Flask web framework for Python.
- **Pickle**: The pre-trained Naive Bayes model and vectorizer are saved and loaded using the Pickle library.
- **Chart.js**: The probability chart is created using the Chart.js library.
- **HTML/CSS**: The user interface is built with HTML and styled using CSS.
- **JavaScript**: JavaScript is used to add interactivity to the web page, including showing the prediction container with animation.
- **Jupyter Notebook**: The training and model development were done in a Kaggle Notebook, which can be found in the `notebook` folder.
- **requirements.txt**: The `requirements.txt` file contains a list of Python packages and dependencies needed to run the project.

## Getting Started

To run this web application on your local machine, follow these steps:

1. Clone this repository to your local machine.
git clone https://github.com/SubhScripter/Language_Classifier_NB.git

2. Navigate to the project directory.
cd language-classifier-web-app

3. Install the required Python packages.
pip install -r requirements.txt

4. Run the Flask application.
python app.py

5. Open a web browser and go to `http://localhost:5000` to access the web application.

## Usage

1. Enter text into the text area.
2. Click the "Go!" button to make a language prediction.
3. The predicted language will be displayed with the corresponding color.
4. You can reset the input area by clicking the "Reset" button.
5. The probability chart below the text area shows the predicted probabilities for each language.

## Screenshots

![image](https://github.com/SubhScripter/Language_Classifier_NB/assets/142106447/eb85c4b4-e5ee-4c67-a72e-e9deecfcfc1d)

## Kaggle Notebook

The training and model development for this project were done in a Kaggle Notebook. You can find the notebook in the following Kaggle link:

[Kaggle Notebook - Language Classification with Naive Bayes](https://www.kaggle.com/code/subhraneelpaul/language-classification-with-naive-bayes)

This notebook contains the code and steps used to train the language classification model that powers this web application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This web application was created as a demonstration project for language classification using machine learning and web development.
- Special thanks to the Flask and Chart.js communities for their excellent documentation and resources.

Feel free to customize and extend this project for your own use or as a learning resource!


