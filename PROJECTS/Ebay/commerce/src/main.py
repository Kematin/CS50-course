class Listing:
    def __init__(self, request, model):
        self.model = model
        self.request = request
        self.all_listings = self.model.objects.all()

    # Return None if new cost less than old
    def upp_cost(self, listing_id: int, new_cost: float) -> bool | None:
        listing = self.all_listings.get(id=listing_id)
        old_cost = listing.cost

        if self.check_new_cost(old_cost, new_cost):
            return None
        else:
            listing.cost = new_cost
            listing.save()
            return True
 
    def delete_listing(self, listing_id: int) -> None:
        listing = self.all_listings.get(id=listing_id)
        listing.delete()

    # Return None if listing with same name already exist
    def create_listing(self, data) -> bool | None:
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

    def check_same_name(self, listing_name: str) -> bool:
        names_listing = [listing.name for listing in self.all_listings]
        if listing_name in names_listing:
            return True
        else:
            return False

    def create_image_url(self, listing_image: str) -> str:
        if listing_image is None:
            # str replace to directory src with image
            return "No image"
        else:
            return listing_image
    
    def check_new_cost(self, old_cost, new_cost) -> bool:
        if new_cost <= old_cost:
            return True
        else:
            return False
