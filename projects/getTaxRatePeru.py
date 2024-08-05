import requests
from bs4 import BeautifulSoup
# ? pip install requests

url='https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx'

cookiesBrowser='''.ASPXANONYMOUS=b_KrWpfggFRKpi2n-P_H_9VpH0T4m4YaD5B9C5e9M38YQq1trLSsraRphMzTa3p4bpfjXaMA9KAEEmkpofVL0Xgm-IsgKN-TkBxLXGJk4tY8I0p90; visid_incap_2355492=xF6B26PlTmOYcbuxfE0Od06RjmYAAAAAQUIPAAAAAABTZ5bfnNGVwWHFoVs4x/my; ASP.NET_SessionId=tzeb4zkkhneunhefdjmrxdyx; incap_ses_1721_2355492=oE/RT6HzIE+WQVFUgjjiFyJFsWYAAAAAG7RKWp9K0PPPkpOzlitK/A==; ASPSESSIONIDAADSDDRT=HCKELFDAGIFACHJHPEHLBMBM; dnn_IsMobile=False; language=es-ES; __RequestVerificationToken=pJEuxmpo1J_QjuKnFU1zAvfLMZ-gxDk8iNWex7k4u9KT8tx22uSs1bbl9hEou-X_DxqwqQ2; _ga=GA1.3.296666253.1720619344; _gid=GA1.3.1371486480.1722896359; _ga_M92VDMFGFM=GS1.3.1722896359.3.0.1722896359.0.0.0; _ga_XK0K3P9NPZ=GS1.1.1722896358.3.0.1722896525.0.0.0; TS01fc2e41=019955ae1604f6ffe6991d2a0e3f6ea16fd34a82501af2b35bc80ef9e03447f82230ac8c32a4e3d8d8e90a4f621f40f9f912fcf8d25c5746c478cd64d21547b0645d4dc7d4b4953e31780d43940672b50c735c7d57935058a3ecb085acdd506b864a22b96265efa0389798b196cbe1a40d76edd438fb85b9d010db9f6ad45660ec35b5473162a474ff9b273625bb4554964fee6a589e9497ecf03ee7fce6a89ae5bf234131a835751b57ea52273bf56a4c7498be7dfdfe48e08cd6f1e1717b78544f80f6c3
'''
cookies = dict()
taxRate = dict()

for ck in cookiesBrowser.split(';'):
    tmp = ck.split('=')
    cookies[tmp[0].strip()]=tmp[1].strip()

html_http_response = requests.get(url, cookies=cookies)
data = html_http_response.text
soup = BeautifulSoup(data, "html.parser")
tableWithData=soup.find('table',id='ctl00_cphContent_rgTipoCambio_ctl00')
for cell in tableWithData.find_all('td',class_='APLI_fila2'):
    print(cell.text)