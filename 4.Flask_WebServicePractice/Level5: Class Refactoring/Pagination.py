import math
# 입력값: 데이터(list), 현재페이지, 한페이지에 보일 데이터수, pagination에 보일 페이지 수(홀수)
# 출력값: start_index, end_index, pagination_start, pagination_end, move_page_front, move_page_back
class Pagination:
    def makepagination(self, data, page, data_per_page=10, page_per_pagination=5):
        num_data = len(data) # data에 있는 정보의 개수
        total_page = math.ceil(num_data / data_per_page) # 전체 페이지 개수
        start_index = (page-1) * data_per_page # 현재 페이지의 첫번째 데이터의 index

        # 페이지에 따른 마지막 정보의 index값
        if page < total_page:
            end_index = page * data_per_page - 1 #전체 페이지
        else:
            end_index = num_data - 1

        # 페이지에 따라 밑에 보여야 하는 페이지 넘기기 정보(가운데에 지금 페이지!)
        if total_page >= page_per_pagination:
            if page <= 1+ page_per_pagination//2:
                pagination_start, pagination_end = 1, page_per_pagination
                move_page_front, move_page_back = False, True
            elif page <= total_page - page_per_pagination//2:
                pagination_start, pagination_end = page - page_per_pagination//2, page + page_per_pagination//2
                move_page_front, move_page_back = True, True
            else:
                pagination_start,pagination_end = total_page - page_per_pagination + 1,total_page
                move_page_front, move_page_back = True, False

        else:
            pagination_start, pagination_end = 1, total_page
            move_page_front, move_page_back = False, False
        
        return start_index, end_index, total_page, pagination_start, pagination_end, move_page_front, move_page_back