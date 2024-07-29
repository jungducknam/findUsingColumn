import re
import module.reader as rd
def parseFiles(file_path):
    matching_list = []
    patterns = [
        re.compile(r'(<select id=".*?">.*?</select>)', re.DOTALL),
        re.compile(r'(<insert id=".*?">.*?</insert>)', re.DOTALL),
        re.compile(r'(<update id=".*?">.*?</update>)', re.DOTALL)
    ]
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # 주석 제거
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        # 개행문자와 탭문자 제거
        content = content.replace('\n', '').replace('\t', '')
        for pattern in patterns:
            matches = pattern.findall(content)
            for match in matches:
                id_match = re.search(r'id="([^"]+)"', match)
                if id_match:
                    id_value = id_match.group(1)
                    matching_list.append({id_value: match})
    return matching_list

def queryFilter(matching_list):
    csv_list = rd.readCsv()
    filtered_list = []

    for item in matching_list:
        for id_value, query in item.items():
            reasons = []
            # 각 쿼리에서 CSV 리스트의 요소가 포함되어 있는지 확인
            for column, table in csv_list:
                if column in query and table in query:
                    reasons.append((column, table))
            # 모든 CSV 리스트 요소가 쿼리에 포함된 경우에만 필터링된 리스트에 추가
            if reasons:
                filtered_list.append({"id": id_value, "query": query, "reasons": reasons})

    return filtered_list

def clearEmptyList(list):
    return [item for item in list if item]