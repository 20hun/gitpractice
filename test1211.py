import os
import sys
from difflib import SequenceMatcher
import logging
import main2

def test2():
    global job_cnt
    print(job_cnt)
    print(str1)
    print(excel_full_path)

    logging.basicConfig(filename='./server.log', level=logging.DEBUG) # 현재 파일 위치에서 server.log 파일 생성 > log 값 기록

    logging.info('my info log')

    companyCode = '1233'

    print('[2] 회사코드: ' + companyCode + ' - Close [찾기] Window')


def test3():
    print('성공')

test3()

if __name__ == '__main__':
    print(sys.argv)  # 현재 실행한 파이썬 위치
    
    print(__name__)

    str1 = 'abc'
    str2 = 'abc'

    ratio = SequenceMatcher(None, str1, str2).ratio()
    print(ratio)
    # 서로 다른 비율이구나
    str3 = 'abcd'
    str4 = 'dabc'

    ratio2 = SequenceMatcher(None, str3, str4).ratio()
    print(ratio2)

    str5 = 'abcd'
    str6 = 'efgh'

    ratio3 = SequenceMatcher(None, str5, str6).ratio()
    print(ratio3)

    season_year = '2020'
    save_type = '1기'

    excelPath = 'C:\\Users\\lyhgo\\Desktop\\PythonWorkspace\\e'
    storePath = 'C:\\Users\\lyhgo\\Desktop\\PythonWorkspace\\ed'
    seasonPath = os.path.join(storePath, season_year + '_' + save_type)
    if not os.path.isdir(seasonPath): # 해당 디렉토리가 존재하는지 확인
        os.mkdir(seasonPath) # 해당 디렉토리 없으면 만들어줌

    for (path, dir, fileNames) in os.walk(excelPath):
        for fileName in fileNames:
            print(fileName)

        #for pat in path: 경로 1글자씩 다 쪼갠거
        #    print(pat)

            binder_check = ''
            # ex: '9978_이종필_7515100212_매출.xls'
            if len(fileName.split('_')) == 4:
                company_code = fileName.split('_')[0]
                print(company_code)
                company_name = fileName.split('_')[1]
                company_num = fileName.split('_')[2]
                type_name = os.path.splitext(fileName.split('_')[3])[0]
                print(type_name)

                type_nam2 = '매출2'
                if len(type_nam2) >= 3:
                    binder_check = type_nam2[2:]
                    print(type_nam2[0:1])
                    print(binder_check)

                excel_full_path = os.path.join(path, fileName)
                print(excel_full_path)
                save_dir_name = company_code + '_' + company_name
                print(save_dir_name)
                save_excel_path = os.path.join(storePath, seasonPath, save_dir_name)

                if not os.path.isdir(save_excel_path):
                    os.mkdir(save_excel_path)
                print(save_excel_path)

                job_cnt = 1

                test2()
else:
    print(__name__)