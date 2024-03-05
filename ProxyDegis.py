import xml.etree.ElementTree as ET

def update_ppx_with_proxy_list(ppx_file, proxy_list_file):

    tree = ET.parse(ppx_file)
    root = tree.getroot()

    with open(proxy_list_file, 'r') as f:
        proxy_list = f.readlines()

    for proxy_elem, proxy_info in zip(root.findall('.//Proxy'), proxy_list):
        address, port, username, password = proxy_info.strip().split(':')

        proxy_elem.find('Address').text = address
        proxy_elem.find('Port').text = port
        proxy_elem.find('.//Username').text = username
        proxy_elem.find('.//Password').text = password
        proxy_elem.set('type', proxy_type)

    tree.write(r'C:\Users\Adighe\Desktop\CODE\Metin2\ProxyDegis\updated_ppx_file.ppx', encoding='utf-8', xml_declaration=True)


ppx_file_path = r'C:\Users\Adighe\Desktop\CODE\Metin2\ProxyDegis\adighe-yeni.ppx'
proxy_list_file_path = r'C:\Users\Adighe\Desktop\CODE\Metin2\ProxyDegis\proxy.txt'
proxy_type = 'HTTPS' 

# PPX dosyasını güncelle
update_ppx_with_proxy_list(ppx_file_path, proxy_list_file_path)