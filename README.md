# FizzBuzz REST Server

This is a simple Flask application that provides a REST API endpoint for the classic Fizz-Buzz algorithm. It also includes a statistics endpoint to track the most used request.

## Setup

1. Ensure you have Python installed on your machine.
2. Install Flask using the following command:
   ```bash
   pip install Flask

## Running the Server
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to start the server:
    python fizzbuzz_server.py
   (The server will be accessible at http://127.0.0.1:5000/ or http://localhost:5000/)


## Endpoints
    ## Fizz-Buzz Endpoint
    URL: /fizzbuzz/<int1>/<int2>/<limit>/<str1>/<str2>
    Method: GET
    Parameters:
        int1, int2: Integers for divisors.
        limit: Upper limit for the range of numbers.
        str1, str2: Strings for replacements.
    Example: /fizzbuzz/3/5/15/fizz/buzz
    ## Statistics Endpoint
    URL: /statistics
    Method: GET
## Testing
Install the required testing dependencies:
    pip install Flask
    Run the unit tests using the following command:
        python test_fizzbuzz_server.py

## Contributing
Feel free to contribute by opening issues or submitting pull requests.

## License
Made by Nishant Pandey