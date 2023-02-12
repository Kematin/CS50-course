class Listing:
    def __init__(self, request, model):
        self.model = model
        self.request = request
        self.all_listings = self.model.objects.all()

    # Return None if new cost less than old
    def upp_cost(self, listing_id: int, new_cost: float, UserModel) -> bool | None:
        listing = self.all_listings.get(id=listing_id)
        old_cost = listing.cost

        if self.check_new_cost(old_cost, new_cost):
            return None
        else:
            temporary_winner = UserModel.objects.get(username=self.request.user)
            listing.cost = new_cost
            listing.temporary_winner = temporary_winner.username
            listing.save()
            return True
 
    def delete_listing(self, listing_id: int) -> bool | None:
        listing = self.all_listings.get(id=listing_id)
        winner = listing.temporary_winner
        if winner:
            listing.winner = winner
            listing.save()
            return True
        else:
            return None

    # Return None if listing with same name already exist
    def create_listing(self, data, CategoryModel) -> bool | None:
        listing_name = data["name"]
        if self.check_same_name(listing_name):
            return None
        
        # Get main data
        listing_description = data["description"] 
        listing_cost = data["cost"] 
        listing_image = self.create_image_url(data["image_url"])
        listing_id_categories = self.request.POST.getlist("category_names")

        # Get creator 
        listing_creator = self.request.user

        # Get categories
        listing_categories = self.get_categories(listing_id_categories, CategoryModel)

        # Create new listing
        new_listing = self.model(name=listing_name, description=listing_description, 
                            cost=listing_cost, image_url=listing_image, creator=listing_creator)
        new_listing.save()
        new_listing.category_names.set(listing_categories)
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

    def get_categories(self, id_categories, CategoryModel) -> list:
        categories = CategoryModel.objects.all()
        print(id_categories)
        listing_categories = [categories[int(id_category)-1] for id_category in id_categories]
        return listing_categories


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
