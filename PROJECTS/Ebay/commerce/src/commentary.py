class Commentary:
    def __init__(self, request, model):
        self.request = request
        self.model = model

    def add_commentary(self, commentary: str, listing_id:int, UserModel, ListingModel):
        user = UserModel.objects.get(username=self.request.user)
        listing = ListingModel.objects.get(id=listing_id)
        new_commentary = self.model(user=user, commentary=commentary, listing=listing) 
        new_commentary.save()
    
    def delete_commentary(self):
        pass


