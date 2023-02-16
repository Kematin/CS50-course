from .listing import CreateListingArguments
from ..exceptions import ListingError
from typing import NamedTuple

class UnpackedData(NamedTuple):
    description = str
    cost = float
    image_url = str
    categories = list[str]
    creator = str


class ListingCreateNew():
    def __init__(self, create_arguments: CreateListingArguments): 
        self.data = create_arguments.data 
        self.request = create_arguments.request 
        self.ListingModel = create_arguments.ListingModel 
        self.CategoryModel = create_arguments.CategoryModel
        self.all_listings = self.ListingModel.objects.all()

    def create_listing(self) -> None:
        name = self.data["name"]
        if self.check_same_name(name):
            raise ListingError
        else: 
            try:
                data = self.unpack_data(self.data)
                description, cost, image_url, creator, categories = data

                new_listing = self.ListingModel(name=name, description=description, 
                                    cost=cost, image_url=image_url, creator=creator)
                new_listing.save()
                new_listing.category_names.set(categories)
                new_listing.save()
            except Exception as e:
                print(e)
                raise ListingError
        
    def unpack_data(self, data):
        description = data["description"] 
        cost = data["cost"] 
        image_url = self.create_image_url(data["image_url"])
        category_names = self.request.POST.getlist("category_names")
        creator = self.request.user
        categories = self.get_categories(category_names, self.CategoryModel)

        data = (description, cost, image_url, creator, categories)
        return data 

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
