import os


class NumberHandler:

    def choose_number(self):
        folder_path = 'sessions/'
        files = os.listdir(folder_path)
        session_files = []
        number = ''

        for file in files:
            if file.endswith('.pkl'):
                session_files.append(file)

        while True:
            if session_files:
                print('\n-----------------------')
                print('Виберіть номер телефону\n')
            
                count = 0
                for file in session_files:
                    count += 1
                    print(f'{count}. {file}')
                print('add - добавити новий номер')
                
                session_number = input('\nСесія: ')

                if session_number == 'add':
                    new_number = self._add_new_number()

                    if new_number != False:
                        return new_number
                    else:
                        continue
                elif session_number >= str(count) and session_number <= str(count):
                    number = session_files[int(session_number)-1].removesuffix(".pkl")
                    return number
                else:
                    print('\n------------------------------')
                    print('Ви ввели невірний номер сесії!')
                    print('------------------------------')
            else:
                number = str(input('Введіть номер телефону: '))
                new_number = self._number_validation(number)    

                if new_number != False:
                    return new_number
                else:
                    continue

    def _add_new_number(self):
        while True:
            print('\n------------------------------')
            print('Введіть новий номер телефону: ')
            print('(Вернутися назад до списку: back)')

            number = str(input())
                        

            if number == 'back':
                return False
            else:
                verified_number = self._number_validation(number)
                
                if verified_number != False:
                    return verified_number
                else:
                    continue

    def _number_validation(self, number):
        if len(number) > 9:
            return number[-9:]

        if not number.isdigit():
            print('\n----------------------------')
            print('Номер має містити тільки цифри')
            print('------------------------------')

            return False
        
        if len(number) != 9:
            print('\n---------------------------')
            print('Номер містить менше 9 цифр!')
            print('---------------------------')

            return False
