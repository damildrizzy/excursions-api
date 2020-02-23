import os
import json
from api.models import Excursion
from django.core.management.base import BaseCommand
from cruise.settings import BASE_DIR

class Command(BaseCommand):
    def import_from_file(self):
        json_file = os.path.join(BASE_DIR, 'api', 'resources/data.json')
        with open(json_file, encoding='UTF-8') as data_file:
            data = json.loads(data_file.read())
            for data_object in data:
                id = data_object.get('id')
                name = data_object.get('name')
                detailPageName = data_object.get('detailPageName')
                portID = data_object.get('portID')
                type = data_object.get('type')
                typology = data_object.get('typology')
                activityLevel = data_object.get('activityLevel')
                collectionType = data_object.get('collectionType')
                duration = data_object.get('duration')
                language = data_object.get('language')
                priceLevel = data_object.get('priceLevel')
                currency = data_object.get('currency')
                mealInfo = data_object.get('mealInfo')
                status = data_object.get('status')
                shortDescription = data_object.get('shortDescription')
                longDescription = data_object.get('longDescription')
                externalContent = data_object.get('externalContent')
                minimumAge = data_object.get('minimumAge')
                wheelChairAccessible = data_object.get('wheelChairAccessible')
                featured = data_object.get('featured')

                try:
                    excursion = Excursion.objects.create(
                        id=id,
                        name=name,
                        detailPageName = detailPageName,
                        portID = portID,
                        type = type,
                        typology = typology,
                        activityLevel = activityLevel,
                        collectionType = collectionType,
                        duration = duration,
                        language = language,
                        priceLevel = priceLevel,
                        currency = currency,
                        mealInfo = mealInfo,
                        status = status,
                        shortDescription = shortDescription,
                        longDescription = longDescription,
                        externalContent = externalContent,
                        minimumAge = minimumAge,
                        wheelChairAccessible = wheelChairAccessible,
                        featured = featured
                    )

                    excursion.save()

                    print("Data Imported")

                except Exception as ex:
                        print(str(ex))

    def handle(self, *args, **options):
        """
        Call the function to import data
        """
        self.import_from_file()
                        



