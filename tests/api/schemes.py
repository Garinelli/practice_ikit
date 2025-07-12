from pydantic import BaseModel

class Catalog(BaseModel):
    slug: str 
    path: str 
    title: str 
    image: dict 

class Offer(BaseModel):
    title: str 
    slug: str 
    offer: int
    color: str 
    background: str 

class RootMini(BaseModel):
    title: str
    slug: str 

class ProductByCode(BaseModel):
    id: str
    slug: str
    code: str
    article: str
    title: str
    description: str
    category_path: str
    in_basket: bool
    in_favorite: bool

class Product(BaseModel):
    id: str
    slug: str
    code: str
    article: str
    title: str
    category_path: str
    in_basket: bool
    in_favorite: bool

class ProductFilter(BaseModel):
    title:str
    code: str
    type: str
    min: str
    max: str

class City(BaseModel):
    title: str
    kladr_id: str
    subdomain: str
    coordinates: str

class Session(BaseModel):
  basket_count: int 
  favorite_count: int
  fizmobile_store: None
  user: None 
  isAdmin: bool
  isManager: bool
  canManage: bool

class SiteMapCatalogCategories(BaseModel):
    title: str 
    path: str 
    updated_at: str

class SiteMapLandings(BaseModel):
    path: str

class SiteMapNews(BaseModel):
    slug: str 
    updated_at: str

class SiteMapCatalogCategoriesTree(BaseModel):
    id: int
    title: str
    path: str
    _lft: int
    _rgt: int
    parent_id: None
    children: list

class ProductToBasket(BaseModel):
    type: str
    product_id: str
    quantity: int
    selected: bool

class Receive(BaseModel):
    title: str
    id: str 
