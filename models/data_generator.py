from faker import Faker
from faker.providers import DynamicProvider
from dataclasses import dataclass
from typing import List
import datetime
import random

@dataclass
class DataGenerator:
    column_names: List[str]

    def _generate_random_date(self,start_date, end_date):
        """Generates a random date between start_date and end_date."""
        delta = end_date - start_date
        days = delta.days
        random_days = random.randrange(days)
        return start_date + datetime.timedelta(days=random_days)

    def _generate_blank_date(self):
        """Generates a blank date."""
        return ""

    def generate_data(self, num_rows: int) -> List[str]:
        fake = Faker()
        data = []
        for _ in range(num_rows):
            row = {}
            row["Company"] = random.choice(["IBM","Microsoft","Apple","Google","Amazon","Facebook","Oracle","SAP","Salesforce","Adobe","Intel","Cisco","Dell","VMware","HP","Huawei","HPE","NTT","NEC","NTT Data","NTT Communications","NTT Security","NTT DOCOMO","NTT TechnoCross","NTT Urban Development","NTT Finance","NTT Advanced Technology","NTT DATA Business Solutions"])
            row["Product"] = random.choice(["Solo", "Professional", "Enterprise"])
            row["Last Name"] = fake.last_name()

            # Generate First name with a random percentage of Male and Female names
            if random.random() < 0.47:
                row["First Name"] = fake.first_name_female()
            else:
                row["First Name"] = fake.first_name_male()
            row["Telephone"] = fake.basic_phone_number()
            
            row["Deal Status"] = random.choice(["Closed", "Follow Up", "No Deal", "Interested" ,""])

            # Generate Completion Date with a random percentage of blank dates
            if random.random() < 0.43:
                row["Completion Date"] = self._generate_blank_date()
            else:
                row["Completion Date"] = self._generate_random_date(datetime.date(2002, 6, 1), datetime.date(2023, 6, 30))

            row["Sales Code"] = random.choice(["RPT", "NEW", "UPG", "ADD", ""])
            row["Type of Contact"] = random.choice(["In Person", "Expo Event", "Telephonic", "Email", "Social Media",""])

            # Generate Reach Attempt #1 with a random percentage of blank dates
            if random.random() < 0.83:
                row["Call Attempt #1"] = self._generate_blank_date()
            else:
                row["Call Attempt #1"] = self._generate_random_date(datetime.date(2023, 1, 1), datetime.date(2023, 6, 30))

            # Generate Reach Attempt #2 with a random percentage of blank dates
            if random.random() < 0.33:
                row["Call Attempt #2"] = self._generate_blank_date()
            else:
                row["Call Attempt #2"] = self._generate_random_date(datetime.date(2023, 1, 1), datetime.date(2023, 6, 30))

            # Generate Reach Attempt #3 with a random percentage of blank dates
            if random.random() < 0.63:
                row["Call Attempt #3"] = self._generate_blank_date()
            else:
                row["Call Attempt #3"] = self._generate_random_date(datetime.date(2023, 1, 1), datetime.date(2023, 6, 30))

            row["Subscription Plan"] = random.choice(["6 Mo", "12 Mo", "18 Mo", "1 Mo",""])

            # Generate 2023 Support Plan 2 with a random percentage of blank dates
            if random.random() < 0.73:
                row["Follow up"] = self._generate_blank_date()
            else:
                row["Follow up"] = self._generate_random_date(datetime.date(2023, 1, 1), datetime.date(2023, 6, 30))

            row["Type Of Contact"] = random.choice(["In Person", "Telephonic",""])
            row["Last Name of Sales Rep"] = fake.last_name()
            if random.random() < 0.67:
                row["First Name of Sales Rep"] = fake.first_name_female()
            else:
                row["First Name of Sales Rep"] = fake.first_name_male()
            row["Title of Sales Rep"] = random.choice(["Associate", "Manager", "Closer", ""])
            row["Comments"] = ""
            
            data.append(row)

        return data