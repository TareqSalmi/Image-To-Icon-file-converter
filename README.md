# Image To Icon Converter

The "Image To Icon Converter" is a simple Python application built with PyQt5 and Pillow that allows you to convert image files (PNG and JPG) into Windows icon (.ico) files. This tool is particularly useful when you need custom icons for your applications or projects.

## Features

- Converts PNG and JPG image files to Windows icon (.ico) format.
- Displays the conversion progress with a progress bar.
- Provides detailed status updates on the conversion process.
- Allows you to select an icon file to use as the application's window icon.

## Prerequisites

Before running the application, ensure you have the following prerequisites installed:

- Python 3.x
- PyQt5
- Pillow (PIL)

You can install the required Python packages using pip:

**pip install PyQt5 pillow**


## How to Use

1. _**Clone the Repository**_

   Clone this repository to your local machine using Git:

**git clone https://github.com/your-username/image-to-icon-converter.git**

2. _**Navigate to the Project Directory**_

**cd image-to-icon-converter**

3. **Run the Application**

Execute the following command to run the application:

**python converter.py**

4. **Using the Application**

- Click the "Select Icon" button to choose an icon file that will be used as the application's window icon.
- Click the "Convert Image" button to select a folder containing PNG and JPG image files for conversion.
- The application will display the conversion progress using a progress bar.
- Status updates about the conversion process will be shown in the text box.
- Converted icon files will be saved in the same directory as the source images with the ".ico" extension.

5. **Notes**

- Ensure that the selected folder contains PNG or JPG image files for conversion.
- The selected icon will be used as the application's window icon while the application is running.

## License

This project is licensed under the MIT License. 

## Acknowledgments

- The application uses PyQt5 for the graphical user interface.
- Image processing is performed using Pillow (PIL).






