from rest_framework.pagination import PageNumberPagination


class Pagenations(PageNumberPagination):
    page_size = 7                               #number of record show per page
    # page_query_param = "PPP"                  # for the customzie name fromtemd side in serch bar
    # page_size_query_param = "record"          # for the customize record show , like user using this show the record
    # max_page_size = 10                        # for the set customize limit, like user request any number of record  but using this we give limit