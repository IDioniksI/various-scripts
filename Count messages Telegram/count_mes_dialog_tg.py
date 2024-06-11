import json


def count_num_mes_dialog(path):
    filename = path
    with open(filename, encoding='utf8') as file:
        data = json.load(file)

    all_messages = data['messages']
    count_mes_1 = count_mes_2 = 0
    count_voice_1 = count_voice_2 = 0
    count_stickers_1 = count_stickers_2 = 0
    unique_ids_and_names = {}

    for message in all_messages:
        if 'from_id' in message:
            account_id = message['from_id']
            account_name = message['from']
            unique_ids_and_names[account_id] = account_name

    keys_list = list(unique_ids_and_names.keys())
    values_list = list(unique_ids_and_names.values())

    for message in all_messages:
        if 'from_id' in message and message['from_id'] == keys_list[0]:
            count_mes_1 += 1
            if 'media_type' in message and message['media_type'] == "sticker":
                count_stickers_1 += 1
            elif 'media_type' in message and message['media_type'] == "voice_message":
                count_voice_1 += 1
        elif 'from_id' in message and message['from_id'] == keys_list[1]:
            count_mes_2 += 1
            if 'media_type' in message and message['media_type'] == "sticker":
                count_stickers_2 += 1
            elif 'media_type' in message and message['media_type'] == "voice_message":
                count_voice_2 += 1

    print('\033[1m' + '\nMessage statistics' + '\033[0m')
    print(f'{values_list[0]} sent {count_mes_1} messages \n{values_list[1]} sent {count_mes_2} messages \n')
    print(f'{values_list[0]} sent {count_voice_1} voice messages \n{values_list[1]} sent {count_voice_2} voice messages')
    print(f'{values_list[0]} sent {count_stickers_1} stickers \n{values_list[1]} sent {count_stickers_2} stickers')
    return 0


if __name__ == '__main__':
    file_path = r'result.json'
    count_num_mes_dialog(file_path)
