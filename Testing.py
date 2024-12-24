import requests

def student_information(name):
    url="https://6766aa23410f849996584133.mockapi.io/api/v1/college"
    try:
        response=requests.get(url)
        data=response.json()
        if response.status_code==200:
            print("Url running successfully!")

        else:
            print("Your status code is: ",response.status_code)

        for student in data:
            if student["Student_name"].lower()==name.lower():
                print(f"Student marks is {student['Student_marks']}")
                break
            else:
                print("Not found that student name you have given!!!")
                break
    except (ValueError,KeyError,TypeError) as e:
        print(f"Error! {e}")
    finally:
        print("You're out of code now  !!")
student_information("Edwin.Gaurav")