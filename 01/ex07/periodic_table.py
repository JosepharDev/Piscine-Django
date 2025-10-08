#!/bin/python3
import sys


def generate_html(periodic):
    html = '''
        <!DOCTYPE html>
        <html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>periodic_table</title>
            <style>
                table{{
                    border-collapse: collapse;
                }}
                h4 {{
                    text-align: center;
                }}
                ul {{
                    list-style:none;
                    padding-left:0px;
                }}
            </style>
            </head>
        <body>
            <table>
                {body}
            </table>
        </body>
        </html>'''
    cell = '''
        <td style="border: 1px solid black; padding:10px">
            <h4>{name}</h4>
            <ul>
                <li>No {number}</li>
                <li>{small}</li>
                <li>{molar}</li>
                <li>{electron} electron</li>
            </ul>
        </td>
        '''
    body_construct = "<tr>"
    position = 0
    for item in periodic:
        if position > int(item["position"]):
            body_construct += "    </tr>\n    <tr>"
            position = 0
        for _ in range(position, int(item["position"]) - 1):
            body_construct += "      <td></td>\n"
        position = int(item["position"])
        body_construct += cell.format(
            name=item["name"],
            number=item["number"],
            small=item["small"],
            molar=item["molar"],
            electron=item["electron"],)
    body_construct += "    </tr>\n"
    f = open("periodic_table.html", "w")
    f.write(html.format(body=body_construct))
    f.close()


if __name__ == "__main__":
    try:
        tmp = []
        value = {}
        res = []
        with open("periodic_table.txt", "r") as file:
            for line in file:
                tmp = line.split("=")
                value = dict((value.strip().split(":")
                                for value in tmp[1].split(", ")))
                value["name"] = tmp[0].strip()
                res.append(value)
        generate_html(res)
    except Exception as e:
        print(f"Error {e}")
