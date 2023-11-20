
# NQL - Natural Query Language

## Introduction
NQL allows you to use Natural Language to perform SQL operations on your database

## Features
- **SQL Query Execution**: Execute SQL queries seamlessly through natural language right from your command line.
- **Database Schema Description**: Send ChatGPT a schema of your database tables at the beginning of th conversation.
- **Integration with OpenAI**: Leverage OpenAI's capabilities for advanced operations. (Let ChatGPT figure out that crazy Inner Join Query!)

## Requirements
- Python 3.x
- MySQL Database
- OpenAI API Key

## Installation
1. **Clone the Repository**:
   ```
   git clone https://github.com/david-mackay/SQL-for-GPT.git
   cd sqlbuddy
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Configuration**:
   - Create a `db_config.json` file with your database configuration.
   - Place your OpenAI API key in a file named `api_key.txt`.

## Usage
1. **Setting Up Database Configuration**:
   Create the file `db_config.json` to include your database credentials. Remember to set up permissions for this user knowing that ChatGPT will have these permissions:
   ```json
   {
     "host": "localhost",
     "user": "your_username",
     "password": "your_password",
     "database": "your_database"
   }
   ```
2. **Setting Up OpenAI API Key**:
   Create the file `api_key.txt` to include your OpenAI API key. This key will be used to make requests to the OpenAI API.
   ```
   sk-blahblahblah
   ```

3. **Running the Application**:
   Execute `main.py` to start the application:
   ```
   python main.py
   ```

4. **Executing SQL Queries**:
   Follow the prompts in the application to execute SQL queries and view database schema.

## Contributing
Contributions to the SQL Buddy project are welcome. Please ensure to follow coding standards and submit pull requests for any new features or bug fixes. Prompt improvements and better usage of openAI's python package are super appreciated!.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
