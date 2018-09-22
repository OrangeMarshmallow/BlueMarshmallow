from Plugins.Base import BasePlugin as base


class ConvertPlugin(base):
    def __init__(self):
        super().__init__()
        self.name = 'Конвертор СС'
        self.description = 'Перевод из любой в любую СС'
        self.words = ["конверт", "сс", "cc", "convert", "base"]

    def func(self):
        try:
            nums = self.text.split()
            if len(nums) != 3:
                self.result['message'] = 'Введите число, сс1, сс2'
            else:
                def convert_base(num, to_base=10, from_base=10):
                    n = int(num, from_base) if isinstance(num, str) else int(num)
                    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    return alphabet[n] if n < to_base else convert_base(n // to_base, to_base) + alphabet[n % to_base]
                self.result['message'] = str(convert_base(nums[0], nums[2], nums[1]))
            return True
        except Exception as e:
            self.result['message'] = str(e)
            return False
