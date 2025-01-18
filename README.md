# Quiz Game - General Knowledge

A general knowledge quiz game playable in the terminal. The user can choose their difficulty level (easy, medium, hard) and answer 10 random questions. At the end, a score is displayed along with an encouragement message tailored to the performance.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following:

- Python 3.10 or later
- Standard Python libraries (to be confirmed during installation)

### Installing

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/JulesSylMUAMBA/Quiz_game-MUAMBA-CDOF3.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Quiz_game-MUAMBA-CDOF3
   ```
3. Install dependencies if required:
   ```bash
   pip install -r requirements.txt
   ```
   An other option to build the project :
   ```bash
   pip install .
   ```

### Example Execution

1. Run the game:
   ```bash
   python main.py
   ```
2. Follow the displayed instructions to select your difficulty level and answer the questions.

## Running the Tests

### End-to-End Tests

These tests verify the overall functionality of the game.

1. Ensure the JSON question file is properly formatted.
2. Run the test script:
   ```bash
   python tests/test_end_to_end.py
   ```

### Code Style Tests

These tests ensure the code adheres to Python style standards (PEP8).

1. Use the `flake8` tool:
   ```bash
   flake8 .
   ```

## Deployment

This project is designed for local use in a terminal. No online production dependencies are required.

## Built With

- **Python** - Main language for development
- **JSON** - Format for storing questions and messages

## Contributing

Please read the `CONTRIBUTING.md` file for details on our code of conduct and the process for submitting pull requests.

## Versioning

We use [SemVer](https://semver.org/) for versioning. See the tags on this repository for available versions.

## Authors

- **Jules Sylvain MUAMBA** - Initial work

See also the list of contributors who participated in this project.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

- Thanks to [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) for the README template
- Inspiration:
  - [MAT34525](https://github.com/MAT34525)
  - Nandy Bâ (Developer at Aave, Mentor ETH Global)
  - Baptiste Florentin (DeFi Engineer, Entrepreneur)
  - AIT LAHCEN Souhail

