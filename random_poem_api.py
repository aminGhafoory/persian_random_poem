import requests
import re



#+========================+
#|   .::poet numbers::.   |
#|                        |
#|  2==>ÍÇÝÙ              |
#|  3==>ÎíÇã              |
#|  28==>ÈÇÈÇØÇåÑ         |
#|  26==>ÇÈæÓÚíÏ ÇÈæÇáÎíÑ |
#|                        |  
#+========================+


def get_poem(poet_number):
    #request webpage
    if poet_number==0:
        r=requests.get("http://c.ganjoor.net/beyt.php")
        source_txt=r.text
    else:
        r=requests.get(f"http://c.ganjoor.net/beyt.php?p={poet_number}")
        source_txt=r.text
    #parse data
    regex_m1=r'class="ganjoor-m1">(.*)<\/div>'
    regex_m2=r'class="ganjoor-m2">(.*)<\/div>'
    regex_poet=r'\/">(.*)<\/a>'

    m1_list=re.findall(regex_m1,source_txt)
    m1_strig=m1_list[0]

    m2_list=re.findall(regex_m2,source_txt)
    m2_strig=m2_list[0]

    poet_list=re.findall(regex_poet,source_txt)
    poet_string=poet_list[0]
    return m1_strig,m2_strig,poet_string

get_poem(2)
print(get_poem(2))
