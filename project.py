
import requests
import re
from bs4 import BeautifulSoup
import os

URL = "https://www.acmicpc.net"

# get html
def get_beautifulsoup(url: str) -> BeautifulSoup:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    return soup

 # this function will replace invalid characters in the file or diretctory names with spaces 
def replace_invalid_characters(filename) -> str:
    invalid_chars = '<>:"/\\|?*'
    pattern = '[' + re.escape(''.join(invalid_chars)) + ']'
    
    return re.sub(pattern, ' ', filename)


def find_stages(soup: BeautifulSoup) -> BeautifulSoup:
    # table = soup.find("table", attrs={"class":"table table-bordered table-striped"})
    table = soup.find("table")      # there is only one table
    stages = table.find_all("a")
    return stages


def make_folder(stages) -> None:        # make directory with the stage name
    # stages = find_stages()    
    # stages = soup.find("table", attrs={"xpath":""})

    for idx, stage in enumerate(stages):
        stage_name = stage.get_text()
        stage_name = replace_invalid_characters(stage_name)
        if (idx + 1) < 10:
            os.makedirs(f"./problems/0{idx+1}_{stage_name}")
        else:
            os.makedirs(f"./problems/{idx+1}_{stage_name}")

def make_quiz_file(stages) -> None:
    list_dir = os.listdir('./problems') # get names of element in problems directory

    for dir_idx, stage in enumerate(stages):

        # for i in len(list_dir):         # preprocessing
        #     list_dir[i] = list_dir[i].split('_')[1]
        
        stage_name = stage.get_text()
        
        soup = get_beautifulsoup(URL+stage['href'])     
        table = soup.find('table', id='problemset')     # get html table element 
        quiz_links = table.find_all('a')                

        idx_quiz = 1
        for quiz_link in quiz_links:
            if quiz_link['href'].startswith("/p"):      # the a tag contains not only name of quiz but also other links
                quiz_name = quiz_link.get_text()
                quiz_name = replace_invalid_characters(quiz_name)
                
                if idx_quiz < 10:

                    with open(f'./problems/{list_dir[dir_idx]}/0{idx_quiz}_{quiz_name}.py', 'w', encoding='utf-8') as f:
                        # pass
                        insert_content(f, quiz_link)
                    
                else:
                    with open(f'./problems/{list_dir[dir_idx]}/{idx_quiz}_{quiz_name}.py', 'w', encoding='utf-8') as f:
                        # pass
                        insert_content(f, quiz_link)

                idx_quiz += 1
                

            else:
                continue       


def insert_content(f, quiz_link) -> None:
    soup = get_beautifulsoup(quiz_link)
    
    problem_name = soup.find('span', id='problem_title')
    problem_number = quiz_link.split('/')[-1]
    problem_content = soup.find('div', id='problem-body')

    f.write(f'url: {quiz_link}')
    f.write(problem_name+'\n')
    f.write(problem_number+'\n')
    f.write(problem_content)



if __name__ == '__main__':
    soup = get_beautifulsoup(URL+'/step')
    stages = find_stages(soup)
    make_folder(stages)
    make_quiz_file(stages)
    

    
