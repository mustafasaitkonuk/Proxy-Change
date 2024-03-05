import xml.etree.ElementTree as ET

def update_ppx_with_proxy_list(ppx_file, proxy_list_file):
    # PPX dosyasını aç
    tree = ET.parse(ppx_file)
    root = tree.getroot()

    # Proxy listesini oku
    with open(proxy_list_file, 'r') as f:
        proxy_list = f.readlines()

    # Her bir proxy için
    for proxy_elem, proxy_info in zip(root.findall('.//Proxy'), proxy_list):
        address, port, username, password = proxy_info.strip().split(':')

        # Proxy bilgilerini güncelle
        proxy_elem.find('Address').text = address
        proxy_elem.find('Port').text = port
        proxy_elem.find('.//Username').text = username
        proxy_elem.find('.//Password').text = password
        proxy_elem.set('type', proxy_type)

    # Güncellenmiş PPX dosyasını kaydet
    tree.write(r'C:\Users\Adighe\Desktop\CODE\Metin2\ProxyDegis\updated_ppx_file.ppx', encoding='utf-8', xml_declaration=True)

# PPX dosyası ve proxy listesi dosyasının yolları
ppx_file_path = r'C:\Users\Adighe\Desktop\CODE\Metin2\ProxyDegis\adighe-yeni.ppx'
proxy_list_file_path = r'C:\Users\Adighe\Desktop\CODE\Metin2\ProxyDegis\proxy.txt'
proxy_type = 'HTTPS'  # Burada HTTP, HTTPS veya başka bir tür belirtebilirsiniz

# PPX dosyasını güncelle
update_ppx_with_proxy_list(ppx_file_path, proxy_list_file_path)