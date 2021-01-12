# Save data to an AWS bucket

from typing import Dict

import aws_lib


def aws_upload(data: Dict):
    database = aws_lib.connect("AKIAF6BAFJKR45SAWSZ5", "hjshnk5ex5u34565AWS654/JKGjhz545d89sjkja")
    database.push(data)


def transform_data(es_data: Dict) -> Dict:
    es_data = {**data, "origin": "ES"}
