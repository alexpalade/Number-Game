import random
import button


class Game:
    secret_num = ''
    attempts = 0
    MAX_ATTEMPTS = 8

    def gen_secret_num(self):
        while len(self.secret_num) != 4:
            r_num = str(random.randint(0, 9))
            if r_num in self.secret_num:
                continue
            else:
                self.secret_num = self.secret_num + r_num

    def compare(self):
        self.gen_secret_num()

        s_num = self.secret_num
        e_num = button.user_input
        correct_num = 0
        correct_pos = 0
        if e_num == s_num:
            print("You win!")
        else:
            for letter in e_num:
                letter_index = e_num.find(letter)
                if letter == s_num[letter_index]:
                    correct_num += 1
                    correct_pos += 1
                elif e_num[letter_index] in s_num:
                    correct_num += 1
            print("There's " + str(correct_num) + " correct numbers, " + str(correct_pos) +
                  " of them are in the correct position")
            self.attempts += 1
            remaining_attempts = self.MAX_ATTEMPTS - self.attempts
            print("Attempts left: " + str(remaining_attempts))
            if self.attempts >= self.MAX_ATTEMPTS:
                print("You have reached the maximum attempt! You lost")