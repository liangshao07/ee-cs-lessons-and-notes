import urllib.request

'''
    Now a simple crawler batch download file is implemented
    Although only in the form of inferred download links to achieve bulk
    The next step is to implement, simulate click the web page, copy the link, download
    The next step, related, crawls web article content

    现在实现了简单的爬虫批量下载文件
    虽然只是通过推断下载链接的形式实现批量
    下一步是实现，模拟点击网页，复制链接，下载
    下下一步，相关，爬取网页文章内容
'''

arr = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']
# for i in arr:
#     print(f'zhe{i}test')

# for i in arr:
#     url = f'https://sp18.datastructur.es/materials/discussion/disc{i}sol.pdf'
#     urllib.request.urlretrieve(url, f'cs61b-disc{i}sol.pdf')
#     print(i)

# examprep from 02 to ?
# url = 'https://sp18.datastructur.es/materials/discussion/examprep02.pdf'
# urllib.request.urlretrieve(url, f'cs61b-examprep01.pdf')

arrexamprep = ['02','03','04','05','06','07','08','09','10','11','12','13','14','15']

for i in arrexamprep:
    url = f'https://sp18.datastructur.es/materials/discussion/examprep{i}sol.pdf'
    urllib.request.urlretrieve(url, f'cs61b-examprep{i}sol.pdf')
    print(i)
