from entities.store import Store
from entities.store_m2m_book import StoreM2MBook
from entities.store_m2m_vinyl import StoreM2MVinyl
from entities.stock_info import StockInfo



def populate() -> None:
    for store in [
        Store("Funky Street 69", "69696969", "dump@shite.onion"),
        Store("John Doe Avenue 420", "13371337", "merf@vas.merp"),
        Store("Dumb Cow Boulevard 1337", "69696969", "herpderp@flerp.merp"),
    ]:
        store.insert_query()
    
    for store_m2m_book in [
        StoreM2MBook(1,2),
        StoreM2MBook(1,3),
        StoreM2MBook(1,4),
        StoreM2MBook(1,5),
        StoreM2MBook(1,6),
        StoreM2MBook(2,2),
        StoreM2MBook(2,2),
        StoreM2MBook(2,2),
        StoreM2MBook(2,4),
        StoreM2MBook(2,7),
    ]:
        store_m2m_book.insert_query()
    
    for store_m2m_vinyl in [
        StoreM2MVinyl(1,3),
        StoreM2MVinyl(1,5),
        StoreM2MVinyl(1,7),
        StoreM2MVinyl(1,4),
        StoreM2MVinyl(1,1),
        StoreM2MVinyl(2,3),
        StoreM2MVinyl(2,5),
        StoreM2MVinyl(2,4),
        StoreM2MVinyl(2,4),
        StoreM2MVinyl(2,1),
    ]:
        store_m2m_vinyl.insert_query()
        
    for stock_info in [
        StockInfo("AOSIJCOAasd12aS",1,3,1),
        StockInfo("AAOSdijcocais",2,9,3),
        StockInfo("Qoisjdfov",1,7,2),
        StockInfo("zPsojovzixnvo",1,9,4),
        StockInfo("lASOdijozx",2,2,0),
        StockInfo("pajsudbiduQ",1,19,5),
    ]:
        stock_info.insert_query()
        
        
    
    
    
        

