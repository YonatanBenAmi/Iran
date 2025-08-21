from dal import Dal


class GetData:

    dal = Dal()
    client = dal.open_connection()

    def get_collection(self):
        try:  
            return self.client.IranMalDB.tweets.find({})
        except Exception as e:
            print(e)
    