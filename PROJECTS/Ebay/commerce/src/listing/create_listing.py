from .listing import Listing, DefaultArguments
from ..exceptions import ListingError

class ListingCreateNew(Listing):
    def __init__(self, default_arguments: DefaultArguments):
        super().__init__(default_arguments)
 
    # Return False if listing with same name already exist
    def create_listing(self, data, CategoryModel) -> bool:
        listing_name = data["name"]
        if self.check_same_name(listing_name):
            return False
        
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
    
    def get_categories(self, id_categories, CategoryModel) -> list:
        categories = CategoryModel.objects.all()
        listing_categories = [categories[int(id_category)-1] for id_category in id_categories]
        return listing_categories
