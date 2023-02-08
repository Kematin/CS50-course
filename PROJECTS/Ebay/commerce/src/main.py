class CreateListing:
    def __init__(self, request, model):
        self.model = model
        self.request = request

    def main(self, data):
        listing_name = data["name"]
        if self.check_same_name(listing_name):
            return None
        
        listing_description = data["description"] 
        listing_cost = data["cost"] 
        listing_creator = self.request.user
        listing_image = self.create_image_url(data["image_url"])

        new_listing = self.model(name=listing_name, description=listing_description, 
                            cost=listing_cost, image_url=listing_image, creator=listing_creator)
        new_listing.save()
        return True

    def check_same_name(self, listing_name: str):
        all_listings = self.model.objects.all()
        names_listing = [listing.name for listing in all_listings]
        if listing_name in names_listing:
            return True
        else:
            return False

    def create_image_url(self, listing_image: str):
        if listing_image is None:
            # str replace to directory src with image
            return "No image"
        else:
            return listing_image
