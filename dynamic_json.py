import psycopg2
import requests
import json

# Replace with the provided database connection details
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'tiger',
    'host': 'localhost',
    'port': '5432'
}

def fetch_student_data_and_call_api():
    # Connect to the database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    try:
        # Fetch data from the student table using the modified query
        cursor.execute("""
            SELECT
                json_build_object(
                    'name', first_name || ' ' || last_name,
                    'data', json_build_object('dob', date_of_birth)
                ) AS student_info
            FROM student;
        """)
        result = cursor.fetchall()

        # Extract the JSON result
        if result:
            student_data_json = [row[0] for row in result]

            # Pretty-print the JSON with indentation
            indented_json = json.dumps(student_data_json[0], indent=2)
            print("Student Data (Indented JSON):")
            print(indented_json)

            # Use the retrieved JSON data to make an API call
            api_url = 'http://localhost:8080/api'
            headers = {'Content-Type': 'application/json'}
            response = requests.post(api_url, json=student_data_json[0], headers=headers)

            # Print API response
            print("API Response:")
            print(response.text)

    except (psycopg2.Error, requests.RequestException) as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    fetch_student_data_and_call_api()
