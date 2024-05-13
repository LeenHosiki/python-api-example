from pyairtable import Api
import pandas as pd
from airtable import airtable

apiKey = 'patjBumX9wHN6LZID.d878740118a9334a7ed950033bfbf9cdcbf607edaa46d3f46a990b22205639b8'
tableKey = 'tblrbetENXIvP7FKo'
appKey = 'appZyCpb01HmLGd1u'

api = Api(apiKey)
bedData = api.table(appKey, tableKey)
tableName = 'bedData'
airtable = airtable.Airtable(appKey, tableName, api_key = apiKey)

bedData = airtable.get_all()
df = pd.DataFrame.from_records((r['fields'] for r in bedData))



class recommendBed:
    def userPreference(self, length, width, price):
        filtered_df = df[((df['Price'] > float(price)-500) & (df['Price'] < float(price)+500)) &
      ((df['Width'] > float(width)-30) & (df['Width'] < float(width)+30)) &
      ((df['Length'] > float(length)-15) & (df['Length'] < float(length)+15))]

        # Return random
        random_row = random.choice(filtered_df.index)
        data = filtered_df.loc[random_row].to_dict()
        return data
        
        # Return list of dictionaries
        #return filtered_df.to_dict('records')


"""
class BookReview:
    def __init__(self):
        self.api = Api(apiKey)
        self.table = self.api.table(appKey, tableKey)

    def get_book_ratings(self, sort="ASC", max_records=10):
        if not sort:
            return self.table.all(max_records=max_records)
        elif sort == "ASC":
            rating = ["Rating"]
        elif sort == "DESC":
            rating = ["-Rating"]
        
        table = self.table.all(sort=rating, max_records=max_records)
        return table

    def add_book_rating(self, book_title, book_rating, notes=None):
        fields = {'Book': book_title, 'Rating': book_rating, 'Notes': notes}
        self.table.create(fields=fields)

"""

if __name__ == '__main__':
    rc = recommendBed()
    # br.add_book_rating('Infinite Jest', 7.0)
    recBed = rc.userPreference(length = 200, width = 140, price = 1000)
    print(recBed)
