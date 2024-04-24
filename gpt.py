from g4f.client import Client


def RequestEvent(request: str) -> str:
    ''' returns response to request from user by gpt4 '''

    # sending request to gpt4
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{
            "role": 
            "user", "content": request
            }]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print(RequestEvent('Привет'))
