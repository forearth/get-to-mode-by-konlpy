from konlpy.tag import Twitter      #명사를 분리/추출하기 위해 한국어 형태소 분석기 konlpy, Twitter는 konlpy 분석 종류중 하나
from collections import Counter     #Counter 객체는 counting hashable container객체로 빈도 수 계산을 위한 사전형태의 데이터 타입

def get_tags(text, ntags=50):
    spliter=Twitter()
    nouns=spliter.nouns(text)
    count=Counter(nouns)
    return_list=[]
    for n, c in count.most_common(ntags):
        temp={'tag':n, 'count':c}
        return_list.append(temp)
    return return_list

def main():    
    text_file_name="full.txt"
    noun_count=40
    output_file_name="res.txt"
    open_text_file=open(text_file_name, 'r', -1, "utf-8")
    text=open_text_file.read()
    tags=get_tags(text, noun_count)
    open_text_file.close()
    open_output_file=open(output_file_name, 'w', -1, "utf-8")
    for tag in tags:
        noun=tag['tag']
        count=tag['count']
        open_output_file.write('{}-{}\n'.format(noun, count))
    open_output_file.close()

if __name__=='__main__':
    main()