import app


if __name__ == '__main__':
    extracted = app.event.scrape().extract()
    print(extracted)

    content = app.database.get_data()

    if extracted != "No upcoming tours":
        for row in content:
            if extracted not in row:
                app.database.store_data(extracted)
                app.email.send_email(message="Hey, new event was found!")
