from scraper import Scraper

class Search:
    'Class to initialize search'

    def __init__(self):
        """Initialize the iMDB top 1000 search object
        """

        # initialize the scraper to pull imdb data into search

        self.imdb_scraper = Scraper()
        self.imdb_scraper.startScraper()


        print("==================== WELCOME TO TOP 1000 iMDB SEARCH ====================")
        print("Type any genre")
        print("Type 'exit' to Quit.")


    def searchQuery(self, search_terms):

        # split the search term by '&'
        search_terms_arr = search_terms.split('&')
        cleaned_search = [term.strip().lower() for term in search_terms_arr]
        
        return self.imdb_scraper.search_graph.findCommonNeighbors(cleaned_search)


    def launchSearch(self):

        while True:
            search_terms = str(input("Search: "))

            if search_terms.strip() == "exit": 
                print("Bye!")
                break
            
            search_movie_list = self.searchQuery(search_terms)

            if len(search_movie_list) == 0: 
            	print("Sorry we could not find anything for your search request :(")
            
            else: 
            	i = 0
            	for movie in search_movie_list:
            		if i < 11:
            			print(str(i+1) + ". " + movie.title())
            			i+=1

            		else:
            			break



def main():

    # start scraper and search
    search = Search()
    search.launchSearch()

if __name__ == "__main__":
    main()