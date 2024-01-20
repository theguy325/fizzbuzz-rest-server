from flask import Flask, jsonify
app = Flask(__name__)

# Counter variables for statistics
stats = {
    "fizz_count": 0,
    "buzz_count": 0,
    "fizzbuzz_count": 0
}


def fizz_buzz_logic(number, int1, int2, str1, str2):
    """
    Helper function to apply Fizz-Buzz logic to a given number.

    Args:
        number (int): The number to check.
        int1 (int): First divisor.
        int2 (int): Second divisor.
        str1 (str): String replacement for multiples of int1.
        str2 (str): String replacement for multiples of int2.

    Returns:
        str: Resulting string based on Fizz-Buzz logic.
    """
    global stats
    result = ""

    if number % int1 == 0 and number % int2 == 0:
        result = str1 + str2
        stats["fizzbuzz_count"] += 1

    elif number % int1 == 0:
        result = str1
        stats["fizz_count"] += 1

    elif number % int2 == 0:
        result = str2
        stats["buzz_count"] += 1

    else:
        result = str(number)

    return result


@app.route('/fizzbuzz/<int:int1>/<int:int2>/<int:limit>/<str1>/<str2>', methods=['GET'])
def fizz_buzz(int1, int2, limit, str1, str2):
    """
    Fizz-Buzz API endpoint.

    Args:
        int1 (int): First divisor.
        int2 (int): Second divisor.
        limit (int): Upper limit for the range of numbers.
        str1 (str): String replacement for multiples of int1.
        str2 (str): String replacement for multiples of int2.

    Returns:
        json: Resulting list of strings based on Fizz-Buzz logic.
    """
    final_result = ""
    result_list = [fizz_buzz_logic(i, int1, int2, str1, str2) for i in range(1, limit + 1)]
    result_list[limit - 1] += "."
    # return jsonify({"result": result_list})
    for num in range(0, limit - 1):
        result_list[num] += ","

    for each in result_list:
        final_result += each

    return final_result




@app.route('/statistics', methods=['GET'])
def statistics():
    """
    Statistics API endpoint.

    Returns:
        json: Statistics about the most used request.
    """
    global stats
    most_used_request = max(stats, key=stats.get)
    stat_result = {
        "most_used_request": most_used_request,
        "hits": stats[most_used_request]
    }
    return jsonify(stat_result)


if __name__ == '__main__':
    app.run(debug=True)
