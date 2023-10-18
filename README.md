# Word Frequency Analyzer

#### Video Demo: URL_HERE

## Description

This project is a Python application that analyzes the word frequency in a given month's CNN article sitemap. It provides functionality to retrieve the most frequently used words, generate a bar chart of the top 20 words, and export the word frequency data to a CSV file.

## Key Features

- Analyzes word frequency in a specific month's CNN article sitemap.
- Retrieves the most frequently used words.
- Generates a bar chart of the top 20 most frequently used words.
- Exports word frequency data to a CSV file for further analysis.

## Prerequisites

- Python 3.x
- `requests` library
- `BeautifulSoup` library
- `matplotlib` library
- `spacy` library
- `tkinter` library (for GUI)

## Installation

1. Clone or download the project files to your local machine.

2. Install the required Python libraries by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

To run the project using the graphical user interface, navigate to the project directory and execute the following command:

```
python project.py
```

The application will open a GUI window where you can enter the month and year for analysis. Click the "Analyze" button to start the analysis process. The program will retrieve the sitemap for the specified month and year from CNN's website and display the most repeated words in the console. It will also generate a bar chart showing the top 20 most frequently used words.


![GUI Screenshot 1](screenshots/gui_screenshot_1.png)

![GUI Screenshot 2](screenshots/gui_screenshot_2.png)


### Testing

The project includes a test file `test_project.py` that uses pytest for unit testing. To run the tests, execute the following command:

```
pytest test_project.py
```

The tests validate the functionality of the project's functions and ensure that they behave as expected.

## Testing

The `test_project.py` file contains unit tests for the project functions.

To run tests, execute the following command:

```
pytest test_project.py
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For support and contribution guidelines, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

If you have any questions or need assistance, you can reach out to the project maintainers at project@example.com.

 Here is a suggested README file:

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Future Enhancements/Roadmap

While the current version of the Word Frequency Analyzer is functional and provides valuable insights into word frequencies, we have plans for future enhancements and additions. Some of the planned features and improvements include:

- Adding support for analyzing word frequencies from multiple sources, such as different news websites or RSS feeds.
- Implementing advanced text analytics techniques, such as sentiment analysis and entity recognition, to gain deeper insights from the analyzed data.
- Enhancing the visualization capabilities by providing more interactive and customizable charts and graphs.
- Improving the performance and efficiency of the word frequency analysis algorithm.
- Expanding the project's documentation and providing more comprehensive user guides and tutorials.

We are committed to continuously improving the Word Frequency Analyzer and welcome any feedback or suggestions from the user community.

---

Please refer to the previous sections for the complete Readme contents.