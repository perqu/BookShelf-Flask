from urllib.request import urlopen
import json


def GetBookData(bookName):
    if bookName == None:
        return None
    bookName = bookName.replace(" ", "%20")
    url = f"https://www.googleapis.com/books/v1/volumes?q={bookName}"

    # store the response of URL
    response = urlopen(url)

    # storing the JSON response
    data_json = json.loads(response.read())

    selected_data = []

    for i in range(len(data_json["items"])):
        temp = {}

        # counter
        temp["id"] = i + 1
        # title
        try:
            temp["title"] = data_json["items"][i]["volumeInfo"]["title"]
        except:
            temp["title"] = "None"
        # authors
        try:
            temp["authors"] = data_json["items"][i]["volumeInfo"]["authors"]
        except:
            temp["authors"] = "None"
        # published_date
        try:
            temp["published_date"] = data_json["items"][i]["volumeInfo"][
                "publishedDate"
            ]
        except:
            temp["published_date"] = "None"
        # ISBN10
        try:
            industry_identifiers = data_json["items"][i]["volumeInfo"][
                "industryIdentifiers"
            ]
            for el in industry_identifiers:
                if el["type"] == "ISBN_10":
                    temp["ISBN10"] = el["identifier"]
            if "ISBN10" not in temp.keys():
                temp["ISBN10"] = "None"
        except:
            temp["ISBN10"] = "None"
        # ISBN13
        try:
            industry_identifiers = data_json["items"][i]["volumeInfo"][
                "industryIdentifiers"
            ]
            for el in industry_identifiers:
                if el["type"] == "ISBN_13":
                    temp["ISBN13"] = el["identifier"]
            if "ISBN13" not in temp.keys():
                temp["ISBN13"] = "None"
        except:
            temp["ISBN13"] = "None"
        # page_count
        try:
            temp["page_count"] = data_json["items"][i]["volumeInfo"]["pageCount"]
        except:
            temp["page_count"] = 0
        # preview_link
        try:
            temp["preview_link"] = data_json["items"][i]["volumeInfo"]["previewLink"]
        except:
            temp["preview_link"] = "None"
        # language
        try:
            temp["language"] = data_json["items"][i]["volumeInfo"]["language"]
        except:
            temp["language"] = "None"

        selected_data.append(temp)

    return selected_data
