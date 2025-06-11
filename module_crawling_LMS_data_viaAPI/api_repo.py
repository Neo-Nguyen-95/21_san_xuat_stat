#%% LIB
import requests
import pandas as pd

#%% REPO CLASS
class APIRepository:
    """Goal: Get all items in the folder, either directly or download files.
    """

    #%%% AUTH TOKEN
    def get_login_token(self):   
        url = "https://steve-api.lotuslms.com/user/login"
        
        payload = {'lname': 'aeglobal',
        'pass': '123',
        'submit': '1',
        '_sand_ajax': '1',
        '_sand_platform': '3',
        '_sand_readmin': '1',
        '_sand_is_wan': 'false',
        '_sand_ga_sessionToken': '',
        '_sand_ga_browserToken': '',
        '_sand_domain': 'aeglobal',
        '_sand_masked': '',
        '_sand_web_url': 'https://aeglobal.lotuslms.com/user/login/?logout=1',
        '_sand_device_uuid': '2aa480b4-2236-4197-9de3-887429bddbbd',
        '_sand_session_id': '23147fd0-b547-465c-a6b9-0924e829378e',
        '_sand_user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0',
        '_sand_ri': 'd7c34309a513c76a09d691c243b42477',
        '_sand_rit': '9d3466563474414814ef2703ff9c3f12:uurl82kqpfAbnBfhjO/Vwho7T/Vgoyp/HnFd2KGbxzCBsmzqlhsfB2BrwTPev86W'}
        files=[
        
        ]
        headers = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0',
          'Accept': 'application/json, text/plain, */*',
          'Accept-Language': 'en-US,en;q=0.5',
          'Accept-Encoding': 'gzip, deflate, br, zstd',
          'Referer': 'https://aeglobal.lotuslms.com/user/login/?logout=1',
          'Origin': 'https://aeglobal.lotuslms.com',
          'Connection': 'keep-alive',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-site',
          'Priority': 'u=0',
          'Cookie': 'name=value'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        
        return response.json()['result']['token']
    
    #%%% NHCH TASK
    def request_into_folder(self, parent_id):
        """ Show list of sub-folders
        """
                
        url = f"https://steve-api.lotuslms.com/content/api/folder-detail?_sand_get_total=0&parent_id={parent_id}&submit=1&page=1&items_per_page=-1&_sand_ajax=1&_sand_platform=3&_sand_readmin=1&_sand_is_wan=false&_sand_ga_sessionToken=&_sand_ga_browserToken=&_sand_domain=aeglobal&_sand_masked=&_sand_session_id=ed9767b7-e0f9-4111-87cb-335cbb102233&_sand_user_agent=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010.15;%20rv:139.0)%20Gecko/20100101%20Firefox/139.0"
        
        payload = {
        '_sand_token': f'{self.get_login_token()}',
        '_sand_uiid': '705519',
        '_sand_ri': 'b9eb13edda2ae0592a8906e0fd59cfc2',
        '_sand_rit': 'a0f7ab3ac247e7748adb97a3dea5e2ed:2zTonxzOw8/YWnvZgj21d4hTRye3jIPZ/if2HOEoFBBrO/JATTPA8M5NP24Cb3sN'}
        
        files=[
        
        ]
        
        headers = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0',
          'Accept': 'application/json, text/plain, */*',
          'Accept-Language': 'en-US,en;q=0.5',
          'Accept-Encoding': 'gzip, deflate, br, zstd',
          'Referer': 'https://aeglobal.lotuslms.com/admin/content-manager/folder/681b22f70d5f2255bd0e52d7',
          'Origin': 'https://aeglobal.lotuslms.com',
          'Connection': 'keep-alive',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-site',
          'Pragma': 'no-cache',
          'Cache-Control': 'no-cache',
          'Cookie': 'name=value'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        
        # print(response.json()['success'])
        
        return response.json()['result']
    
    def request_into_bank(self, bank_id):
        """ Show list of items in a bank
        """

        url = f"https://steve-api.lotuslms.com/question-bank/search-questions?_sand_get_total=0&question_bank%5B%5D={bank_id}&submit=1&page=1&items_per_page=-1&_sand_ajax=1&_sand_platform=3&_sand_readmin=1&_sand_is_wan=false&_sand_ga_sessionToken=&_sand_ga_browserToken=&_sand_domain=aeglobal&_sand_masked=&_sand_session_id=ed9767b7-e0f9-4111-87cb-335cbb102233&_sand_user_agent=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010.15;%20rv:139.0)%20Gecko/20100101%20Firefox/139.0"
        
        payload = {
        '_sand_token': f'{self.get_login_token()}',
        '_sand_uiid': '705519',
        '_sand_ri': '59b78b552eaccf549ef6fbc69b536556',
        '_sand_rit': '7ec15a114a0c41692f50c090e0d72b1b:HjYZyhKRFc1DfuvLjbe7zPhZ6jBL5j2nhm7UQ2auKKpN9N0u+gUYQIGU/ugV/t0L'}
        files=[
        
        ]
        headers = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0',
          'Accept': 'application/json, text/plain, */*',
          'Accept-Language': 'en-US,en;q=0.5',
          'Accept-Encoding': 'gzip, deflate, br, zstd',
          'Referer': 'https://aeglobal.lotuslms.com/admin/content-manager/folder/681b231196ca6c1ab70caf97',
          'Origin': 'https://aeglobal.lotuslms.com',
          'Connection': 'keep-alive',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-site',
          'Pragma': 'no-cache',
          'Cache-Control': 'no-cache',
          'Cookie': 'name=value'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        
        # print(response.json()['success'])
        
        return response.json()['result']
    
    def get_nhch_id(self, grand_parent_id):
        result = {
            'name': [],
            'nhch_id': []
            }

        def walk_folder(parent_id):
            items = self.request_into_folder(parent_id)
           
            for item in items:
                if item['type'] == 'file':
                    result['name'].append(item['name'])
                    result['nhch_id'].append(item['target_item_iid'])
                
                elif item['type'] == 'folder':
                    walk_folder(parent_id=item['id'])
           
                else:
                    print('Weird type detected:', item['type'])

        walk_folder(parent_id=grand_parent_id)

        return pd.DataFrame(result)
    
    def get_nhch_file(self, bank_iid):
        """Input: bank_iid => Output: link of bank file
        """

        url = "https://steve-api.lotuslms.com/question-bank/export/export-questions"
        
        payload = {'bank_iid': f'{bank_iid}',
        'submit': '1',
        '_sand_ajax': '1',
        '_sand_platform': '3',
        '_sand_readmin': '1',
        '_sand_is_wan': 'false',
        '_sand_ga_sessionToken': '',
        '_sand_ga_browserToken': '',
        '_sand_domain': 'aeglobal',
        '_sand_masked': '',
        '_sand_device_uuid': '2aa480b4-2236-4197-9de3-887429bddbbd',
        '_sand_session_id': '73bc493b-258d-424e-b751-e6dc38b33eba',
        '_sand_token': f'{self.get_login_token()}',
        '_sand_uiid': '705519',
        '_sand_uid': '6576b1b5d18d78fd5f032742',
        '_sand_user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0',
        '_sand_ri': 'b7776ca72239fef8ffd243df78e03f37',
        '_sand_rit': 'bf604612f972428831009063dbc8fadc:lJZZ4+lD7IFm14l7Vp9+5nctT+o1mkYbxuOIkKVfSz0v840qACN0c8Rr76vtQir/'}
        files=[
        
        ]
        headers = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0',
          'Accept': 'application/json, text/plain, */*',
          'Accept-Language': 'en-US,en;q=0.5',
          'Accept-Encoding': 'gzip, deflate, br, zstd',
          'Referer': 'https://aeglobal.lotuslms.com/admin/content-manager/folder/677e1f831879aa54870b2004',
          'Origin': 'https://aeglobal.lotuslms.com',
          'Connection': 'keep-alive',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-site',
          'Priority': 'u=0',
          'Pragma': 'no-cache',
          'Cache-Control': 'no-cache',
          'Cookie': 'name=value; name=value'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        
        return response.json()['objects']['url']
    
    #%%% SCORE EXPORT
    
    def get_exercise_iid_in_a_course(self, course_iid):

        url = f"https://steve-api.lotuslms.com/course/marking/get-exercises-in-course?_sand_get_total=0&mode=all&course_iid={course_iid}&submit=1&page=1&items_per_page=-1&_sand_ajax=1&_sand_platform=3&_sand_readmin=1&_sand_is_wan=false&_sand_ga_sessionToken=&_sand_ga_browserToken=&_sand_domain=aeglobal&_sand_masked=&_sand_session_id=73bc493b-258d-424e-b751-e6dc38b33eba&_sand_user_agent=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010.15;%20rv:139.0)%20Gecko/20100101%20Firefox/139.0"
        
        payload = {
        '_sand_device_uuid': '2aa480b4-2236-4197-9de3-887429bddbbd',
        '_sand_token': f'{self.get_login_token()}',
        '_sand_uiid': '705519',
        '_sand_uid': '6576b1b5d18d78fd5f032742',
        '_sand_ri': 'f6b0e68bdf795c4d69d5d04b30f89469',
        '_sand_rit': '1b5fcee61c0911859b1404d4021db3b4:c5aRX28nzAIs/QrG9uONWFtQoU2IK0s5vk/fRu6iewaJHNgu/Xn3yroqjlg1uX/7'}
        
        files=[
        
        ]
        
        headers = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0',
          'Accept': 'application/json, text/plain, */*',
          'Accept-Language': 'en-US,en;q=0.5',
          'Accept-Encoding': 'gzip, deflate, br, zstd',
          'Origin': 'https://aeglobal.lotuslms.com',
          'Connection': 'keep-alive',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-site',
          'Pragma': 'no-cache',
          'Cache-Control': 'no-cache',
          'Cookie': 'name=value'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        
        data = {
            'exercise_name': [],
            'exercise_iid': []
            }
        
        items = response.json()['result']
        
        for item in items:
            data['exercise_name'].append(item['name'])
            data['exercise_iid'].append(item['iid'])
            
        return pd.DataFrame(data)

   
    def get_score_file(self, course_iid, exercise_iid):
        
        url = "https://steve-api.lotuslms.com/take/course/export-for-aeglobal"

        payload = {'exercise_iid': f'{exercise_iid}',
        'course_iid': f'{course_iid}',
        'option_fetching': 'refetch-cache-in-backgroundable',
        'submit': '1',
        '_sand_ajax': '1',
        '_sand_platform': '3',
        '_sand_readmin': '1',
        '_sand_is_wan': 'false',
        '_sand_ga_sessionToken': '',
        '_sand_ga_browserToken': '',
        '_sand_domain': 'aeglobal',
        '_sand_masked': '',
        '_sand_web_url': 'https://aeglobal.lotuslms.com/admin/course/24697770/exercise',
        '_sand_device_uuid': '2aa480b4-2236-4197-9de3-887429bddbbd',
        '_sand_session_id': '73bc493b-258d-424e-b751-e6dc38b33eba',
        '_sand_token': f'{self.get_login_token()}',
        '_sand_uiid': '705519',
        '_sand_uid': '6576b1b5d18d78fd5f032742',
        '_sand_user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0',
        '_sand_ri': '0dc9b7ba3feee9087a9a0af99280ad5f',
        '_sand_rit': 'e19c538f8b10434a0c5a02ffee54a563:rQMlFyLmJ7ewdSsEHVgb5jO2AdFZwXXbhtbh2PrLnBXUafqlOyvKwbWGmXBOcwxl'}
        files=[
        
        ]
        headers = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0',
          'Accept': 'application/json, text/plain, */*',
          'Accept-Language': 'en-US,en;q=0.5',
          'Accept-Encoding': 'gzip, deflate, br, zstd',
          'Referer': 'https://aeglobal.lotuslms.com/admin/course/24697770/exercise',
          'Origin': 'https://aeglobal.lotuslms.com',
          'Connection': 'keep-alive',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-site',
          'Pragma': 'no-cache',
          'Cache-Control': 'no-cache',
          'Cookie': 'name=value'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        
        file_link = response.json()['objects']['url']
        return file_link


        
#%% TRAIL & DEPLOY
repo = APIRepository()

    #%%% ITEM BANK WORK
# items = repo.request_into_folder(parent_id='681dcf80adfe9584320c9851')
# items[0]  # a folder

# items = repo.request_into_bank(27674354)
# items[0]  # an item

# ID of 2025_SX GD T5-T9 = 681b2286f66e30b9980ba9f4
# ID of 2025 = 677ddddf74eea3a33f05abad

# grand_parent_id='677ddddf74eea3a33f05abad'
# df = repo.get_nhch_id(grand_parent_id)

# bank_iid = 24481941
# repo.get_nhch_file(bank_iid)

# df['link'] = df['nhch_id'].map(lambda bank_iid: repo.get_nhch_file(bank_iid))

# df.to_excel('2025_nhch_id.xlsx')

    #%%% STUDENT SCORE 
# item = repo.get_score_file(course_iid=24698734, exercise_iid=26784694)
# item










