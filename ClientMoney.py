class Clientmoney:
    def __init__(self, your_money=140):
        self.your_money = your_money

    def get_your_money(self):
        return f"Your Money before the Reservation : {self.your_money}"

    def set_your_money(self):
        if self.your_money >= 100:
            return f"You can use services at the moment and This is the your remaining money : {self.your_money - 100}." \
                   f"Thanks for trusting our Hospital's Services! "
        else:
            return f"You don't have enough money for our services!"

    def giveCampaign(self):
        if (self.your_money - 100) >= 0:
            return "We have a campaign for you!\n"
        else:
            return "You cant enter the campaign. Because you don't enough money for our services\n "
