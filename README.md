# ai-ml-task

## Problem Statement:
You are given an image which contains multiple headings and subheadings, perform suitable preprocessing techniques and computer vision approaches to extract the text in an organized format, write the python code to take the image input and create the organized dictionary as output. 

## Sample Input and output
### Input 
![image](https://github.com/user-attachments/assets/e5695bba-0dfa-4144-8c09-1cabf8096b3e)
### Output
```json
{
  "Ashoka Chakra": "Dharma Chakra (Wheel of Law)",
  "Saffron": "Represents strength and courage",
  "Green": "Represents fertility, growth, and auspiciousness of the land",
  "White": "Symbolizes peace and truth"
}
```


### Requirements
The following libraries and tools are required for running the project:

Python Libraries
- pytesseract: For Optical Character Recognition (OCR).
- opencv-python: For preprocessing images.
- Pillow: For handling and manipulating images.
## External Tool
- Tesseract OCR: Make sure to install the Tesseract OCR engine separately
- Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki and after downloading it install into a folder. Edit the environment variables and add the exe file into the PATH of the System Variables.
- Linux: Install via sudo apt-get install tesseract-ocr
- MacOS: Install via Homebrew: brew install tesseract
### Virtual Environment 
It is a good pratice to create a virtual environment when doing a new project so that it  helps to  decouple and isolate Python installs and associated pip package. It also helps for people to replicate your project.
- In the terminal of your IDE go to command prompt and in that type python -m venv virtual-environment-name
- After creating the virtual environment you should activate it. To do that use venv/Scripts/activate.bat
- To see if you have activated the virtual environment you can see near the command prompt that the environment name is present in the left corner.
### Python Requirements File
- pytesseract
- opencv-python
- Pillow
### Steps to Run the Code
1)Install Tesseract OCR:
- Install Tesseract OCR on your system and set the path to tesseract.exe in your Python script.
2) Clone or Download the Repository
3) Clone this repository or download the necessary files, including the image sample.jpeg.
4) Set up the Path to Tesseract
- In the Python script (app.py), update the Tesseract path to point to the executable:
pytesseract.pytesseract.tesseract_cmd = r'path_to_your_tesseract_executable'
5) Install Python Libraries
- pip install -r requirements.txt
6) The output will be a dictionary where the extracted headings are keys and subheadings or values are the corresponding dictionary values.
### Explanation
1) Image Loading - We load the image using the Pillow library. In this case, the image (sample.jpeg) is loaded for text extraction.
2) Preprocessing the Image - Image preprocessing is crucial for improving OCR accuracy. Using OpenCV, the image is converted to grayscale to reduce noise and simplify the text extraction process. Further, thresholding techniques are applied to binarize the image, making the text stand out more clearly.
3) Extracting Text Using OCR (Tesseract)
Using pytesseract, the processed image is passed through the OCR engine, which extracts the text. This raw text contains all the headings, subheadings, and contents from the image in an unorganized format.
4) Organizing Extracted Text - After extracting the text, the program uses regular expressions (re) to identify headings and their corresponding values. The headings are treated as dictionary keys, and their values (or subheadings) are the dictionary values. This organization depends on the structure of the extracted text and specific rules for recognizing headings.
5) Returning the Organized Dictionary - The final output is a Python dictionary that organizes the headings and subheadings in a clean format.

